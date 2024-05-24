from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import URL
from .forms import URLForm

@login_required
def home(request):
    if request.method == 'POST': 
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user if request.user.is_authenticated else None
            url.save()
            messages.success(request, 'Short URL created successfully!')
            return redirect('dashboard')
    else:
        form = URLForm()
    return render(request, 'home.html', {'form': form})

def redirect_url(request, short_url):
    
    url = get_object_or_404(URL, short_url=short_url)
    url.clicks += 1

    referral_source = request.META.get('HTTP_REFERER', '')
    if referral_source:
        if url.referral_sources:
            url.referral_sources += f"\n{referral_source}"
        else:
            url.referral_sources = referral_source
            
    url.save()
    return redirect(url.original_url)

def redirect_slug(request,url_slug):
    
    url = get_object_or_404(URL,url_slug=url_slug)
    url.clicks += 1

    referral_source = request.META.get('HTTP_REFERER', '')
    if referral_source:
        if url.referral_sources:
            url.referral_sources += f"\n{referral_source}"
        else:
            url.referral_sources = referral_source
            
    url.save()
    return redirect(url.original_url)

@login_required
def dashboard(request):
    urls = URL.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'urls': urls,'username': request.user.username})

@login_required
def delete_url(request, url_id):
    url = get_object_or_404(URL, id=url_id)
    if url.user == request.user:
        url.delete()
    return redirect('dashboard')