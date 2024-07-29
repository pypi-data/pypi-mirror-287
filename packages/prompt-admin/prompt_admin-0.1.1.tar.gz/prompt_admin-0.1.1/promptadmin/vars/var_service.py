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
            conn = await asyncpg.connect(SETTINGS.connections[self.connection])
        except Exception as e:
            logger.error('Error connection database for get vars', exc_info=e)
            return {}

        row = await conn.fetch('SELECT key, value FROM pa_var')

        return {
            i.get('key'): i.get('value') for i in row
        }
