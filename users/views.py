from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Wow! Account created for {username}!')
        return redirect('events')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})



