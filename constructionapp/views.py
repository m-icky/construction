from django.shortcuts import render
from django.views.generic import TemplateView
from constructionapp.models import UserType, shop_reg,user_reg
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect





# Create your views here.
class indexView(TemplateView):
    template_name='index.html'  
    
    
class registration(TemplateView):
    template_name='register.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'register.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            se = user_reg()
            se.user = user
            se.phone = phone
            se.address=address
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()


            return render(request, 'login.html', {'message': "successfully added"})
        
        

class Shop_reg(TemplateView):
    template_name='shop_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        address = request.POST['address']
        email= request.POST['email']
        phone= request.POST['phone']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'shop_reg.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            shop_owner = shop_reg()
            shop_owner.user = user
            shop_owner.address = address
            shop_owner.phone = phone
            shop_owner.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "shop"
            usertype.save()

            return render(request, 'login.html', {'message':"successfully added"})
        
        
class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password= request.POST['password']

        user = authenticate(username=email,password=password)
        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                # elif UserType.objects.get(user_id=user.id).type == "shop":
                #     return redirect('/shop')
                else:
                    return redirect('/shop')

            else:


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})