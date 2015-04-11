from django.contrib.auth.models import User
from rest_framework import serializers
import pdb
 
def email_validator(data):
    users = User.objects.filter(email=data)
    if(len(users) > 0):
        raise serializers.ValidationError("Email already exists")

def length_validator(data):
    if(len(data) < 8):
        raise serializers.ValidationError("Too short")



class UserListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [email_validator])
    username = serializers.CharField(validators = [length_validator])
    password = serializers.CharField(validators = [length_validator],write_only=True)
    class Meta:
        model = User
        fields = ('id','username','password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)

 
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password', instance.password))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
