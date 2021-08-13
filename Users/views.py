from django.shortcuts import render,redirect
from Users.models import User,Post
from Products.models import Product
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def index(request):
	if request.session.has_key('username'):
		data = Product.objects.all()
		p = Post.objects.filter(user=request.session.get('username'))
		return render(request, template_name="index.html",context={'user':data,'p':p})
	else:
		return redirect('login')
def login(request):
	if request.method=="POST":
		username = request.POST.get('email',False)
		pas = request.POST.get('password')
		for data in User.objects.all():
			e=data.email
			p=data.password
			if e==username and p==pas:
				messages.success(request, message="Login successfully")
				request.session['uid'] = data.pk
				request.session['username'] = data.username
				request.session['email'] = data.email
				request.session['name'] = data.first_name+" "+data.last_name
				return redirect('home')
			else:
				messages.warning(request, message="Invalid input plz try again")
				return redirect('login')
	return render(request, template_name="login.html")

def register(request):
	fm = UserForm()
	if request.method=="POST":
		fm = UserForm(request.POST)
		if fm.is_valid():
			fm.save()
			messages.success(request, message="Register successfully")
			return redirect('login')

	return render(request, template_name="register.html",context={"form":fm})

def logout_view(request):
	request.session.flush()
	messages.info(request, message="Logout successfully!")
	return redirect('login')