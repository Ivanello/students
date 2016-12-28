"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from students import views
from .settings import MEDIA_ROOT, DEBUG, MEDIA_URL
from django.conf.urls.static import static


# admin.autodiscover()

urlpatterns = [

    #Students

    url(r'^$', views.students_list, name='home'),
    url(r'^students/add/$', views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', views.students_delete, name='students_delete'),
    
    #Groups

    url(r'^groups/$', views.groups_list, name='groups_list'),
    url(r'^groups/add/$', views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/del/$', views.groups_delete, name='groups_delete'),
    
    #Journal
    
    url(r'^journal/$', views.journal, name='journal'),
    url(r'^journal/update/$', views.journal_update, name='journal_update'),
    url(r'^journal/(?P<sid>\d+)/$', views.journal_personal, name='journal_personal'),

    url(r'^admin/', include(admin.site.urls), name='admin')
] 
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)