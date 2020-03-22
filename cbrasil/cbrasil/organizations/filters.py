from django.db.models import Count, Q

from rest_framework import filters

from cbrasil.organizations.models import Sectors
from cbrasil.helpers import get_closed_events_filters

class SectorsAggregationFilters(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        region__initial = request.GET.get('region__initial', None)
        actually_closed = request.GET.get('actually_closed', False)
        q = Sectors.objects
        if region__initial and actually_closed == 'True':
            has_both_correct_dates, has_undefined_ends_date = get_closed_events_filters(region__initial)
            q = q.annotate(total_events=Count('events', filter=has_both_correct_dates| has_undefined_ends_date))
        elif region__initial:
            q = q.annotate(total_events=Count('events', filter=Q(events__region__initial=region__initial)))
        elif actually_closed:
            has_both_correct_dates, has_undefined_ends_date = get_closed_events_filters(region__initial)
            q = q.annotate(total_events=Count('events', filter=has_both_correct_dates| has_undefined_ends_date))
        else:
            q = q.annotate(total_events=Count('events'))
        return q.order_by('-total_events', 'name')