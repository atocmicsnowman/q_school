import json
import logging

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render 
from django.views import View
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

import pandas as pd

from q_school.geography.models import Region
from q_school.registration.models import Pax, User
from q_school.registration.utils import validate_users_upload_formatted


logger = logging.getLogger(__name__)

class UsersView(View):
    template = 'user_management.html'

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
        return HttpResponse(status=204)


class PaxView(View):
    pax_template = "single_pax_manager.html"

    def get(self, request, user_id):
        pax = Pax.objects.get(user_id=user_id)
        return render(request, self.pax_template, {"pax": pax})


class UserView(View):
    def get(self, request):
        pax_list = Pax.objects.all().values('id', 'f3_handle', 'user__last_name', 'user__first_name', 'user__username')
        return JsonResponse({"pax_list": list(pax_list)})


class UserUploadView(View):

    def post(self, request, region_id):
        """
        File size is not going to be big enough for pandas (fewer than 4k 
        entries), so it isn't exactly a mortal sin to read it twice. and not
        have the complication of having to deal with pandas' dependency hell...
        
        hopefully
        """
        csv_file = request.FILES['attachment']
        new_pax = []
        df = pd.read_csv(csv_file)
        
        print(f"rows {len(df.index)}")
        # we will not process anything with a duplicate email address, the 
        # submitter can fix and resubmit
        dupe_emails = df[df['email'].duplicated()==True]['email']
        
        dupe_rows = df[df['email'].isin(dupe_emails)]
        dupe_rows = dupe_rows[['email', 'f3_handle']]
        flat_list = dupe_rows.values.flatten().tolist()
        dupe_rows_list = list(set(zip(flat_list[::2], flat_list[1::2])))
        existing_users = {u[0] for u in User.objects.filter(username__in=df.email.to_list()).values_list('username')}
        print(f"{existing_users=}")
        df.drop(df.loc[df['email'].isin(dupe_emails)].index, inplace=True)
        print(f"{len(df.index)=}")
        df.drop(df.loc[df['email'].isin(existing_users)].index, inplace=True)
        print(f"{len(df.index)=}")
        df['phone_number'] = df['phone_number'].apply(str)
        df.reset_index(inplace=True)
        related_region = Region.objects.get(pk=region_id)
        new_users = [
            User(
                username=user['email'],
                email=user['email'],
                first_name=user['first_name'],
                last_name=user['last_name'],
                is_active=False,
                is_staff=False
            ) for index, user in df.iterrows()
        ]
        created_users = User.objects.bulk_create(new_users)
        pax_list = [
            Pax(
                user_id=created_users[index].id,
                f3_handle=user['f3_handle'],
                cell_number=user['phone_number'],
                email=user['email'],
                sms_subscribed=False,
                sms_notifications=False,
                email_notifications=False,
            ) for index, user in df.iterrows()
        ]
        new_pax = Pax.objects.bulk_create(pax_list)
        related_region.members.add(*new_pax)
        return JsonResponse({
            "existing_users": list(existing_users), 
            "duplicates": dupe_rows.to_html(classes="table"),
            "new_users": len(new_pax)
            })


class UsersUploadView(View):
    def post(self, request):
        files = request.FILES
        print(f"\n\n{files}\nCOMMIT ******************")
        return JsonResponse({"yay": "yay"})