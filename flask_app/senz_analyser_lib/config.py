__all__ = ["LOGENTRIES_TOKEN", "APP_ENV", "BUGSNAG_TOKEN"]
import os

# Settings

LOGENTRIES_DEV_TOKEN = "be1d8b07-4159-4a03-b6cf-b240a8aba75e"
LOGENTRIES_PROD_TOKEN = "cfe1f162-8726-4eb1-83e2-96452dcfc686"
LOGENTRIES_LOCAL_TOKEN = "be1d8b07-4159-4a03-b6cf-b240a8aba75e"

BUGSNAG_DEV_TOKEN = "c66016203d2dc0f77e7620e132160199"
BUGSNAG_PROD_TOKEN = "ecc2e62fafbbcc897d16c6bdd03632d7"
BUGSNAG_LOCAL_TOKEN = "c66016203d2dc0f77e7620e132160199"

LOGENTRIES_TOKEN = ""
BUGSNAG_TOKEN = ""
APP_ENV = ""

# Configuration

try:
    APP_ENV = os.environ["APP_ENV"]
except KeyError, key:
    print "KeyError: There is no env var named %s" % key
    print "The local env will be applied"
    APP_ENV = "local"
finally:
    if APP_ENV == "test":
        LOGENTRIES_TOKEN = LOGENTRIES_DEV_TOKEN
        BUGSNAG_TOKEN = BUGSNAG_DEV_TOKEN
    elif APP_ENV == "prod":
        LOGENTRIES_TOKEN = LOGENTRIES_PROD_TOKEN
        BUGSNAG_TOKEN = BUGSNAG_PROD_TOKEN
    elif APP_ENV == "local":
        LOGENTRIES_TOKEN = LOGENTRIES_LOCAL_TOKEN
        BUGSNAG_TOKEN = BUGSNAG_LOCAL_TOKEN
