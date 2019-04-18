from . import views

try:
    # Djando 2.x系
    from django.urls import path, include

    urlpatterns = [
        path('', views.post_list, name='post_list'),
        path('post/new/', views.post_new, name='post_new'),
    ]

except ImportError:
    # Djando 1.11.x系
    from django.conf.urls import include, url

    urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        url(r'^post/new/$', views.post_new, name='post_new'),
    ]

