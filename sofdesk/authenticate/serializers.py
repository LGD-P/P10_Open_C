from rest_framework.serializers import ModelSerializer


from authenticate.models import User


class UserSerialiser(ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'age',
                  'can_be_shared', 'can_be_contacted']
