import logging
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render 
from django.views.generic import TemplateView
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

from django_countries import countries

from q_school.geography.models import Region, AreaOfOperation, AreaOfOperationType, AreaOfOperationFlavor, Pax
from q_school.geography.serializers import RegionSerializer



class RegionsView(View):
    template = "region_page.html"
    
    def get(self, request):
        regions = Region.objects.all()
        return render(request, self.template, {'regions': regions, 'countries': countries})
    
    def post(self, request):
        """
        creates a new region if it can
        """
        request_json = json.loads(request.body)
        region, created = Region.objects.get_or_create(
            name=request_json['region_name'],
            associated_country=request_json['region_country'],
            associated_territory=request_json['region_territory'],
            associated_city=request_json['region_city']
        )
        if created:
            region.description = request_json['region_description']
            region.save()
            return HttpResponse(status=204)
        return JsonResponse({"error": f"Region with name {request_json['region_name']} already exists"}, status=409)


class RegionView(View):
    template = "region_details_page.html"
    
    def get(self, request, region_index):
        regions = Region.objects.filter(pk=region_index)
        # pax_list = Pax.objects.all().values('f3_handle', 'user__last_name', 'user__first_name', 'user__username')
        # pax_list = json.dumps(list(pax_list), cls=DjangoJSONEncoder)})
        if regions:
            return render(request, self.template, {'region': regions[0], 'countries': countries})
    
    def post(self, request, region_index):
        """
        modify the current region
        """
        request_json = json.loads(request.body)
        
        regions = Region.objects.filter(
            name=request_json['region_name'],
            associated_country=request_json['region_country'],
            associated_territory=request_json['region_territory'],
            associated_city=request_json['region_city']
        )
        if len(regions) > 1:
            return JsonResponse({"error": f"Region with requested parameters already exists"}, status=409)
        this_region = Region.objects.get(pk=region_index)
        this_region.name=request_json['region_name']
        this_region.associated_country=request_json['region_country']
        this_region.associated_territory=request_json['region_territory']
        this_region.associated_city=request_json['region_city']
        this_region.description=request_json['region_description']
        this_region.save()
        return HttpResponse(status=204)
        

class AreaOfOperationView(View):
    template = "ao_page.html"
    template_detail = "ao_details_page.html"

    def get(self, request, ao_index=""):
        if not ao_index:
            areas = AreaOfOperation.objects.all()
            ao_types = AreaOfOperationType.objects.all()
            return render(request, self.template, {
                'areas': areas, 
                'countries': countries,
                'ao_types': ao_types
                })
        return HttpResponse(status=404)

    def post(self, request, ao_index=""):
        data = json.loads(request.body)
        # AreaOfOperation.objects.get_or_create(
        #     name=data['name'],
        #     primary_site_q=Pax.objects.get(email=data['name']),
        #     gps_long=data['area_long'],
        #     gps_lat=data['area_lat'],
        #     city=data['city'],
        #     state=data['area_state'],
        #     country=data['country'],

        # )
        print(json.dumps(data, indent=4))
        return HttpResponse(status=204)


class RegionViewSet(APIView):
    """
    API endpoint for region information
    """
    queryset = Region.objects.all().order_by('name')
    serializer_class = RegionSerializer

    def get(self, request, format=None):
        """
        get all region information
        """
        response = Region.objects.all().values('pk', 'name', 'associated_city', 'associated_country', 'associated_territory', 'description')
        return Response(response)
