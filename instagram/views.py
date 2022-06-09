from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Image,User,Profile
from .forms import NewImageForm,NewProfileForm
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
@login_required(login_url="/accounts/login/")
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = NewProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        profile_form = NewProfileForm()
    return render(request, 'new_profile.html', {"profile_form": profile_form,})
def search_profiles(request):
    if 'profiles' in request.GET and request.GET['profiles']:
        search_term=request.GET.get('profiles')
        user=User.objects.filter(username=search_term)
        print(user)
        profiles=Profile.objects.filter(user=user)
        print(profiles)
        message=f'{search_term}'

        return render(request,'search.html',{"message":message,"profiles":profiles,})

    else:
        message='You Havent searched for any term'

        return render(request, 'search.html',{"message":message},)
