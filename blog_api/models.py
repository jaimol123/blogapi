from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from phone_field import PhoneField

class UserProfiles(AbstractUser):

    # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    # def create_auth_token(sender, instance=None, created = False, **kwargs):
    #     if created:
    #         Token.objects.create(user = instance)


    class Meta:
        db_table = 'userprofiles'
        verbose_name = "UserProfile"


class Ingredients(models.Model):

    ingredients = models.CharField(max_length=25, default="0")

    def __str__(self):
        return self.ingredients

    class Meta:
        db_table= "ingredients"
        verbose_name_plural="Ingredients"


class Recipe(models.Model):

    recipe_name = models.CharField( max_length=25, null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredients, max_length=25, default="0")
    recipe_image = models.FileField(null=True,blank=True)
    category = models.CharField( max_length= 25, null=True, blank=True )
    type = models.CharField(max_length=30, null=True, blank=True)
    step = RichTextField(null= True)
    pub_date = models.DateField(auto_now_add = True,  null=True, blank=True)
    prep_time = models.CharField(max_length=25, null=True, blank=True)
    slug = models.SlugField(null = True, blank = True)

    def __str__(self):
        return self.recipe_name

    class Meta:
            db_table="recipe"
            verbose_name= "Recipe"
            ordering=['pub_date']



class Slider(models.Model):
    slider_image = models.FileField(blank=True, null=True)
    slider_caption1 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption2 = models.CharField(max_length=100, null=True, blank=True)
    slider_caption3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "slider"
        verbose_name= "Slider"


class SocialLinks(models.Model):
    icon_name = models.CharField(max_length=30, null=True, blank=True)
    social_url = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        db_table= "social_links"
        verbose_name_plural= "Social Links"


class FooterImage(models.Model):

    image= models.FileField(null=True, blank=True)

    class Meta:
        db_table="footerimage"
        verbose_name_plural="FooterImage"


class Feature(models.Model):

    text1 = RichTextField(null= True, blank=True)
    text2 = RichTextField(null= True, blank=True)
    heading = models.CharField(max_length=25, null=True, blank=True)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    heading2 = models.CharField(max_length = 255, null = True, blank = True)

    class Meta:
        db_table="feature"
        verbose_name="feature"

    def __str__(self):
        return self.heading


class AboutUs(models.Model):

    heading = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="about", null=True, blank=True)
    text = models.CharField(max_length=25, null=True, blank=True)
    numbers = models.IntegerField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)

    class Meta:
        db_table="aboutus"
        verbose_name_plural = 'AboutUs'


class Contact(models.Model):

    contact_name = models.CharField(max_length=25, null=True, blank=True)
    contact_subject = models.CharField(max_length=25, null=True, blank=True)
    contact_msg = models.TextField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(max_length=255, null=True,blank=True)

    class Meta:
        db_table="contact"
        verbose_name="contact"


class Comments(models.Model):

    receipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comment_recipename", null=True, blank=True)
    name= models.CharField(max_length= 25, null=True, blank=True)
    subject= models.CharField(max_length= 25, null=True, blank=True)
    msg= models.TextField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True , blank = True, null = True)



    class Meta:
        db_table= "comments"
        verbose_name_plural="Comments"


class Address(models.Model):

    address = models.CharField(max_length=255, null=True,blank=True)
    phone_number = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField( null=True,blank=True)
    heading1 = models.CharField(max_length=255, null=True,blank=True)
    heading2 = models.CharField(max_length=255, null=True,blank=True)
    heading3 = models.CharField(max_length=255, null=True,blank=True)

    class Meta:
        db_table = "details"
        verbose_name = "Detail"


class Newsletter(models.Model):
    heading = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="news", null=True, blank=True)
    mail = models.EmailField(blank= True, null = True)

    class Meta:
        db_table="newsletter"
        verbose_name_plural = 'Newsletter'


class Rating(models.Model):

    name = models.CharField(max_length = 255, blank = True, null = True)
    rate = models.IntegerField(blank=True, null=True)
    avg = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    recipename = models.CharField(max_length = 255, null=True, blank=True)
  

    class Meta:
        db_table = "rating"
        verbose_name_plural = "Rating"











