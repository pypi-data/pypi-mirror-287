from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

try:
    import pytz
except ImportError:
    raise ImportError(  # noqa: B904
        "Install `pytz` package. Run `pip install pytz`."
    )

from sage_tools.forms.timezone import TimezoneForm
from sage_tools.handlers.session import SessionHandler


class TimezoneUpdateView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        form = TimezoneForm(request.POST)
        if form.is_valid():
            tzname = form.cleaned_data['timezone']
            next_url = form.cleaned_data['next']
            if tzname in pytz.all_timezones:
                session_handler = SessionHandler(request)
                session_handler.set('user_timezone', tzname)
            return redirect(next_url)
        return redirect('/')
