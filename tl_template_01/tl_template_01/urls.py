"""interview_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from wp_site import views
from wp_site.models import WpPosts, Tag

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('home/', views.main),
    path('人工智能/', views.category),
    path('区块链/', views.category),
    path('大数据/', views.category),

    path('tag/', views.tag),
]


from wp_site import excel2db
urlpatterns += [
    path('excel2db', excel2db.transfer),

]




for i in WpPosts.category:
    urlpatterns.append(path(i[1], views.category))
    urlpatterns.append(re_path(i[1] + '/(?P<aid>\d+)\.html', views.article))
    urlpatterns.append(re_path(i[1] + '/(?P<page>\d+)', views.article))

tag_rows = Tag.objects.all()
for row in tag_rows:
    #print(row.tag_name)
    urlpatterns.append(path(row.tag_name, views.category))


#for i in Tag.tag_name:
#    urlpatterns.append(path(i[1], views.category))



