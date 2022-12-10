from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from constructionapp.models import Cart, add_product, feedback, shop_reg
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage









class IndexView(TemplateView):
    template_name = 'shop/shop_index.html'
    
    
class product_add(TemplateView):
    template_name='shop/add_product.html'
    def post(self , request,*args,**kwargs):
        com=shop_reg.objects.get(user_id=self.request.user.id)
        user = User.objects.get(pk=self.request.user.id)
        name = request.POST['name']
        price= request.POST['price']
        quantity= request.POST['quantity']
        description= request.POST['description']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
            
        product =add_product()
        product.user = user
        product.shop_id=com.id
        product.name = name
        product.price = price
        product.quantity = quantity
        product.description = description
        product.image = filesss
        product.save()

        return render(request, 'shop/add_product.html', {'message':"successfully added"})
    
    
class view_product(TemplateView):
    template_name = 'shop/view_product.html'
    def get_context_data(self, **kwargs):
        context = super(view_product,self).get_context_data(**kwargs)
        shop = shop_reg.objects.get(user_id=self.request.user.id)
        product = add_product.objects.filter(shop_id = shop.id)

        context['product'] = product
        return context

class product_reject(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_product.objects.get(id=id).delete()

        return render(request,'shop/shop_index.html',{'message':"Product Removed"})
    
    
    
class view_booking(TemplateView):
    template_name = 'shop/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(view_booking,self).get_context_data(**kwargs)
        # u = user_reg.objects.all()
        shop = shop_reg.objects.get(user_id=self.request.user.id)
        cart = Cart.objects.filter(payment='paid', shop_id = shop.id)

        context['cart'] = cart
        return context
    
    
class cancel(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        ca = Cart.objects.get(id=id)
        ca.status='Out Of Stock'
        ca.save()

        return render(request,'shop/shop_index.html',{'message':"Product Canceled"})
    
    
    
class view_feed(TemplateView):
    template_name = 'shop/view_feed.html'
    def get_context_data(self, **kwargs):
        context = super(view_feed,self).get_context_data(**kwargs)

        fe = feedback.objects.filter(statuss='send')

        context['fe'] = fe
        return context
    
    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        actions = request.POST['actions']
        act = feedback.objects.get(pk=id)
        # act.complaint=complaint
        act.actions = actions
        act.statuss = 'done'
        act.save()

        return render(request,'shop/shop_index.html',{'message':" Replied Successfull"})
    
class profeed(TemplateView):
    template_name = 'shop/view_profeed.html'
    def get_context_data(self, **kwargs):
        context = super(profeed,self).get_context_data(**kwargs)
        shop = shop_reg.objects.get(user_id=self.request.user.id)
        fee = Cart.objects.filter(shop_id = shop.id)

        context['fee'] = fee
        return context
    