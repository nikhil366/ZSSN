from curses import meta
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class SerializersSurvivor(serializers.ModelSerializer):

    class Meta:
        model = Survivor
        fields = '__all__'
