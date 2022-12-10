from django.urls import path

from constructionapp.user_views import IndexView, RejectcartView, Singleproducts, addcart, bill, booking, cancel, checkout, feed_back, payment, profeedback, profile, view_feedback,view_product, view_shop, viewcart





urlpatterns = [

    path('',IndexView.as_view()),
    path('shop',view_shop.as_view()),
    path('product',view_product.as_view()),
    path('cart',addcart.as_view()),
    path('viewcart',viewcart.as_view()),
    path('pay',checkout.as_view()),
    path('single',Singleproducts.as_view()),
    path('removecart',RejectcartView.as_view()),
    path('bill',bill.as_view()),
    path('payment',payment.as_view()),
    path('booking',booking.as_view()),
    path('cancel',cancel.as_view()),
    path('view_feedback',view_feedback.as_view()),
    path('profile',profile.as_view()),
    path('feedback',feed_back.as_view()),
    path('profeedback',profeedback.as_view()),
    








    ]
def urls():
    return urlpatterns, 'user', 'user'