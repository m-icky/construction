from django.views.generic import TemplateView
from constructionapp.models import Cart, add_product, feedback, shop_reg, user_reg
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage





class IndexView(TemplateView):
    template_name = 'user/user_index.html'
    
    


class view_shop(TemplateView):
    template_name = 'user/view_shop.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(view_shop, self).get_context_data(**kwargs)
        sh = shop_reg.objects.filter(user__last_name='1')
        context['sh'] = sh
        return context

    def post(self, request, *args, **kwargs):
        address = request.POST['address']
        host = shop_reg.objects.filter(address__icontains=address)
        return render(request, 'user/search.html', {'sh': host})
    
        
    
    
class view_product(TemplateView):
    template_name = 'user/view_product.html'
    def get_context_data(self, **kwargs):
        id =self.request.GET['id']
        context = super(view_product,self).get_context_data(**kwargs)
        shop = shop_reg.objects.get(user_id=id)

        pro = add_product.objects.filter(shop_id=shop.id)

        context['pro'] = pro
        context['userid']=id
        context['shop_id']=shop.id
        return context
    

    
# class view_product(TemplateView):
#     template_name = 'user/view_product.html'
#     login_url = '/'

#     def get_context_data(self, **kwargs):
#         context = super(view_product, self).get_context_data(**kwargs)
#         s = add_product.objects.all()
#         context['s'] = s
#         return context

#     def post(self, request, *args, **kwargs):
#         location = request.POST['location']
#         host = add_product.objects.filter(location__icontains=location)
#         return render(request, 'user/search.html', {'s': host})
    
    


class Singleproducts(TemplateView):
    template_name = 'user/product.html'

    def get_context_data(self, **kwargs):
        id =self.request.GET['id']

        context = super(Singleproducts, self).get_context_data(**kwargs)

        single_view = add_product.objects.get(id=id)
        shop = add_product.objects.get(id=id)


        context['single_view'] = single_view
        context['shop_id']=shop.shop_id

        return context
    
    
class addcart(TemplateView):
    template_name = 'user/product.html'
    def dispatch(self, request, *args, **kwargs):
        pid = request.POST['id']
        qunty =request.POST['quantity']
        shop = add_product.objects.get(pk=pid)
        price=shop.price
        qty=shop.quantity
        
        Total= int(qunty)*int(price)
        # shop.quantity=int(qty)-int(qunty)  
        a=int(shop.quantity)-int(qunty)
        if a < 0:
            return render(request,'user/user_index.html',{'message':" Out Of Stock"})
        else:
            shop.quantity=a
            shop.save()
            shopp = shop_reg.objects.get(id=shop.shop_id)
            ca = Cart()
            ca.user = User.objects.get(id=self.request.user.id)
            ca.shop_id = shopp.id
            ca.product = add_product.objects.get(pk=pid)
            ca.payment = 'null'
            ca.quantity=qunty
            ca.status = 'cart'
            ca.delivery = 'null'
            ca.total=Total
            ca.save()
            return redirect(request.META['HTTP_REFERER'],{'message':"cart"})
    
               
       


class viewcart(TemplateView):
    template_name = 'user/cart.html'
    def get_context_data(self, **kwargs):
        context = super(viewcart, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        cr = self.request.user.id

        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null')

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context
    
    
    
    
class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Cart.objects.get(id=id).delete()


        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})
    
    

class bill(TemplateView):
    template_name = 'user/bill.html'
    def get_context_data(self, **kwargs):
        context = super(bill, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        cr = self.request.user.id

        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null')

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context

    

class checkout(TemplateView):
    template_name = 'user/payment.html'
    def get_context_data(self, **kwargs):
        context = super(checkout, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        cr = self.request.user.id

        ct = Cart.objects.filter(status='cart', user_id=cr, delivery='null')

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context

    
    
class payment(TemplateView):
    template_name= 'user/payment.html'
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id

        ch = Cart.objects.filter(user_id=pid,status='cart')


        print(ch)
        for i in ch:
            i.payment='paid'
            i.status='Available'
            i.delivery = 'delivered'
            i.save()
        return render(request,'user/user_index.html',{'message':" payment Successfull, Check Booking Details"})
    
    
class booking(TemplateView):
    template_name = 'user/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(booking,self).get_context_data(**kwargs)
        id=self.request.user.id
        cart = Cart.objects.filter(payment='paid', user_id=id)

        context['cart'] = cart
        return context
    
    
class cancel(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Cart.objects.get(id=id).delete()
        
  
        return render(request,'user/user_index.html',{'message':"Product Canceled, Amount will Refund within 24 hours."})



# class addfeed(TemplateView):
#     template_name = 'user/feedback.html'
#     def get_context_data(self, **kwargs):
#         context = super(addfeed,self).get_context_data(**kwargs)
#         id=self.request.user.id
#         cart = Cart.objects.filter(payment='paid', user_id=id, )
#         context['cart'] = cart
#         return context
    
#     def post(self , request,*args,**kwargs):
#         id = request.POST['id'] 
#         # user = User.objects.get(pk=self.request.user.id)
#         action= request.POST['action']
        
         
#         car = Cart.objects.get(pk=id)           
#         car.action = action
#         car.statuss = "send"
#         car.save()

#         return render(request, 'user/feedback.html', {'message':"successfully Submit Your Feedback"})



    
class feed_back(TemplateView):
    template_name='user/feedback.html'
    def post(self , request,*args,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        subject= request.POST['subject']
        feed= request.POST['feedback']
        
        fee =feedback()
        fee.user = user
        fee.subject = subject
        fee.feedback = feed
        fee.status = "Added"
        fee.statuss = "send"
        fee.save()

        return render(request, 'user/feedback.html', {'message':"successfully Submit Your Feedback"})
   
    
    
class view_feedback(TemplateView):
    template_name = 'user/view_feed.html'
    def get_context_data(self, **kwargs):
        context = super(view_feedback,self).get_context_data(**kwargs)
        id=self.request.user.id
        feed = feedback.objects.filter(user_id=id)

        context['feed'] = feed
        return context
    
    
class profile(TemplateView):
    template_name = 'user/user_profile.html'
    def get_context_data(self, **kwargs):
        context = super(profile,self).get_context_data(**kwargs)
        id=self.request.user.id
        pro = user_reg.objects.get(user_id=id)

        context['pro'] = pro
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id'] 
        id2 = request.POST['id2']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        i = User.objects.get(pk=id)
        u = user_reg.objects.get(pk=id2)
        i.first_name = name
        i.email = email
        i.save()
        u.address = address
        u.phone = phone
        u.save()
        
        return render(request,'user/user_index.html',{'message':"Profile Updated"})
    
    
class profeedback(TemplateView):
    template_name = 'user/product_feed.html'
    def get_context_data(self, **kwargs):
        context = super(profeedback,self).get_context_data(**kwargs)
        id=self.request.user.id
        cart = Cart.objects.filter(payment='paid', user_id=id)

        context['cart'] = cart
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.GET['id'] 
        feed = request.POST['feedback']
        i = Cart.objects.get(pk=id)
        i.feedback = feed
        i.save()
        
        return render(request,'user/user_index.html',{'message':"Feedback Added"})