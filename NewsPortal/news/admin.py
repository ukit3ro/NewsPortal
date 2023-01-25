from django.contrib import admin
from .models import Comment, Author, Category, PostCategory, Rating, Post
# Register your models here.
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Post)
admin.site.register(Rating)