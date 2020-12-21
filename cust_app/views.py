from django.shortcuts import render
from cust_app.models import Customer, Services, SalesData
from cust_app.serializer import CustomerSerializer, ServicesSerializer, SalesDataSerializer
from rest_framework import viewsets



class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class SalesDataViewset(viewsets.ModelViewSet):
    queryset = SalesData.objects.all()
    serializer_class = SalesDataSerializer

# class FriendViewset(viewsets.ModelViewSet):
#     queryset = models.SalesData.objects.all()
#     serializer_class = serializers.SalesDataSerializer
#     def list(self,request):
#         pass
#     def post(self,request):
#         serializer = SalesDataSerializer(data=request.data)
#         if serializer.is_valid():
#             int_cust_id=Customer.objects.filter(bint_mobile=request.data('bint_mobile'))
#             serializer.fk_customer_id=int_cust_id
#             serializer.save()
#             return JsonResponse(serializer.data)
#         pass
#
