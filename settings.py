import logging
import sys
from typing import Union, Optional

from pydantic import BaseSettings, IPvAnyAddress, AnyUrl


class Settings(BaseSettings):
    DEBUG: bool = False
    PORT: int = 5002
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    SENTRY_DNS: Optional[AnyUrl]


settings = Settings(_env_file='.env')
