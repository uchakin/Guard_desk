from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    all_formatted_visits = []
    for visit in visits:
      duration = visit.get_duration()
      this_passcard_visit = {
              "entered_at": visit.entered_at,
              "duration": Visit.format_duration(duration),
              "is_strange": Visit.is_visit_long(duration)
              }
      all_formatted_visits.append(this_passcard_visit)

    context = {
        "passcard": visit,
        "this_passcard_visits": all_formatted_visits
    }
    return render(request, 'passcard_info.html', context)
