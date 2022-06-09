from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,User,Profile
from .forms import NewImageForm
# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    
    images=Image.objects.all()
    return render(request,'index.html',{'images':images,})

@login_required(login_url='/accounts/login/')
def newimage(request):
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
    return render(request, 'image.html', {"form": form})
def profile(request):
    profiles=Profile.objects.filter(user=request.user.id)
    images=Image.objects.filter(user=request.user.id)
    return render (request,'profile.html',{'images':images,'profiles':profiles,})
