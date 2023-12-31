from typing import Optional

from pydantic import BaseSettings, EmailStr

VERSION_SHEETS = 'v4'
ROW = 100
COLUMN = 11
VERSION_DRIVE = 'v3'
RANGE = 'A1:E30'


class Settings(BaseSettings):
    app_title: str = 'Фонд поддержки котиков QRKot'
    database_url: str = 'sqlite+aiosqlite:///./QRKotData.db'
    secret: str = 'mysecret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
