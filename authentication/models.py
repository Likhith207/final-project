from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    USER_TYPE=(
        ('buyer','Buyer'),
        ('seller' ,'Seller')

    )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user=models.OneToOneField (User,on_delete=models.CASCADE,related_name='user_profile')
    user_role=models.CharField(choices=USER_TYPE)
    profile_photo=models.ImageField(upload_to='profiles/')
    phone_number=models.PositiveIntegerField()
    address=models.TextField()


    def __str__ (self):
        return f"{self.user_role} Profile  > {self.first_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
     

