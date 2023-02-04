# apps/sekdilu139/views.py

# Import from django modules
from django.shortcuts import render


# HOME PAGE
def home_page(request):
	return render(request, 'sekdilu139/index.html')