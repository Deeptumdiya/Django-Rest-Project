# Create your models here.
from django.db import models
import pytz
from datetime import datetime

# Create your models here.
class Members(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.CharField(primary_key=True, max_length=50)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    
    def __str__(self):
        return self.real_name    
    
class MemberDetails(models.Model):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    member = models.ForeignKey(Members,on_delete=models.CASCADE, related_name='activity_Period')
    
    
      