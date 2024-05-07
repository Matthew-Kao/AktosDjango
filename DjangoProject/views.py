from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

class AccountListView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Account.objects.all().order_by('balance')
        min_balance = self.request.query_params.get('min_balance')
        max_balance = self.request.query_params.get('max_balance')
        consumer_name = self.request.query_params.get('consumer_name')
        status = self.request.query_params.get('status')

        if min_balance:
            queryset = queryset.filter(balance__gte=min_balance)
        if max_balance:
            queryset = queryset.filter(balance__lte=max_balance)
        if consumer_name:
            queryset = queryset.filter(consumer__name__icontains=consumer_name)
        if status:
            queryset = queryset.filter(status__iexact=status)

        return queryset
