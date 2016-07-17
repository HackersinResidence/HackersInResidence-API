from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import models
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .permissions import IsOwnerOrStaffOrReadOnly, IsOwnerOfOrganizationOrStaffOrReadOnly, IsOwnerOfRecidencyOrStaffOrReadOnly
from . import serializers
# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Organizations.
        """
    queryset = models.Organization.objects.filter(approved=True)
    serializer_class = serializers.OrganizationSerializer
    permission_classes = (IsOwnerOrStaffOrReadOnly,)


    @detail_route(methods=['get'])
    def residencies(self, request, pk=None):
        """
            API endpoint that allows
            anons: viewed
            users: viewed
            admins: viewed
            Residencies of the Organization.
            """
        residencies = models.Residency.objects.filter(organization_id=pk)

        page = self.paginate_queryset(residencies)

        if page is not None:
            serializer = serializers.ResidencySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ResidencySerializer(residencies, many=True)
        return Response(serializer.data)


    @detail_route(methods=['get'])
    def videos(self, request, pk=None):
        """
            API endpoint that allows
            anons: viewed
            users: viewed
            admins: viewed
            Videos of the Organization.
            """
        videos = models.Video.objects.filter(organization_id=pk)

        page = self.paginate_queryset(videos)

        if page is not None:
            serializer = serializers.VideoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.VideoSerializer(videos, many=True)
        return Response(serializer.data)\


    @detail_route(methods=['get'])
    def images(self, request, pk=None):
        """
            API endpoint that allows
            anons: viewed
            users: viewed
            admins: viewed
            Images of the Organization.
            """
        images = models.Image.objects.filter(organization_id=pk)

        page = self.paginate_queryset(images)

        if page is not None:
            serializer = serializers.ImageSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ImageSerializer(images, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class StaffOrganizationViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: none
        users: none
        admins: approved or edited
        Organizations.
        """
    queryset = models.Organization.objects.all()
    serializer_class = serializers.StaffOrganizationSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ResidencyViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Residencies.
        """
    queryset = models.Residency.objects.filter(approved=True)
    serializer_class = serializers.ResidencySerializer
    permission_classes = (IsOwnerOfOrganizationOrStaffOrReadOnly,)

    @detail_route(methods=['get'])
    def requires(self, request, pk=None):
        """
            API endpoint that allows
            anons: viewed
            users: viewed
            admins: viewed
            Requires of the Residency.
            """
        requires = models.Required.objects.filter(residence_id=pk)

        page = self.paginate_queryset(requires)

        if page is not None:
            serializer = serializers.RequiredSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.RequiredSerializer(requires, many=True)
        return Response(serializer.data)


    @detail_route(methods=['get'])
    def offer(self, request, pk=None):
        """
            API endpoint that allows
            anons: viewed
            users: viewed
            admins: viewed
            Offers of the Residency.
            """
        offers = models.Offer.objects.filter(residence_id=pk)

        page = self.paginate_queryset(offers)

        if page is not None:
            serializer = serializers.OfferSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.OfferSerializer(offers, many=True)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(organization = models.Organization.objects.get(user= self.request.user))



class StaffReViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: none
        users: none
        admins: approved or edited
        Residencies.
        """
    queryset = models.Residency.objects.all()
    serializer_class = serializers.StaffReSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(organization = models.Organization.objects.get(user= self.request.user))



class OfferViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Offers.
        """
    queryset = models.Offer.objects.all()
    serializer_class = serializers.OfferSerializer
    permission_classes = (IsOwnerOfRecidencyOrStaffOrReadOnly,)



class RequiredViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Requires.
        """
    queryset = models.Required.objects.all()
    serializer_class = serializers.RequiredSerializer
    permission_classes = (IsOwnerOfRecidencyOrStaffOrReadOnly,)



class ImageViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Images.
        """
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = (IsOwnerOfOrganizationOrStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(organization=models.Organization.objects.get(user=self.request.user))


class VideoViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows
        anons: viewed
        users: created or edited
        admins: created or edited
        Videos.
        """
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer
    permission_classes = (IsOwnerOfOrganizationOrStaffOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(organization=models.Organization.objects.get(user=self.request.user))


class UserProfile(generics.RetrieveAPIView):
    """
        API endpoint that allows
        anons: none
        users: viewed
        admins: viewed
        User profile.
        """
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
