from django.shortcuts import render
from django.utils.timezone import utc, now
import datetime

def home(request):
    today = datetime.date.today()
    now_native = datetime.datetime.now()
    now_aware = datetime.datetime.utcnow().replace(tzinfo=utc)
    return render(request, "taskbuster/index.html", {'today': today, 'now': now()})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")