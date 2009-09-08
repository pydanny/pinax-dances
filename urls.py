from django.conf.urls.defaults import *

from dance.models import Dance

from groups.bridge import ContentBridge


bridge = ContentBridge(BasicGroup, 'basic_groups')


urlpatterns = patterns('',
    url(r'^your_groups/$', 'basic_groups.views.your_groups', name="your_groups"),
    url(r'^$', 'basic_groups.views.groups', name="group_list"),
)


urlpatterns += bridge.include_urls('topics.urls', r'^group/(?P<group_slug>[-\w]+)/topics/')