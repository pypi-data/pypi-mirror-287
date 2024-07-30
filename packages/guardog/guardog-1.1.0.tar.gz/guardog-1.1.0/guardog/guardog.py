import json
import pytz
import asyncio
import httpx
import traceback
import importlib.metadata

from datetime import datetime

from .settings import BACKEND_APP_CRASH_ALERTS_URL


version = importlib.metadata.version('guardog')


def current_utc_datetime():
    return datetime.now(tzinfo=pytz.utc)


async def alert(uid: str, service_id: str, api_key: str, datetime: datetime, log: str, tag: str | None):

    async with httpx.AsyncClient() as client:

        try:
            response = await client.post(
                BACKEND_APP_CRASH_ALERTS_URL + f'/v{version}/uid/{uid}/service-id/{service_id}/alert',
                data=json.dumps({
                    'datetime': datetime.isoformat(),
                    'log': log,
                    'tag': tag
                }),
                headers={
                    'X-API-KEY': api_key,
                    'content-type': "application/json"
                }
            )

            if response.status_code == 200:
                pass
            else:
                raise httpx.RequestError(response.text, request=response.request)
        except httpx.RequestError as e:
            raise e


class Guardog:

    def __init__(self, api_key: str, uid: str, service_id: str):

        self.api_key = api_key
        self.uid = uid
        self.service_id = service_id

    def watch(self, tag=None):

        def inner(func):
            if asyncio.iscoroutinefunction(func):
                async def async_wrapper(*args, **kwargs):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        dt = current_utc_datetime()
                        await alert(
                            uid=self.uid,
                            service_id=self.service_id,
                            api_key=self.api_key,
                            datetime=dt,
                            log=traceback.format_exc(),
                            tag=tag
                        )
                        raise
                return async_wrapper
            else:
                def sync_wrapper(*args, **kwargs):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        dt = current_utc_datetime()
                        asyncio.run(alert(
                            uid=self.uid,
                            service_id=self.service_id,
                            api_key=self.api_key,
                            datetime=dt,
                            log=traceback.format_exc(),
                            tag=tag
                        ))
                        raise
                return sync_wrapper

        return inner

    def alert(self, error_log: str, tag: str = None):

        dt = current_utc_datetime()
        asyncio.run(
            alert(
                uid=self.uid,
                service_id=self.service_id,
                api_key=self.api_key,
                datetime=dt,
                log=error_log,
                tag=tag
            )
        )
