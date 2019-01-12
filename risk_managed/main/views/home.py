from django.shortcuts import redirect, render


def view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    return render(request, "main/home.html")
