from rest_framework import serializers
from .models import MemberDetails, Members

class MemberDetailSerializer(serializers.ModelSerializer):
    """To Convert Data into Json formate"""
    class Meta:
        model = MemberDetails
        fields = ['start_time','end_time']
                
class MemberSerializer(serializers.ModelSerializer):
    """To Convert Data into Json formate"""
    activity_Period = MemberDetailSerializer(many=True)
    class Meta:
        """Meta used for which model and which model & fields"""
        model = Members 
        fields = ['id','real_name','tz','activity_Period']