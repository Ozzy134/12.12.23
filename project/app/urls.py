from django.urls import path
from .views import index, vxod, reg, data

urlpatterns = [
    path('', index, name='home'),
    path('vxod', vxod, name='vxod'),
    path('reg', reg, name='reg'),
    path('data', data, name='data'),
]