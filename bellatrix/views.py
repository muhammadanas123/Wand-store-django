from django.shortcuts import render
from .models import WandVariety, Store
from django.shortcuts import get_object_or_404
from .forms import WandVarietyForm

# Create your views here.

def all_wand(request):
  wands = WandVariety.objects.all( )
  return render(request, 'bellatrix/all_wand.html', {'wands': wands})

def wand_detail(request, wand_id):
  wand = get_object_or_404(WandVariety, pk=wand_id)
  return render(request, 'bellatrix/wand_detail.html', {'wand': wand})

def wand_store_view(request):
  stores = None
  if request.method == 'POST':
    form = WandVarietyForm(request.POST)
    if form.is_valid():
      wand_variety = form.cleaned_data['wand_variety']
      stores = Store.objects.filter(wand_varieties=wand_variety)
  else:
    form = WandVarietyForm()
  return render(request, 'bellatrix/wand_stores.html', {'stores': stores, 'form': form})
