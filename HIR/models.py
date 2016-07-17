from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

from uuslug import uuslug
from . import countries

# Create your models here.

def organization_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/organization_<id>/<filename>
    return 'organization_{0}/{1}'.format(instance.id, filename)


class Offer(models.Model):
    """What things can be offered to a resident?"""
    slug = models.CharField(max_length=80, blank=True, null=True,
                help_text="What is being offered. as a slug Ex 'Travel expenses' becomes travel_expenses'")
    label = models.CharField(max_length=80, blank=True, null=True,
                help_text="What is being offered. Readable prompt Ex 'Travel Expenses'")
    summary = models.CharField(max_length=80, blank=True, null=True,
                help_text="One line summary of what is being offered")
    notes = models.TextField(blank=True, null=True,
                help_text="Full description of what is being offered")
    residence = models.ForeignKey("Residency", related_name="offers")

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.label, instance=self)
        super(Offer, self).save(*args, **kwargs)



class Required(models.Model):
    """What can be required from a resident?"""
    slug = models.CharField(max_length=80, blank=True, null=True,
                help_text="What is required as a slug Ex 'Give a Talk(s)' becomes 'give_a_talk' ")
    label = models.CharField(max_length=80, blank=True, null=True,
                help_text="What is required. Readable prompt Ex 'Give a Talk(s)'")
    summary = models.CharField(max_length=80, blank=True, null=True,
                help_text="One line summary of what is required")
    notes = models.TextField(blank=True, null=True,
                help_text="Full description of what is required")
    residence = models.ForeignKey("Residency", related_name="requires")

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.label, instance=self)
        super(Required, self).save(*args, **kwargs)



class Organization(models.Model):
    name = models.CharField(max_length=200, help_text="The name of your organization",editable=True)
    approved = models.BooleanField(default=False)
    website = models.CharField(max_length=100, blank=True, null=True,help_text="")
    street_address = models.CharField(max_length=200, blank=True, null=True,help_text="")
    city = models.CharField(max_length=30, blank=True, null=True,help_text="")
    state = models.CharField(max_length=30, blank=True, null=True,help_text="Where applicable")
    postal_code = models.CharField(max_length=30, blank=True, null=True,help_text="Where applicable")
    country = models.CharField(max_length=2, choices=countries.COUNTRIES, default='ZZ')
    email = models.CharField(max_length=30,help_text="A contact email for Residency issues")
    phone = models.CharField(max_length=30, blank=True, null=True,help_text="optional")
    about = models.TextField(blank=True, null=True,help_text="Tell us about your fine space!")
    user = models.OneToOneField(User, related_name="organizations")
    logo = models.ImageField(upload_to=organization_directory_path, null=True, blank=True, default=None)
    slug = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Organization, self).save(*args, **kwargs)

    #def get_absolute_url(self):
     #   return reverse('nacion:detail', kwargs={
     #       'slug': self.slug
     #   })



class Residency(models.Model):
    organization = models.ForeignKey("Organization", related_name='residencies')
    title = models.CharField(max_length=120)
    about = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    application_instructions = models.TextField(blank=True, null=True)

    offer_travel_check = models.BooleanField(default=None)
    offer_travel_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_housing_check = models.BooleanField(default=None)
    offer_housing_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_food_check = models.BooleanField(default=None)
    offer_food_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_stipend_check = models.BooleanField(default=None)
    offer_stipend_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_studio_check = models.BooleanField(default=None)
    offer_studio_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_tools_check = models.BooleanField(default=None)
    offer_tools_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_additional_detail = models.TextField(blank=True, null=True)

    require_language = models.CharField(max_length=120, blank=True, null=True)

    require_start_date = models.DateField(blank=True, null=True, help_text="Earliest date the residency can start")
    require_end_date   = models.DateField(blank=True, null=True, help_text="Latest date the residency can end")
    require_minimum_stay = models.CharField(max_length=120, blank=True, null=True, help_text="Minimum required length of stay")
    require_maximum_stay = models.CharField(max_length=120, blank=True, null=True, help_text="Maximum required length of stay")
    require_date_detail = models.TextField(blank=True, null=True)

    require_mentoring_check  = models.BooleanField(default=None)
    require_mentoring_detail =models.CharField(max_length=120, blank=True, null=True)

    require_talk_check  = models.BooleanField(default=None)
    require_talk_detail =models.CharField(max_length=120, blank=True, null=True)

    require_workshop_check  = models.BooleanField(default=None)
    require_workshop_detail =models.CharField(max_length=120, blank=True, null=True)

    require_presentation_check  = models.BooleanField(default=None)
    require_presentation_detail =models.CharField(max_length=120, blank=True, null=True)

    require_class_check  = models.BooleanField(default=None)
    require_class_detail =models.CharField(max_length=120, blank=True, null=True)

    require_hackathon_check  = models.BooleanField(default=None)
    require_hackathon_detail =models.CharField(max_length=120, blank=True, null=True)

    require_other_requirements = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Residency, self).save(*args, **kwargs)



class Video(models.Model):
    url = models.URLField()
    organization = models.ForeignKey("Organization", related_name="videos")



class Image(models.Model):
    image = models.ImageField(upload_to=organization_directory_path)
    organization = models.ForeignKey("Organization", related_name="images")
