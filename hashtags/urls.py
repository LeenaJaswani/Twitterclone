from django.conf.urls import url
from django.views.generic.base import RedirectView
from . views import HashTagView


urlpatterns = [
    
 url(r'^tags/(?P<hashtag>.*)/$',HashTagView.as_view(),name='hashtag'),
    
     
]
