from django.db import models
from django.db import connection

class User_Login(models.IntegerField(primary_key=True)):
       id           = models.IntegerField(primary_key=True)
       user_name    = models.CharField(max_length=100)
       password     = models.CharField(max_length=100)
       user_ip      = models.CharField(max_length=100)
       otdel        = models.CharField(max_length=100)
       podrazdelen  = models.CharField(max_length=100)
       priveleg     = models.CharField(max_length=100)
       account_condit  = models.CharField(max_length=100)
       class Meta:
              db_table = "users"

