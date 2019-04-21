"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

try:
    # Djando 2.x系
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
    ]

    # DEBUG=Falseの時のデバッグ手段
    # http://d.hatena.ne.jp/karasuyamatengu/20100521/1274399876
    # 組み込みの500エラーハンドラーを自前のにすり替える。
    # urls.pyでやるのがいいだろう。
    # 参照： http://docs.djangoproject.com/en/dev/topics/http/views/
    from . import exception_logger
    from django.urls import *
    handler500=exception_logger.server_error

except ImportError:
    # Djando 1.11.x系
    from django.conf.urls import include, url

    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
    ]

