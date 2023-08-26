{%- if cookiecutter.use_celery == 'y' %}
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app
{%- endif %}

__version__ = "{{cookiecutter.version}}"
__all__ = (
{%- if cookiecutter.use_celery == 'y' %}
    "celery_app",
{%- endif %}
    "__version__",
)
