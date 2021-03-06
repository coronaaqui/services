from django.db.models import Sum, Q, Value, Count
from django.db.models.functions import Coalesce

from rest_framework import filters

from cbrasil.organizations.models import Sectors
from cbrasil.helpers import get_closed_events_filters, get_region_filter

class SectorsAggregationFilters(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        region__initial = request.GET.get('region__initial', None)
        actually_closed = request.GET.get('actually_closed', False)
        ordering = request.GET.get('ordering', None)
        has_both_correct_dates, has_undefined_ends_date = get_closed_events_filters(region__initial)
        q = Sectors.objects
        
        if region__initial and actually_closed == 'True':
            q = q.annotate(total_estimated_impact=Coalesce(Sum('events__estimated_impact', filter=has_both_correct_dates| has_undefined_ends_date), Value(0)))
            q = q.annotate(events_count=Coalesce(Count('events', filter=has_both_correct_dates| has_undefined_ends_date), Value(0)))
        elif region__initial:
            q = q.annotate(total_estimated_impact=Coalesce(Sum('events__estimated_impact', filter=Q(get_region_filter(region__initial))), Value(0)))
            q = q.annotate(events_count=Coalesce(Count('events', filter=Q(get_region_filter(region__initial))), Value(0)))
        elif actually_closed:
            q = q.annotate(total_estimated_impact=Coalesce(Sum('events__estimated_impact', filter=has_both_correct_dates| has_undefined_ends_date), 0))
            q = q.annotate(events_count=Coalesce(Count('events', filter=has_both_correct_dates| has_undefined_ends_date), Value(0)))
        else:
            q = q.annotate(total_estimated_impact=Coalesce(Sum('events__estimated_impact'), Value(0)))
            q = q.annotate(events_count=Coalesce(Count('events'), Value(0)))

        if ordering in ['events_count', 'total_estimated_impact']:
            q = q.order_by('-{}'.format(ordering))
        return q