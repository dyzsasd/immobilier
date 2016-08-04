from __future__ import unicode_literals

from datetime import datetime

from mongoengine import Document
from mongoengine.fields import StringField, DateTimeField


class RawPage(Document):
    url = StringField(unique=True)
    canonical_url = StringField(unique=True)
    fetch_at = DateTimeField(default=datetime.utcnow)
    body = StringField(default='')
    meta = {
        'indexes': [
            '#url',
        ]
    }

