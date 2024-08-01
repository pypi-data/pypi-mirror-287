from django.urls import path

from sage_tools.views.timezone import TimezoneUpdateView

app_name = "sage_tools"
urlpatterns = [
    path('update-timezone/', TimezoneUpdateView.as_view(), name='timezone_update'),
]
