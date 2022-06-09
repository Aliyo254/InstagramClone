from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,User
from .forms import NewImageForm
# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    
    images=Image.objects.all()
    return render(request,'index.html',{'images':images,})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})
