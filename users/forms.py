from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleand_data.get('email')
        domain = email.split("@")[1]
        print(domain)
        if domain != "kookmin.ac.kr":
            raise ValidationError("This domain is not valid")
        return email