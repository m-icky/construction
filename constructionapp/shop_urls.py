from django.urls import path
from constructionapp.shop_views import IndexView, cancel, product_add, product_reject, profeed, view_booking, view_feed, view_product





urlpatterns = [

    path('',IndexView.as_view()),
    path('product_add',product_add.as_view()),
    path('product_view',view_product.as_view()),
    path('reject',product_reject.as_view()),
    path('view_booking',view_booking.as_view()),
    path('cancel',cancel.as_view()),
    path('feed',view_feed.as_view()),
    path('profeed',profeed.as_view()),



    ]
def urls():
    return urlpatterns, 'product', 'product'