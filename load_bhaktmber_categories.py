import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'composeexample.settings'

import django
django.setup()

from temple_audit.models import BhaktamberCategories


bhaktamber_categoris = ('Birth day', 'Anniversary', 'Memory day', 'temple day', 'other')

for data in bhaktamber_categoris:
    p = BhaktamberCategories(
        reason=data
    )
    p.save()
