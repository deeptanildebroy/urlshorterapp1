from django.db import models
from django.contrib.auth.models import User
from .utils import generate_short_url

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url_slug = models.SlugField(max_length=10, unique=True,null=False)
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)
    referral_sources = models.TextField(blank=True)

# Created a custom save method to generate a short url and then add that short url to the database
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_url(self.original_url)
            #To create more uniqueness
            while URL.objects.filter(short_url=self.short_url).exists():
                self.short_url = generate_short_url(self.original_url, length=len(self.short_url) + 1)
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.short_url
