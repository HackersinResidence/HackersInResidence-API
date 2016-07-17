"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from HIR import views as hir

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'organization', hir.OrganizationViewSet)
router.register(r'residence', hir.ResidencyViewSet)
router.register(r'offer', hir.OfferViewSet)
router.register(r'required', hir.RequiredViewSet)
router.register(r'image', hir.ImageViewSet)
router.register(r'video', hir.VideoViewSet)
router.register(r'residence-staff', hir.StaffReViewSet)
router.register(r'organization-staff', hir.StaffOrganizationViewSet)



urlpatterns = [
    # Examples:
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/profile', hir.UserProfile.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]