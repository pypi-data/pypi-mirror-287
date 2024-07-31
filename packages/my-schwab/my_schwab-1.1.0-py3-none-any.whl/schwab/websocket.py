# Standard library imports
import asyncio
import atexit
import certifi
from datetime import datetime
import ssl
import signal
import sys
from traceback import print_exc


# Third party imports
from asynchronizer import Asynchronizer
import orjson as json
import websockets

# Local imports
from .client import Client
from .enums.websocket import Command, Service
from .utils import from_enum

def _logout(websocket):
    with Asynchronizer() as executor:
        executor.run(websocket.logout())

class Websocket:
    __slots__ = ('_client_params', '_conn', '_sub_id', '_preferences', '_ssl_context', '_stop', '_loop')

    def __init__(self, loop=None, **client_params):
        self._client_params = client_params
        self._ssl_context = ssl.create_default_context()
        self._ssl_context.load_verify_locations(certifi.where())
        self._stop = asyncio.Event()
        self._sub_id = 0

        with Client(fetch=False, **client_params) as client:
            self._preferences = client.user_preferences

        if loop is None:
            try:
                self._loop = asyncio.get_running_loop()
            except RuntimeError as e:
                print(f"Error initializing websocket: {e}")
                self._loop = asyncio.get_event_loop()
        else:
            self._loop = loop

        # atexit.register(_logout, self)
        # self._register_cleanup()

    @property
    def sub_id(self):
        self._sub_id += 1
        return self._sub_id

    def _cleanup(self):
        print("Running cleanup...")
        self.logout()
        print("Cleanup done.")

    def _build_request(self, service, command, params):
        return json.dumps({
            'requests': [{
                'requestid': self.sub_id,
                'service': from_enum(Service, service),
                'command': from_enum(Command, command),
                'SchwabClientCustomerId': self._preferences.client_customer_id,
                'SchwabClientCorrelId': self._preferences.client_correl_id,
                'parameters': params
            }]
        }).decode('utf-8')

    async def logout(self, conn=None):
        conn = conn or self._conn
        params = self._build_request('admin', 'logout', {})
        await conn.send(params)
        print(await conn.recv())
        self._stop.set()

    async def login(self):
        with Client(**self._client_params) as client:
            access_token = client.token.access_token

        params = {
            'Authorization': access_token,
            'SchwabClientChannel': self._preferences.client_channel,
            'SchwabClientFunctionId': self._preferences.client_function_id,
        }
        params = self._build_request('admin', 'login', params)

        await self._conn.send(params)
        print(await self._conn.recv())

    async def subscribe_equities(self, symbols, fields=(0, 3, 8)):
        fields = sorted(fields)
        symbols = ','.join(symbols)
        fields = ','.join(str(n) for n in fields)
        params = {
            'keys': symbols,
            'fields': fields,
        }
        params = self._build_request('equities', 'subs', params)
        await self._conn.send(params)
        print(await self._conn.recv())

    async def subscribe_account(self):
        params = {
            'keys': 'account_activity',
            'fields': '0,1,2,3'
        }
        params = self._build_request('account_activity', 'subs', params)
        await self._conn.send(params)
        print(await self._conn.recv())

    async def subscribe(self, subscription):
        try:
            subscription, args = subscription
            await subscription(*args)
        except ValueError:
            await subscription[0]()

    async def stream(self, subscriptions=(), handler=None, stop_time=None, infinite=False):
        iscoroutine = asyncio.iscoroutinefunction(handler)

        if infinite:
            async for conn in websockets.connect(self._preferences.ws_url, ping_interval=5):
                self._conn = conn
                try:
                    await self.login()
                    for subscription in subscriptions:
                        await self.subscribe(subscription)
                    print('Successfully authenticated and subscribed. Streaming...')

                    while True:
                        res = await conn.recv()
                        res = json.loads(res)
                        if handler is not None:
                            if iscoroutine:
                                await handler(res)
                            else:
                                handler(res)

                        if stop_time is not None:
                            if datetime.now().time() >= stop_time:
                                await self.logout()
                                sys.exit(0)

                        if self._stop.is_set():
                            break

                except Exception as e:
                    print_exc()
                    self._sub_id = 0
                    continue

        else:
            async with websockets.connect(self._preferences.ws_url, ping_interval=5) as conn:
                self._conn = conn
                try:
                    await self.login()
                    for subscription in subscriptions:
                        await self.subscribe(subscription)
                    print('Successfully authenticated and subscribed. Streaming...')

                    while True:
                        res = await conn.recv()
                        res = json.loads(res)
                        if handler is not None:
                            if iscoroutine:
                                await handler(res)
                            else:
                                handler(res)

                        if stop_time is not None:
                            if datetime.now().time() >= stop_time:
                                await self.logout()
                                sys.exit(0)

                        if self._stop.is_set():
                            break

                except Exception as e:
                    print_exc()
                    self._sub_id = 0