# serializers.py

from rest_framework import serializers
from .models import Event
from categories.models import Category
from users.models import CustomUser

class LimitedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')

class EventSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    student_organizer = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='student'), many=True)
    staff_organizer = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(role='staff'), many=True)
    thumbnail = serializers.ImageField(required=False, allow_null=True)  # New field

    class Meta:
        model = Event
        fields = '__all__'
