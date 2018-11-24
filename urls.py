from django.conf.urls import patterns, url

from suggest.views import SuggestView

urlpatterns = patterns('',
    # Suggest
    url(r'^$', SuggestView.as_view(), name='suggest'),
)