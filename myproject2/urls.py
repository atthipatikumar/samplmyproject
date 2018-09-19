from django.conf.urls import patterns, url, include
from django.conf.urls import *
from tastypie.api import *
from myproject2.api.seconduser import FirstpageResource, SecondpageResource
from myproject2.Views import main
#admin.autodiscover()


v2_api = Api(api_name='v2')
v2_api.register(FirstpageResource())
v2_api.register(SecondpageResource())

urlpatterns = patterns('',

                        #url(r'^admin/', include(admin.site.urls)),
                        (r'', include(v2_api.urls)),
                        url(r'^regist/$', main.register22),
                        (r'', include((v2_api.urls))),
                        url(r'^ord/$', main.order24),
                       )
