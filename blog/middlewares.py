# from django.shortcuts import HttpResponse
from .models import Userinfo
from . forms import Signupform,Loginform,Postform
class Trackip:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        ip=request.META.get("REMOTE_ADDR")
        print("Client ip :",ip)
        print(request)
        response=self.get_response(request)            
        return response


class LogUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print(f"Client Name: {request.user.username}") 
        else:
            print("Anonyms User")
        response = self.get_response(request)
        return response


