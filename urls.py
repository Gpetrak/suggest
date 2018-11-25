from django.conf.urls import patterns, url

from crete_gis.suggest.views import SuggestView

urlpatterns = patterns(
    'crete_gis.suggest.views',
    # Suggest
    url(r'^$', SuggestView.as_view(), name='suggest'),
)
