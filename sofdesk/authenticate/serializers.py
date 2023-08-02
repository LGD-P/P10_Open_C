
from authenticate.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from datetime import datetime


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'})
    password2 = serializers.CharField(
        write_only=True, style={'input_type': 'password'})
    date_of_birth = serializers.DateField(write_only=True,)

    class Meta:

        model = User

        fields = ['user_id', 'username', 'can_be_shared',
                  'can_be_contacted', 'password', 'password2', 'date_of_birth']

        extra_kwargs = {

            'password': {'write_only': True},
            'date_of_birth': {'write_only': True},

        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data['password'] != data.pop('password2'):
            raise serializers.ValidationError(
                "Les mots de passes ne sont pas identiques")

        return data

    def validate_date_of_birth(self, value):
        """
        Check that the user is at least 15 years old
        """
        today = datetime.now()
        age = today.year - value.year - \
            ((today.month, today.day) < (value.month, value.day))
        if age < 15:
            raise serializers.ValidationError(
                "L'utilisateur doit avoir au moins 15ans pour créer un compte.")
        return value

    def create(self, validated_data):
        """Remove date_of_birth from validated_date 
        before user_creation
        """
        password = validated_data.pop('password')
        test_date = validated_data.pop('date_of_birth', None)
        user = User.objects.create(**validated_data)
        user.set_password(password)
        if test_date:
            user.date_of_birth = test_date
        user.save()
        return user
