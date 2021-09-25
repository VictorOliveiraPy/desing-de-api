from django.urls import include, path

urlpatterns = [
    #path('', include('apps.core.urls')),
    path('', include('apps.level1.urls'))
]
