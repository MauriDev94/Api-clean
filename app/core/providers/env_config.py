from functools import lru_cache
from app.core.config.env_config import EnvConfig


@lru_cache()
def get_env_config() -> EnvConfig:
    """get environmet cofiguration

    Returns:
        EnvConfig: _description_
    """
    return EnvConfig()  # type: ignore
