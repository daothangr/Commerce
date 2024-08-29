from django.contrib import admin
from .models import AuctionList, User, Link, Comment

# Register your models here.
admin.site.register(AuctionList)
admin.site.register(Link)
admin.site.register(User)
admin.site.register(Comment)



