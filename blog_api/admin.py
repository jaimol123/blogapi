from django.contrib import admin
from . models import UserProfiles,Recipe,Ingredients,Feature,FooterImage,SocialLinks,Slider,AboutUs, Address, Newsletter, Rating,Contact,Comments


class UserProfilesAdmin(admin.ModelAdmin):

    list_display = ['password' , 'username' , 'first_name' , 'email']
    search_fields = ['username']


class RecipeAdmin(admin.ModelAdmin):

        list_display = ('recipe_name', 'category', 'type', 'recipe_image')
        search_fields = ['recipe_name']
        list_filter = ['pub_date']
        prepopulated_fields = {'slug': ('recipe_name',)}



class SliderAdmin(admin.ModelAdmin):

    search_display = ['slider_caption1', 'slider_caption2', 'slider_caption3']
    list_editable = ( 'slider_caption1', 'slider_caption2', 'slider_caption3' )
    list_display= ('slider_image','slider_caption1', 'slider_caption2', 'slider_caption3')


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'social_url')


class AboutUsAdmin(admin.TabularInline):

    model = AboutUs
    extra = 3


class FeatureAdmin(admin.ModelAdmin):

    fields = ('text1', 'text2','heading','image1', 'image2')
    inlines = [AboutUsAdmin]


class FooterAdmin(admin.ModelAdmin):

    list_display = ('image',)


class AddressAdmin(admin.ModelAdmin):

   list_display = ('address', 'phone_number', 'heading1', 'heading2', 'heading3')


class CommentsAdmin(admin.ModelAdmin):

    list_display = ('receipe_name', 'name', 'subject', 'msg', 'date')


class ContactAdmin(admin.ModelAdmin):

    list_display = ('contact_name', 'contact_subject', 'contact_msg', 'contact_email')


class RatingAdmin(admin.ModelAdmin):

    list_display =('rate', 'avg', 'total' , 'recipename', 'name')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Ingredients, admin.ModelAdmin)
admin.site.register(FooterImage, FooterAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(SocialLinks, SocialLinkAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfiles,UserProfilesAdmin)
