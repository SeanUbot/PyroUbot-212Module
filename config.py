import os
from dotenv import load_dotenv

load_dotenv(".env")


def _get_int(name: str, default: str | None = None) -> int:
    """Read int env var with a helpful error if missing."""
    val = os.getenv(name, default)
    if val is None or str(val).strip() == "":
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            "Set it in your .env file."
        )
    return int(val)


def _get_str(name: str, default: str | None = None) -> str:
    """Read str env var with a helpful error if missing."""
    val = os.getenv(name, default)
    if val is None or str(val).strip() == "":
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            "Set it in your .env file."
        )
    return str(val)

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "").split()))

API_ID = _get_int("API_ID")

API_HASH = _get_str("API_HASH")

BOT_TOKEN = _get_str("BOT_TOKEN")

OWNER_ID = _get_int("OWNER_ID")

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split()))

RMBG_API = os.getenv("RMBG_API", "")

MONGO_URL = _get_str("MONGO_URL")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4912568273"))
