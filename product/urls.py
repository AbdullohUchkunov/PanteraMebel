from . import signals

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet,SubCategoryViewSet,OrderListApiView
from .views import ReviewUserListCreateView, FlashSaleListCreateView,SubCategoryByCategory,ProductListByCategory

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'SubCategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
# router.register(r'products', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('order/', OrderListApiView.as_view(), name='review'),
    path('review/', ReviewUserListCreateView.as_view(), name='review'),
    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('products/by_category/<int:category_id>/', ProductListByCategory.as_view(), name='product_by_category_id'),
    path('category/by_sub_category/<int:sub_category_id>/', SubCategoryByCategory.as_view(), name='category_by_sub_ategory'),
]