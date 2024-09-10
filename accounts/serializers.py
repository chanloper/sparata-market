
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name',
                  'last_name', 'nickname', 'birthday', 'gender', 'bio']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            nickname=validated_data['nickname'],
            birthday=validated_data.get('birthday', None),
            gender=validated_data.get('gender', ''),
            bio=validated_data.get('bio', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
