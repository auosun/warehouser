from django.db import models
from django.contrib.auth.hashers import make_password,check_password

# Create your models here.
class User(models.Model):
    class Meta:
        db_table='user'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    register_time = models.DateTimeField()
    # status = models.IntegerField(default='1')

    def __str__(self):
        return self.name

    def _set_password(self,password):
        self.password = make_password(password)

    def _check_password(self,password):
        return check_password(password,self.password)

class UserLoginrecord(models.Model):
    class Meta:
        db_table='user_loginrecord'

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    login_time = models.DateTimeField()





