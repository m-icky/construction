from django.urls import path
from constructionapp.admin_views import Booking, IndexView, deactivate_shop, deactivate_user, product_delete, product_delete, shop_approve, shop_reject, shop_verify, user_approve, user_reject, user_verify, view_feed, view_product, view_shop, view_user, viewprofeed





urlpatterns = [

    path('',IndexView.as_view()),
    path('shop_approve',shop_verify.as_view()),
    path('approve',shop_approve.as_view()),
    path('reject',shop_reject.as_view()),
    path('user_approve',user_verify.as_view()),
    path('approve',user_approve.as_view()),
    path('reject',user_reject.as_view()),
    path('product_view',view_product.as_view()),
    path('delete',product_delete.as_view()),
    path('booking',Booking.as_view()),
    path('shop',view_shop.as_view()),
    path('delete_shop',deactivate_shop.as_view()),
    path('user',view_user.as_view()),
    path('delete_user',deactivate_user.as_view()),
    path('view_feed',view_feed.as_view()),
    path('viewprofeed',viewprofeed.as_view()),




    
    

    ]
def urls():
    return urlpatterns, 'admin', 'admin'