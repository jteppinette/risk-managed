from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from risk_managed.models import Host


@login_required
def view(request):
    if hasattr(request.user, "administrator"):
        return render(
            request,
            "dashboard.html",
            {"hosts": Host.objects.filter(administrator=request.user.administrator)},
        )

    return render(request, "dashboard.html")
