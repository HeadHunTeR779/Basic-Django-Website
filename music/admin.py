from django.contrib import admin
from .models import Album            # dot for current note that directly "from models" wont work probably cuz he said __ini__.py file required to make it a package

admin.site.register(Album)