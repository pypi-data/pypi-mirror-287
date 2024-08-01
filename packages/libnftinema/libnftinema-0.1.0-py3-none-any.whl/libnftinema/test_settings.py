from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "your_secret_key"
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "libnftinema.testapp",
]
AUTH_USER_MODEL = "testapp.TestUser"
MIDDLEWARE = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
USE_I18N = False
USE_L10N = False
USE_TZ = False

NFTINEMA_CLIENT_SECRET = "xxx"
