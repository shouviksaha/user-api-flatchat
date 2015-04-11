from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework import routers
from api.views import UserDetail,UserList,AuthView,logoutView,UserSignup

from django.conf import settings
from django.conf.urls.static import static

#router = routers.DefaultRouter()
#router.register(r'user', UserView, 'list')


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login/$',AuthView.as_view()),
    url(r'^user/logout/$',logoutView),
    url(r'^user/signup/$',UserSignup.as_view()),
    url(r'^user/$', UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
 #   url(r'^', include(router.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)