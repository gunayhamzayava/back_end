from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import Coalesce
from django.db.models import FloatField, F, Avg
from .forms import ProductForm
from .serializers import *

from .models import *


def list(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=(F("price") - F("discount")),
    )
    context = {"products": products}

    return render(request, "list_view.html", context)


def list2(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=(F("price") - F("discount")),
    )
    context = {"products": products}

    return render(request, "list.html", context)


def detail(request, id):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount"),
    ).get(id=id)

    context = {"products": products}

    return render(request, "detail_view.html", context)


def products_create_view(request):
    products = Product.objects.annotate(
        discount=Coalesce("discount_price", 0, output_field=FloatField()),
        total_price=F("price") - F("discount"),
    )

    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)

        if (
            form.is_valid()
        ):  # --> meselen inputda max_length 255 dise ve cox yazsalar onda error cixir.
            # new_product = form.save()
            # new_product.name = 'gunay'
            # new_product.save()  # --> bir deyisene beraber edib daha sonra onun deyerini ozumuz evvelden teyin ede bilerik

            # new_product = form.save()
            # if new_product.name == 'gunay':
            #     new_product.name = 'adas'
            #     new_product.save()
            # else:
            # form.save() --> #eger ad gunaydisa adi deyis adas olsun

            form.save()
            # sehife yenilenmeli ya da basqa sehifeye kecid olmalidi
            return redirect("list_view")
        else:
            print(form.errors)

    context = {"products": products, "form": form}

    return render(request, "create_view.html", context)


def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("list_view")

    context = {"form": form}
    return render(request, "update.html", context)


def homePage(request):
    author = Author.objects.all()
    context = {"author": author}

    return render(request, "home.html", context)


# REST API
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view()
# def index_view(request):
#     return Response({"text": "Hello World"})


# @api_view(["GET", "POST"])
# def test_post_view(request):
#     print(request.data)
#     if request.method == "POST":
#         return Response(request.data)

#     return Response({"text": "Hello World"})


# ##################
# # @api_view(["GET"])
# # def product_test_view(request):
# #     queryset = Test.objects.all()
# #     serializer = ProductSerializer(queryset, many=True)
# #     print(serializer.data)
# #     return Response(serializer.data)


# @api_view(["GET"])
# def product_test_view(request):
#     queryset = Test.objects.all()
#     serializer = TestProductSerializer(queryset, many=True)
#     print(serializer.data)
#     return Response(serializer.data)


# @api_view(["GET"])
# def test_view(request, id):
#     test = Test.objects.get(id=id)
#     serializers = TestProductSerializer(test)
#     return Response(serializers.data)


# @api_view(["POST"])
# def create_test(request):
#     # print(request.data)
#     serializers = TestProductSerializer(data=request.data)
#     if serializers.is_valid():
#         serializers.save()
#     return Response(serializers.data)

from rest_framework import generics


class TestListView(generics.ListAPIView):
    # queryset = Test.objects.order_by("-created_at")
    # serializer_class = TestProductSerializer

    # get queryset islenende querysete ehtuyac qalmir
    def get_queryset(self):
        avg_price = Test.objects.aggregate(avg_price=Avg("price"))["avg_price"]
        return Test.objects.filter(price__gte=avg_price).order_by("-created_at")
    
    def get_serializer(self):
        return TestProductSerializer
