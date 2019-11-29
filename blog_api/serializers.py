from rest_framework import serializers
import datetime
from .models import UserProfiles, Recipe, Slider, SocialLinks, FooterImage, Feature, Contact, Ingredients,AboutUs,Newsletter,Address,Comments, Rating


class UserProfilesSerializers(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length = 255, required = True)
    username = serializers.CharField(max_length = 255, required = True)
    email = serializers.EmailField(max_length = 255, required = True)
    password = serializers.CharField(max_length = 255, required = True)


    def validate_first_name(self,data):

        for i in data:
            if(i.isdigit()):
                raise  serializers.ValidationError('numeric values not allowed')
            return data

    def validate_password(self, data):

        if(len(data)<4):
            raise serializers.ValidationError("password is too short")
        return data

    def validate_email(self,data):

        if('@' not in data):
            raise serializers.ValidationError("invalid email")
        return data




    class Meta:

        model = UserProfiles
        fields = ('first_name','username', 'email','password')

class LoginSerializers(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 255, required=True)
    password = serializers.CharField(max_length = 255, required = True)

    class Meta:

        model = UserProfiles
        fields = ('username', 'password')


class LogoutSerializers(serializers.Serializer):

    user_id = serializers.IntegerField()


class IngredientSerializers(serializers.ModelSerializer):

    ingredients = serializers.CharField()

    class Meta:
        model = Ingredients
        fields = ('ingredients',)


class RecipeSerializers(serializers.ModelSerializer):

    recipe_name = serializers.CharField(max_length = 255, required = True)
    ingredients = IngredientSerializers(many = True)
    category = serializers.CharField(max_length = 255, required = True)
    type = serializers.CharField(max_length = 255, required = True)


    class Meta:

        model = Recipe
        fields ='__all__'


class RecipePostSerializers(serializers.Serializer):

     recipe_name = serializers.CharField(required = False, allow_null = True,  default = "0")
     category = serializers.CharField(required = False, allow_null = True, default = "0" )
     type = serializers.CharField(required = False, allow_null = True, default = "0")





class SliderSerializers(serializers.ModelSerializer):

    slider_image = serializers.FileField()
    slider_caption1 = serializers.CharField(max_length = 255, required = True)
    slider_caption2 = serializers.CharField(max_length = 255, required = True)
    slider_caption3 = serializers.CharField(max_length = 255, required = True)

    class Meta:

        model = Slider
        fields = ('slider_image', 'slider_caption1', 'slider_caption2', 'slider_caption3')


class SocialLinksSerializers(serializers.ModelSerializer):

    icon_name = serializers.CharField(max_length = 255, required = True)
    social_url = serializers.URLField(required = True)

    class Meta:

        model = SocialLinks
        fields = ('icon_name', 'social_url')


class FooterImageSerializers(serializers.ModelSerializer):

    image = serializers.FileField()

    class Meta:

        model = FooterImage
        fields = ('image', )


class FeatureSerializers(serializers.ModelSerializer):

    text1 = serializers.CharField(max_length = 255, required = True)
    text2 = serializers.CharField(max_length = 255, required = True)
    heading = serializers.CharField(max_length = True, required = True)
    heading2 = serializers.CharField(max_length = 255, required = True)
    image1 = serializers.FileField(required = True)
    image2 = serializers.FileField(required = True)

    class Meta:

        model = Feature
        fields = ('text1', 'text2', 'heading', 'heading2', 'image1', 'image2')


class AboutUsSerializers(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):

    contact_name = serializers.CharField(max_length = 255, required = True)
    contact_subject = serializers.CharField(max_length = 255, required = True)
    contact_message = serializers.CharField(max_length = 255, required = True)
    contact_email = serializers.EmailField(required = True)



    class Meta:

        model = Contact
        fields = ('contact_name','contact_subject', 'contact_message', 'contact_email')



class NewsletterSerializers(serializers.ModelSerializer):

    mail = serializers.EmailField(required = True)

    def validate_mail(self, data):
        if('@' not in data):
            raise serializers.ValidationError('invalid mail')
        return data

    class Meta:
        model = Newsletter
        fields = '__all__'

class AddressSerializers(serializers.ModelSerializer):

    Address = serializers.CharField(max_length=255, required=True)
    phone_number = serializers.CharField(max_length = 255, required = True)
    email = serializers.EmailField(required = True)
    heading1 = serializers.CharField(max_length = 255, required = True)
    heading2 = serializers.CharField(max_length = 255, required = True)
    heading3 = serializers.CharField(max_length = 255, required = True)

    class Meta:
        model = Address
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):

    subject = serializers.CharField(max_length = 255, required = True)
    msg = serializers.CharField(max_length = 255, required = True)
    receipe_name_id = serializers.IntegerField( required = True)

    class Meta:

        model = Comments
        fields = "__all__"



class CommentlistSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name  = serializers.CharField()
    subject = serializers.CharField(max_length = 255, required = True)
    msg = serializers.CharField(max_length = 255, required = True)
    receipe_name = RecipeSerializers()

    class Meta:
        model = Comments
        fields = "__all__"


class CommentUpdateSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()
    name = serializers.CharField(required = True)
    subject = serializers.CharField(required = True)
    msg = serializers.CharField(required = True)
    receipe_name = serializers.CharField(required = True)

    class Meta:
        model = Comments
        fields = "__all__"


class RatingSerializers(serializers.ModelSerializer):

    rate = serializers.IntegerField(required = True)
    recipe_name = serializers.CharField(required = True, max_length = 255)

    class Meta:
        model = Rating
        fields =('rate', 'recipe_name')


class RatingListSerializers(serializers.Serializer):

    recipename = serializers.CharField()
    rate = serializers.IntegerField()
    avg = serializers.IntegerField()


class SocialLoginSerializer(serializers.Serializer):

    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)
























