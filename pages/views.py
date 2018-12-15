from django.shortcuts import render, redirect
from .forms import TestForm
from .models import Post

# Create your views here.

def home(request):
	Post.objects.all().delete()
	if request.method == 'POST':
		my_form = TestForm(request.POST)
		context = {
			"form": my_form,
		}
		if my_form.is_valid():
			my_form.save()
		#return render(request, 'result.html', context)
		return redirect('result')
	else:
		my_form = TestForm()
		context = {
			"form": my_form,
		}
		return render(request, 'home.html', context)

def result(request):
	posts = Post.objects.all()
	post = posts[0]
	results = []
	for attr, value in post.__dict__.items(): 
		results.append(value)
	del results[0]
	del results[0]
	args = {
		'post': post,
		'results': results,
	}
	return render(request, 'result.html', args)





#RIFERIMENTO SOTTO, NON E' IMPLEMENTATO
def search(request):
	my_form = SearchForm()
	my_result = "checking..."
	my_width = "width: 50%"
	if request.method == "POST":
		my_form = SearchForm(request.POST)
		print(my_form)
		if my_form.is_valid():
			result = my_form.cleaned_data.get("search_bar")
			my_width = "width: " + str(result) + "%"
			if result>3:
				my_result = "bene!"
			else:
				my_result = "male"
	context = {
		"form": my_form,
		"result": my_result,
		"line_width": my_width
	}
	return render(request, "search.html", context)