
from django.conf.urls import url,include
from django.contrib import admin

from . import views
from .views import index, loginView, logoutView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', loginView, name='login'),
	url(r'^logout/$', logoutView, name='logout'),
	url(r'^barang/', include('barang.urls', namespace='barang')),
	url(r'^staff/', include('staff.urls', namespace='staff')),
	url(r'^ruang/', include('ruang.urls', namespace='ruang')),
	url(r'^gedung/', include('gedung.urls', namespace='gedung')),
	url(r'^peminjaman/', include('peminjaman.urls', namespace='peminjaman')),
    url(r'^admin/', admin.site.urls),
]
