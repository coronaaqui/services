from datetime import datetime
from django.db.models import Q

def get_region_filter(region__initial):
    return (Q(events__region__initial=region__initial) | Q(events__city__region__initial=region__initial)) 

def get_closed_events_filters(region__initial):
    today = datetime.today()
    if region__initial:
        HAS_BOTH_CORRECT_DATES = Q(get_region_filter(region__initial),events__from_date__lte=today,events__from_date__gte=today)
        HAS_UNDEFINED_ENDS_DATE = Q(get_region_filter(region__initial),events__from_date__lte=today,events__undefined_ends_date=True)
    else:
        HAS_BOTH_CORRECT_DATES = Q(events__from_date__lte=today,events__from_date__gte=today)
        HAS_UNDEFINED_ENDS_DATE = Q(events__from_date__lte=today,events__undefined_ends_date=True)
    return HAS_BOTH_CORRECT_DATES, HAS_UNDEFINED_ENDS_DATE