from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.shortcuts import render
from constructionapp.models import Cart, feedback, shop_reg, user_reg
from constructionapp.models import add_product




class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'
    
    
class shop_verify(TemplateView):
    template_name = 'admin/shop_approvel.html'
    def get_context_data(self, **kwargs):
        context = super(shop_verify,self).get_context_data(**kwargs)

        shop = shop_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['shop'] = shop
        return context
    
class shop_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class shop_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
    
    
    
class user_verify(TemplateView):
    template_name = 'admin/user_approvel.html'
    def get_context_data(self, **kwargs):
        context = super(user_verify,self).get_context_data(**kwargs)

        user = user_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['user'] = user
        return context
    
class user_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class user_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
    
    
class view_product(TemplateView):
    template_name = 'admin/view_product.html'
    def get_context_data(self, **kwargs):
        context = super(view_product,self).get_context_data(**kwargs)

        product = add_product.objects.all()

        context['product'] = product
        return context

class product_delete(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        add_product.objects.get(id=id).delete()

        return render(request,'admin/admin_index.html',{'message':" Removed"})
    
    
class Booking(TemplateView):
    template_name = 'admin/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(Booking,self).get_context_data(**kwargs)
        # u = user_reg.objects.all()

        cart = Cart.objects.filter(payment='paid')

        context['cart'] = cart
        return context
    
    
    
class view_shop(TemplateView):
    template_name = 'admin/shop_view.html'
    def get_context_data(self, **kwargs):
        context = super(view_shop,self).get_context_data(**kwargs)

        shop = shop_reg.objects.filter(user__last_name='1',user__is_active='1')

        context['shop'] = shop
        return context
    
    
class deactivate_shop(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
    
    
    
    
    
class view_user(TemplateView):
    template_name = 'admin/user_view.html'
    def get_context_data(self, **kwargs):
        context = super(view_user,self).get_context_data(**kwargs)

        user = user_reg.objects.filter(user__last_name='1',user__is_active='1')

        context['user'] = user
        return context
    
    
class deactivate_user(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
    
    

class view_feed(TemplateView):
    template_name = 'admin/adminfeed_index.html'
    def get_context_data(self, **kwargs):
        context = super(view_feed,self).get_context_data(**kwargs)

        feed = feedback.objects.filter(status='Added')

        context['feed'] = feed
        return context
    
    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['action']
        act = feedback.objects.get(pk=id)
        # act.complaint=complaint
        act.action = action
        act.status = 'replied'
        act.save()

        return render(request,'admin/admin_index.html',{'message':" Replied Successfull"})
    

class viewprofeed(TemplateView):
    template_name = 'admin/view_profeedback.html'
    def get_context_data(self, **kwargs):
        context = super(viewprofeed,self).get_context_data(**kwargs)

        feed = Cart.objects.all()

        context['feed'] = feed
        return context