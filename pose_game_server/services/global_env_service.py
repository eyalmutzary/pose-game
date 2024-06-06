from typing import Dict
from dal.global_env_dal import GlobalEnvDAL
from models.global_env import GlobalEnvModel


class GlobalEnvService:
    @staticmethod
    async def create_global_env(model: GlobalEnvModel) -> str:
        created_id = await GlobalEnvDAL.create(model)
        return created_id

    @staticmethod
    async def get_latest_global_env(platform: str) -> GlobalEnvModel:
        latest_version: int = await GlobalEnvDAL.get_count(platform)
        latest_env: GlobalEnvModel = await GlobalEnvDAL.get_env(latest_version, platform)
        return latest_env

    @staticmethod
    async def get_by_version(version: int, platform: str) -> GlobalEnvModel:
        return await GlobalEnvDAL.get_env(version, platform)

    @staticmethod
    async def get_latest_version_number(platform: str) -> int:
        return await GlobalEnvDAL.get_count(platform)

    @staticmethod
    async def get_all_latest_envs() -> Dict[str,GlobalEnvModel]:
        """
            Get all latest global environments (one of every platform)
        """
        all_envs = await GlobalEnvDAL.get_all()
        # filter out the latest version of each platform
        latest_envs = {}
        for env in all_envs:
            if env.platform not in latest_envs or env.version > latest_envs[env.platform].version:
                latest_envs[env.platform] = env
        return latest_envs