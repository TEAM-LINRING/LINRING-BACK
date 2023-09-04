from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from .models import User

# Create your views here.
@api_view(['DELETE'])
def userDelete(request, id):
    try:
        uid = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if request.user.is_staff:
            pass
        elif request.user.id == id:
            logout(request)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        uid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConfirmEmailView(APIView):
    permission_classes = [AllowAny] # 전체 권한

    def get(self, *args, **kwargs):
        self.object = confirmation = self.get_object()
        confirmation.confirm(self.request)
        # 실패 시나리오에 따라 Vue 라우터를 이용하여 핸들링 예정
        return HttpResponseRedirect('/')
    
    def get_object(self, queryset=None):
        key = self.kwargs['key']
        email_confirmation = EmailConfirmationHMAC.from_key(key)
        if not email_confirmation:
            if queryset is None:
                queryset = self.get_queryset()
            try:
                email_confirmation = queryset.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                # 실패 시나리오에 따라 Vue 라우터를 이용하여 핸들링 예정
                return HttpResponseRedirect('/')
        return email_confirmation

    def get_queryset(self):
        qs = EmailConfirmation.objects.all_valid()
        qs = qs.select_related("email_address__user")
        return qs