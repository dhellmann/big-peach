from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from events.models import Event


class IndexView(TemplateView):
    ''' Index Page '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        now = timezone.now()
        four_weeks_from_now = now + timedelta(weeks=4)

        context['events'] = Event.objects.filter(
            published=True, start__gte=now, start__lte=four_weeks_from_now)
        return context