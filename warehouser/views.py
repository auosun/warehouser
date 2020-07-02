from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

def indexView(request):
    views_name = "WAREHOUSE"
    return render(request, 'index.html', {"name":views_name})

@xframe_options_exempt
def p5View(request):
    return render(request,'p5.html',{})