from rest_framework.serializers import ModelSerializer, ValidationError


from authenticate.models import User


class UserSerialiser(ModelSerializer):
    # method creat et setpassword

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
                "Pour créer un compte il faut avoir plus de 15 ans")
        return data
