
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'containers/', include('containers.urls')),
    url(r'^admin/', admin.site.urls),
]
