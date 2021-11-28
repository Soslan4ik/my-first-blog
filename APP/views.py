from django.shortcuts import render
from .models import Articles

# Create your views here.
def index(request):
    products = Articles.objects.all()
    return render(request, 'APP/html/index.html', {'products': products})
    
    a = FB(name = request.POST['name_fb'], phone = request.POST['phone_fb'])
    a.save()
    return HttpResponseRedirect(reverse('index'))