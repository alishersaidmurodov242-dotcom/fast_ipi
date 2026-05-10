from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    allowed_origins: str = "http://localhost:3000"
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(",")]

settings = Settings()