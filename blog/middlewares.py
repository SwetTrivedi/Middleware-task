from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import Userinfo
from django.urls import resolve
class TrackUserLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR') 
        url_path=request.path
        if resolve(url_path):
            view_name=resolve(url_path).func.__name__
        else :
            "Unkown view"
        if request.user.is_authenticated:
            user= request.user
            login_record= Userinfo.objects.filter(user=user).first()
            if not login_record:
                login_record = Userinfo.objects.create(user=user, clientcount=1)
            else:
                login_record.clientcount += 1   
            login_record.clientip = user_ip
            login_record.clienttime = now()
            login_record.clientname = user.get_username()
            login_record.clienturl=request.path
            login_record.clientview=view_name
            login_record.save()
                    

        else:
            login_record = Userinfo.objects.filter(user=None).first()

            if not login_record:  
                login_record = Userinfo.objects.create(
                    user=None,
                    clientip=user_ip,
                    clientname="Anonymous",
                    clientcount=1
                )
            else:
                login_record.clientcount += 1 
            login_record.clientip = user_ip
            login_record.clienttime = now()
            login_record.clienturl = request.path
            login_record.clientview=view_name
            login_record.save()

        response = self.get_response(request)
        return response




