from rest_framework import serializers
from .models import UserProfiles, Recipe,Slider
from django.contrib.auth.hashers import make_password



class UserProfilesSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 255)
    username = serializers.CharField(max_length = 255)
    email = serializers.EmailField(max_length =255)
    password = serializers.CharField(max_length =255)

    def create(self, validated_data):
        user = UserProfiles.objects.create(
            first_name=validated_data['first_name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )



    def validate_password(self, data):
        if(len(data)<4):
            raise serializers.ValidationError("password is too short")
        return data

    def validate_email(self,data):
        if('@' not in data):
            raise serializers.ValidationError("invalid email")

    def validate_first_name(self,data):
        for i in data:
            if(i.isdigit()):
                raise  serializers.ValidationError('numeric values not allowed')


    class Meta:
        model = UserProfiles
        fields = ('first_name', 'username', 'email','password')

class LoginSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 255)
    password = serializers.CharField(max_length = 255)





