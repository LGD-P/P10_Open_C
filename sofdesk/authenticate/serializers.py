from rest_framework.serializers import ModelSerializer, ValidationError


from authenticate.models import User


class UserSerialiser(ModelSerializer):

    error_msg = "Les utilisateurs doivent avoir plus de 15ans pour créer un compte."

    class Meta:
        model = User
        fields = ['user_id', 'username', 'age',
                  'can_be_shared', 'can_be_contacted', 'password']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['age'] <= 15:
            raise ValidationError(
                self.error_msg)
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
