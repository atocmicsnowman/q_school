import logging
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render 
from django.views.generic import TemplateView
from django.views import View


from q_school.registration.models import Pax, User


logger = logging.getLogger(__name__)

class CoreView(View):
    template = 'registration_users_new.html'

    def get(self, request):
        users = Pax.objects.all()
        return render(request, self.template, {'users': users})

    def post(self, request):
        request_json = json.loads(request.body)
        new_user, created = User.objects.get_or_create(
            username=request_json['email'],
            email=request_json['email'],
        )
        if not created:
            return JsonResponse({"error": f"Pax with email {request_json['email']} already exists"}, status=409)
        new_user.first_name = request_json['first_name']
        new_user.last_name = request_json['last_name']
        new_user.is_active = True
        new_user.is_staff = False
        new_user.save()

        pax, pax_created = Pax.objects.get_or_create(
            user=new_user,
            cell_number=request_json['phone'],
            email=request_json['email'],
            email_subscribed=True,
            email_notifications=True,
            sms_subscribed=True,
            sms_notifications=True,
            f3_handle=request_json['f3_handle']
        )


class UserView(View):
    def get(self, request):
        pax_list = Pax.objects.all().values('id', 'f3_handle', 'user__last_name', 'user__first_name', 'user__username')
        return JsonResponse({"pax_list": list(pax_list)})
