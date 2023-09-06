from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('id', 'password', 'is_superuser', 'is_staff', 'is_active', 'email')

    def validate_email(self, email):
        domain = email.split("@")[1]
        if domain != "kookmin.ac.kr":
            print("debug1")
            raise serializers.ValidationError("This domain is not valid. Allow domain is [kookmin.ac.kr]")
        return email