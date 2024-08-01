import logging

import asyncpg

from settings import SETTINGS

logger = logging.getLogger(__name__)


class VarService:
    def __init__(
            self,
            connection: str = None
    ):
        self.connection = connection or SETTINGS.prompt_admin_settings.var_connection

    async def collect_vars(self) -> dict[str, str]:
        try:
            conn = await asyncpg.connect(self.connection)
        except Exception as e:
            logger.error('Error connection database for get vars', exc_info=e)
            return {}

        row = await conn.fetch('SELECT key, value FROM pa_var')

        return {
            i.get('key'): i.get('value') for i in row
        }

    async def create(self, key: str, value: str):
        try:
            conn = await asyncpg.connect(self.connection)
        except Exception as e:
            logger.error('Error connection database for get vars', exc_info=e)
            return

        await conn.fetch(f'INSERT INTO pa_var (key, value) VALUES (\'{key}\', \'{value}\')')

    async def change(self, key: str, value: str):
        try:
            conn = await asyncpg.connect(self.connection)
        except Exception as e:
            logger.error('Error connection database for get vars', exc_info=e)
            return

        await conn.fetch(f'UPDATE pa_var SET value=\'{value}\' WHERE key=\'{key}\'')

    async def remove(self, key: str):
        try:
            conn = await asyncpg.connect(self.connection)
        except Exception as e:
            logger.error('Error connection database for get vars', exc_info=e)
            return

        await conn.fetch(f'DELETE FROM pa_var WHERE key=\'{key}\'')
