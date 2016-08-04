from datetime import datetime, timedelta

from mongoengine.queryset import DoesNotExist, MultipleObjectsReturned
from scrapy.dupefilters import RFPDupeFilter

from immobilier.mongodb.models import RawPage
from immobilier.apps.scrapy_crawl.settings import RECRAWLING_DELAY


RECRAWLING_TIME_DELTA = timedelta(days=RECRAWLING_DELAY)


class MongoStorageFilter(RFPDupeFilter):
    def request_seen(self, request):
        rfp_seen = super(MongoStorageFilter, self).request_seen(request)
        if rfp_seen:
            return rfp_seen
        else:
            try:
                RawPage.objects.filter(
                    fetch_at__lte=datetime.utcnow() - RECRAWLING_TIME_DELTA).get(url=request.url)
            except DoesNotExist:
                return False
            except MultipleObjectsReturned:
                return True
            return True
