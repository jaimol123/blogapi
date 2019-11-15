from django.contrib import admin
from . models import UserProfiles,Recipe,Ingredients,Feature,FooterImage,SocialLinks,Slider,AboutUs


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

admin.site.register(Ingredients, admin.ModelAdmin)
admin.site.register(FooterImage, FooterAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(SocialLinks, SocialLinkAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfiles,UserProfilesAdmin)
