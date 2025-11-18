from flask_marshmallow import Marshmallow #Importing Marshmallow class
from flask_limiter import Limiter #Importing Limiter class
from flask_limiter.util import get_remote_address #Importing utility to get remote address
from flask_caching import Cache


ma = Marshmallow()
limtter = Limmiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

cache = Cache()