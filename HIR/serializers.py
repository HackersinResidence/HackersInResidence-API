from rest_framework import serializers
from django.contrib.auth.models import User



from . import models



class OrganizationSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    residencies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'approved',
            'website',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country',
            'email',
            'phone',
            'about',
            'user',
            'logo',
            'residencies',
            'images',
            'videos'
        )
        model = models.Organization
        read_only_fields = ('user','id','approved',)



class StaffOrganizationSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    videos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    residencies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'approved',
            'website',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country',
            'email',
            'phone',
            'about',
            'user',
            'logo',
            'residencies',
            'images',
            'videos'
        )
        model = models.Organization
        read_only_fields = ('user','id',)




class ResidencySerializer(serializers.ModelSerializer):
    offers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    requires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'approved',
            'organization',
            'title',
            'about',
            'offer_travel_check',
            'offer_travel_detail',
            'offer_housing_check',
            'offer_housing_detail',
            'offer_food_check',
            'offer_food_detail',
            'offer_stipend_check',
            'offer_stipend_detail',
            'offer_studio_check',
            'offer_studio_detail',
            'offer_tools_check',
            'offer_tools_detail',
            'offer_additional_detail',
            'require_language',
            'require_start_date',
            'require_end_date',
            'require_minimum_stay',
            'require_maximum_stay',
            'require_date_detail',
            'require_mentoring_check',
            'require_mentoring_detail',
            'require_talk_check',
            'require_talk_detail',
            'require_workshop_check',
            'require_workshop_detail',
            'require_presentation_check',
            'require_presentation_detail',
            'require_class_check',
            'require_class_detail',
            'require_hackathon_check',
            'require_hackathon_detail',
            'require_other_requirements',
            'offers',
            'requires'
        )
        model = models.Residency
        read_only_fields = ('id', 'organization', 'approved',)


class StaffReSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'approved',
            'organization',
            'title',
            'about'
        )
        model = models.Residency
        read_only_fields = ('id', 'organization')



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'label',
            'summary',
            'notes',
            'residence'
        )
        model = models.Offer
        read_only_fields = ('id',)



class RequiredSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'label',
            'summary',
            'notes',
            'residence'
        )
        model = models.Required
        read_only_fields = ('id',)



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'image',
            'organization'
        )
        model = models.Image
        read_only_fields = ('id', 'organization',)



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'url',
            'organization'
        )
        model = models.Video
        read_only_fields = ('id', 'organization',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'email',
            'is_staff'
        )
        model = User
        read_only_fields = ('id', 'username', 'email', 'is_staff',)