from django.shortcuts import render
from .models import Oil_Company, Pumps, Readings

def admin_dashboard(request):
    context = {
        'total_oilcompanies': Oil_Company.objects.count(),
        'total_pumps': Pumps.objects.count(),
        'total_readings': Readings.objects.count(),
    }
    return render(request, 'admin_dashboard.html', context)
