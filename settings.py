import logging
import sys
from typing import Union, Optional

from pydantic import BaseSettings, IPvAnyAddress, AnyUrl


class Settings(BaseSettings):
    DEBUG: bool = False
    PORT: int = 5002
    HOST: Union[IPvAnyAddress, AnyUrl] = '0.0.0.0'
    SENTRY_DNS: Optional[AnyUrl]
    EMAIL_SENDER: str
    PASS: str
    EMAIL_RECIPIENT: str
    PORT_SMTP: int
    SMTP_SERVER: str


settings = Settings(_env_file='.env')
