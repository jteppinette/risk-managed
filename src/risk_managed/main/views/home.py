from django.shortcuts import render, redirect

def view(request):
    if request.user.is_authenticated():
        return redirect('dashboard')

    return render(request, 'home.html')
