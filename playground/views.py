from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Customer, Collection, Order
from tags.models import TaggedItem


def say_hello(request):
    queryset = Product.objects.raw('SELECT * FROM store_product')

    return render(request, 'hello.html', {'name': 'Mosh', 'result': list(queryset)})
