from xml.etree.ElementInclude import include
from django.conf.urls import url
from django.urls import URLPattern,path
from ZSSN_Survival import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('survivors',views.SurvivorView, basename='survivors')
router.register('survivor/reports', views.SurvivorPercentage, basename='repo')


urlpatterns = router.urls