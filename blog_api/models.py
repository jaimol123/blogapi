from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class UserProfiles(AbstractUser):


    class Meta:
        db_table = 'userprofiles'
        verbose_name = "UserProfile"


class Recipe(models.Model):
    recipe_name= models.CharField( max_length=25, null=True, blank=True)
    recipe_image= models.FileField(null=True,blank=True)
    category=models.CharField( max_length= 25, null=True, blank=True )
    type=models.CharField(max_length=30, null=True, blank=True)
    step = RichTextField(null= True)
    pub_date = models.DateField(default=datetime.datetime.now, null=True, blank=True)
    prep_time = models.CharField(max_length=25, null=True, blank=True)
    slug = models.SlugField(null = True, blank = True)

    class Meta:
            db_table="recipe"
            verbose_name= "Recipe"
            ordering=['pub_date']


class Ingredients(models.Model):
    receipe_name=  models.ManyToManyField(Recipe, related_name="food")
    ingredients= models.CharField(max_length=25, default="0")

    class Meta:
        db_table= "ingredients"
        verbose_name_plural="Ingredients"

    def __str__(self):

        return self.receipe_name


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
    text1=RichTextField(null= True, blank=True)
    text2=RichTextField(null= True, blank=True)
    heading=models.CharField(max_length=25, null=True, blank=True)
    image1=models.FileField(null=True, blank=True)
    image2=models.FileField(null=True, blank=True)
    heading2 = models.CharField(max_length = 255, null = True, blank = True)

    class Meta:
        db_table="feature"
        verbose_name="feature"

    def __str__(self):
        return self.heading


class AboutUs(models.Model):
    heading = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name="about", null=True, blank=True)
    text=models.CharField(max_length=25, null=True, blank=True)
    numbers= models.IntegerField(null=True, blank=True)
    image=models.FileField(null=True, blank=True)

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







