"""kkm_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

# When debug option is enabled(DEBUG=True), DO NOT forget to add urlpatterns as shown below:
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('diners/', include('diners.urls')),
    path('', include('single_pages.urls')),
    # dashboard에 들어갈 항목&링크 목록을 표시
    path('foodies_list/', include('foodies_list.urls')),
    # dashboard 본체
    
    #summernote extension
    path('summernote/', include('django_summernote.urls')),

    #all-auth path
    path('accounts/', include('allauth.urls')),
    #django-markdownx path
    path('markdownx/', include('markdownx.urls')),


]
# summernote: When debug option is enabled(DEBUG=True), DO NOT forget to add urlpatterns as shown below:
## gunicorn 사용시 설정 필요
# django와 nginx 연동(on ubuntu linux) 7
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


