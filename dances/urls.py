from django.conf.urls.defaults import *

from dances.models import Dance

from groups.bridge import ContentBridge


bridge = ContentBridge(Dance, 'dances')


urlpatterns = patterns('',
    url(r'^add_dance$', 'dances.views.add', name="dance_add"),
    url(r'^your_dances/$', 'dances.views.your_dances', name="your_dances"),
    url(r'^$', 'dances.views.dances', name="dance_list"),
)


urlpatterns += bridge.include_urls('wall.urls', r'^dance/(?P<group_slug>[-\w]+)/wall/')