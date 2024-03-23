from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('users:login')
    return render(request, 'users/register.html', {'form': form})

def index(request):
    return render(request, 'users/index.html')