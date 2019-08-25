from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def storage_information_view(request):
    all_visiters = Visit.objects.filter(leaved_at=None)
    visiter_formatted = []
    for visiter in all_visiters:
      time = visiter.get_duration()
      non_closed_visit = {
            "who_entered": visiter.passcard.owner_name,
            "entered_at": visiter.entered_at,
            "duration": Visit.format_duration(time),
            }
      visiter_formatted.append(non_closed_visit)
    
    context = {
          "non_closed_visits": visiter_formatted,
          }
    return render(request, 'storage_information.html', context)
