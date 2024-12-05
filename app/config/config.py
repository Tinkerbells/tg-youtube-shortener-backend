from dataclasses import dataclass

from dotenv import load_dotenv

from .base import getenv, ImproperlyConfigured


@dataclass
class YandexGPT:
    folder_id: str
    auth: str


@dataclass
class Config:
    gpt: YandexGPT


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment valriables
    load_dotenv()

    return Config(
        gpt=YandexGPT(folder_id=getenv("FOLDER_ID"), auth=getenv("YANDEX_API_KEY"))
    )
