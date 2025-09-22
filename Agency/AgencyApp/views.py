from django.shortcuts import render, redirect, get_object_or_404

from AgencyApp.forms import RealEstateForm
from AgencyApp.models import RealEstate


# Create your views here.
def index(request):
    houses = RealEstate.objects.filter(sold=False, surface__gte=100).all()
    return render(request, 'index.html', {'houses': houses})

def edit(request, id):
    house = get_object_or_404(RealEstate, id=id)
    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES)
        if form.is_valid():
            house = form.save(commit=False)
            house.save()
        return redirect('index')

    form = RealEstateForm()
    return render(request, 'edit.html', {'form': form, 'house': house})
