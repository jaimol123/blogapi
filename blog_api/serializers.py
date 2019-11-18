from rest_framework import serializers
from .models import UserProfiles, Recipe,Slider

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

class RecipeSerializers(serializers.ModelSerializer):
    recipe_name = serializers.CharField(max_length = 255, required = True)
    recipe_image = serializers.FileField(max_length = 255, required = True)
    category = serializers.CharField(max_length = 255, required = True)
    type = serializers.CharField(max_length = 255, required = True)








