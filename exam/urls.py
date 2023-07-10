from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homePage),
    path("list_view/", list, name="list_view"),
    path("list/", list2, name="list"),
    path("create/", products_create_view, name="create"),
    path("detail_view/<id>/", detail, name="detail_view"),
    path("update/<id>/", product_update_view, name="update"),
    # REST API
    # path("index/", index_view, name="index"),
    # path("test/post/", test_post_view, name="test"),
    ########################
    # path("product/list/", product_test_view, name="product_list_view"),
    # path("test/detail/<id>/", test_view, name="detail"),
    # path("test/create/", create_test, name="test_create"),
    path("test/list/", TestListView.as_view(), name="test_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
