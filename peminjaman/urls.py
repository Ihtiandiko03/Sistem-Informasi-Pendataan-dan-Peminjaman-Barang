from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^create/$', views.create, name='create'),
	url(r'^detail/$', views.detail, name='detail'),
	url(r'^pdf_view/$', views.ViewPDF.as_view(), name="pdf_view"),
    url(r'^pdf_download/$', views.DownloadPDF.as_view(), name="pdf_download"),
	url(r'^$', views.list, name='list'),
]