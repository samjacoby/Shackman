from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from btype.models import Typeface, Variant

urlpatterns = patterns('btype.views',
            (r'^$', 'update'),
)

