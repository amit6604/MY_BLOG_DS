from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blogging, BloggingSeries, BloggingCategory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.

def single_slug(request, single_slug):
	categories = [c.category_slug for c in BloggingCategory.objects.all()]
	if single_slug in categories:
		matching_series = BloggingSeries.objects.filter(blog_category__category_slug=single_slug)

		series_urls = {}
		for m in matching_series.all():
			part_one = Blogging.objects.filter(blog_series__blog_series=m.blog_series).earliest("blog_published")
			series_urls[m] = part_one
		return render(request, "main/category.html", {"part_ones": series_urls})


	bloggings = [b.blog_slug for b in Blogging.objects.all()]

	if single_slug in bloggings:
		return HttpResponse(f"{single_slug} is a blog!!!")

	return HttpResponse(f"{single_slug} does not correspond to anything.")

def homepage(request):
	return render(request = request, 
				  template_name = "main/categories.html",
				  context = {"categories" : BloggingCategory.objects.all})



def register(request):	
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form .cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			messages.info(request, f"You are now logged in as : {username}")
			login(request, user)
			return redirect("main:homepage")

		else :
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

				
	form = NewUserForm
	return render(request, "main/register.html", context = {"form": form})



def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("/")


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form .cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as  {username}")
				return redirect("main:homepage")
			else : 
				messages.error(request, "Invalid username or password")


	form = AuthenticationForm()
	return render(request, "main/login.html", {"form": form})
