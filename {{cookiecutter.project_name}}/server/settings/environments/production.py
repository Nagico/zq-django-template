from server.settings.components import config
from server.settings.components.configs import CacheConfig, DatabaseConfig

# debug 模式
DEBUG = config("DJANGO_DEBUG", False, cast=bool)

ALLOWED_HOSTS = [
    # Add your domain here
]

SERVER_URL = config("SERVER_URL", "https://")

# region Cache
# Redis
CacheConfig.url = "redis://redis"
CACHES = CacheConfig.get()

{%- if cookiecutter.use_celery == 'y' %}
CELERY_BROKER_URL = "redis://redis/0"
{%- endif %}
# endregion
