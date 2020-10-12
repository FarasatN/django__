from django.shortcuts import render, HttpResponse
# Create your views here.

def home_view(request):	
	if request.user.is_authenticated:
		context = {
			'name': 'Farasat',
		}
	else:
		context = {
			'name': 'Guest',
		}
	return render(request, 'home.html', context)