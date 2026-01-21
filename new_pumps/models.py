# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CcVehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    cc = models.ForeignKey('CreditCustomer', models.DO_NOTHING, blank=True, null=True)
    vehicle_num = models.CharField(max_length=20)
    fuel = models.ForeignKey('Fuels', models.DO_NOTHING, blank=True, null=True)
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    tank_capacity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_vehicles'


class CreditCustomer(models.Model):
    cc_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey('Pumps', models.DO_NOTHING, blank=True, null=True)
    cc_name = models.CharField(max_length=200)
    cc_address = models.TextField(blank=True, null=True)
    cc_city = models.CharField(max_length=50, blank=True, null=True)
    cc_state = models.CharField(max_length=50, blank=True, null=True)
    cc_mobile = models.CharField(max_length=15, blank=True, null=True)
    cc_whatsapp = models.CharField(max_length=15, blank=True, null=True)
    cc_email = models.CharField(max_length=100, blank=True, null=True)
    cc_gst = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_customer'


class CreditEntry(models.Model):
    trxn_id = models.AutoField(primary_key=True)
    trxn_datetime = models.DateTimeField()
    cc = models.ForeignKey(CreditCustomer, models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey(CcVehicles, models.DO_NOTHING, blank=True, null=True)
    chit_num = models.IntegerField(blank=True, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    fuel_rate = models.ForeignKey('FuelRate', models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    remark = models.CharField(max_length=500, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_entry'


class DipStockChart(models.Model):
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    dip = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dip_stock_chart'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FuelRate(models.Model):
    pump = models.ForeignKey('Pumps', models.DO_NOTHING, blank=True, null=True)
    rate_date = models.DateField()
    fuel = models.ForeignKey('Fuels', models.DO_NOTHING, blank=True, null=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_rate'


class Fuels(models.Model):
    fuel_id = models.AutoField(primary_key=True)
    fuel_name = models.CharField(max_length=50)
    shorthand = models.CharField(max_length=10)
    hsn_code = models.IntegerField(blank=True, null=True)
    uom = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuels'


class Nozzles(models.Model):
    nozzleid = models.AutoField(primary_key=True)
    pump = models.ForeignKey('Pumps', models.DO_NOTHING, blank=True, null=True)
    tank = models.ForeignKey('TankTable', models.DO_NOTHING, blank=True, null=True)
    nozzle_name = models.CharField(max_length=50, blank=True, null=True)
    du_serial = models.CharField(max_length=100, blank=True, null=True)
    fuel = models.ForeignKey(Fuels, models.DO_NOTHING, blank=True, null=True)
    initial_reading = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nozzles'


class Oil_Company(models.Model):
    oil_comp_id = models.AutoField(primary_key=True)
    oc_name = models.CharField(max_length=100)
    oc_shorthand = models.CharField(max_length=10)
    oc_logo = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oil_company'
    
    def __str__(self):
        return self.oc_name


class PaymentMethod(models.Model):
    pump = models.ForeignKey('Pumps', models.DO_NOTHING, blank=True, null=True)
    method_name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_method'


class PaymentsData(models.Model):
    trxn_id = models.AutoField(primary_key=True)
    method = models.ForeignKey(PaymentMethod, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments_data'


class Pumps(models.Model):
    pump_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact1 = models.CharField(max_length=15, blank=True, null=True)
    contact2 = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gst = models.CharField(max_length=20, blank=True, null=True)
    pan = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.IntegerField(blank=True, null=True)
    oc = models.ForeignKey(Oil_Company, models.DO_NOTHING, blank=True, null=True)
    petrol = models.BooleanField(blank=True, null=True)
    petrol95 = models.BooleanField(blank=True, null=True)
    petrol100 = models.BooleanField(blank=True, null=True)
    diesel = models.BooleanField(blank=True, null=True)
    diesel_turbo = models.BooleanField(blank=True, null=True)
    cng = models.BooleanField(blank=True, null=True)
    electric = models.BooleanField(blank=True, null=True)
    lubes = models.BooleanField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pumps'


class Readings(models.Model):
    trxn_id = models.AutoField(primary_key=True)
    nozzleid = models.ForeignKey(Nozzles, models.DO_NOTHING, db_column='nozzleid', blank=True, null=True)
    reading_date = models.DateField()
    reading = models.DecimalField(max_digits=12, decimal_places=2)
    testing = models.IntegerField(blank=True, null=True)
    meter_sale = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readings'


class TankStock(models.Model):
    trxn_id = models.AutoField(primary_key=True)
    tank = models.ForeignKey('TankTable', models.DO_NOTHING, blank=True, null=True)
    stock_date = models.DateField()
    dip = models.DecimalField(max_digits=10, decimal_places=2)
    dip_sale = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    decant_vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    variance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    water_level = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tank_stock'


class TankTable(models.Model):
    tank_id = models.AutoField(primary_key=True)
    pump = models.ForeignKey(Pumps, models.DO_NOTHING, blank=True, null=True)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    fuel = models.ForeignKey(Fuels, models.DO_NOTHING, blank=True, null=True)
    initial_dip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tank_table'

# End of models.py
