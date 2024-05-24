from django import forms
from .models import URL

class URLForm(forms.ModelForm):

    url_slug = forms.SlugField(
        label= 'Enter a Title'
    )
    original_url = forms.URLField(
        label='Enter the Original URL', 
    )
    class Meta:
        model = URL
        fields = ['url_slug','original_url']