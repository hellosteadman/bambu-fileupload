from django.conf.urls import url
from bambu_fileupload.views import upload, delete, filelist

urlpatterns = (
    url(r'^$', upload, name = 'fileupload'),
    url(r'^delete/$', delete, name = 'fileupload_delete'),
    url(r'^list/$', filelist, name = 'fileupload_list')
)
