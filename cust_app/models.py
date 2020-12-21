from django.db import models
from datetime import datetime

# Create your models here.
class Services(models.Model):
    pk_bint_id = models.BigAutoField(primary_key = True)
    vchr_name = models.CharField(max_length=100)

    def __str__(self):
        return self.vchr_name

    # class Meta:
    #     managed=False
    #     db_table="services"

class Customer(models.Model):
    pk_bint_id = models.BigAutoField(primary_key = True)
    vchr_name = models.CharField(max_length=100)
    bint_mobile = models.BigIntegerField()

    def __str__(self):
        return self.vchr_name

    # class Meta:
    #     managed=False
    #     db_table="customers"

class SalesData(models.Model):
    pk_bint_id = models.BigAutoField(primary_key = True)
    dat_sale = models.DateField()
    dbl_amount = models.DecimalField(decimal_places=2, max_digits=10)
    dbl_service_charge = models.DecimalField(decimal_places=2, max_digits=10)
    int_paid_status = models.IntegerField()
    int_staus = models.IntegerField()
    vchr_ref_no = models.CharField(max_length=10)
    dat_created = models.DateTimeField(default=datetime.now(), blank=True)
    fk_service_id = models.ForeignKey(Services, on_delete = models.PROTECT)
    fk_customer_id = models.ForeignKey(Customer, on_delete = models.PROTECT)

    def __str__(self):
        return self.fk_service_id.vchr_name

    # class Meta:
    #     managed=False
    #     db_table="sales_data"
