from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'phonebook/homepage.html')

def contact(request):
	return render(request, 'phonebook/basic.html',{'values':['Если у вас остались вопросы, то задавайте их по телефону']})


# Create your views here.
