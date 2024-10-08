from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access_token', path='/apartments/', secure=True, httponly=True, samesite='Lax')
        response.delete_cookie('refresh_token', path='/apartments/', secure=True, httponly=True, samesite='Lax')
        return response
