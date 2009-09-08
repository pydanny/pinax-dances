from django.conf.urls.defaults import *

from dances.models import Dance

from groups.bridge import ContentBridge


bridge = ContentBridge(Dance, 'dances')


urlpatterns = patterns('',
    url(r'^your_dances/$', 'dances.views.your_dances', name="your_dances"),
    url(r'^$', 'dances.views.dances', name="dance_list"),
)


urlpatterns += bridge.include_urls('topics.urls', r'^dance/(?P<dance_slug>[-\w]+)/wall/')