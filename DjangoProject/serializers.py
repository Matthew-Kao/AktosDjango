from rest_framework import serializers
from .models import Account, Consumer

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['name', 'address'] 

class AccountSerializer(serializers.ModelSerializer):
    consumer = ConsumerSerializer()  

    class Meta:
        model = Account
        fields = ['id', 'client_reference_no', 'balance', 'status', 'consumer']