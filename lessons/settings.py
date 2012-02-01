from django.conf import settings
from django.db.models import Q

DEFAULT_SETTINGS = {
    'RELATION_MODELS': [],
}

DEFAULT_SETTINGS.update(getattr(settings, 'LESSON_SETTINGS', {}))

globals().update(DEFAULT_SETTINGS)

RELATIONS = [Q(app_label=al, model=m) for al, m in [x.split('.') for x in RELATION_MODELS]]
