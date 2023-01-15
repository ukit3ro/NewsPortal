from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import *

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=255, null=True)

#дописать, тут должен быть рейтинг пользователя

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

post = 'POST'
news = 'NEWS'
POSITIONS = [
    (post, 'Пост'),
    (news, 'Новость')
]
class Post(models.Model):
    post = 'POST'
    news = 'NEWS'

    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='PostCategory', related_name='post_category')
    article = models.CharField(max_length=255)
    _text = models.TextField(db_column='amount')
    posttype = models.CharField(max_length=4, choices=POSITIONS, default=post)
    rates = models.ManyToManyField(User, through='Rating', blank=True)

    #методы данной модели
    def post_time(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return(self.time_out - self.time_in).total_seconds()
        else:
            return(datetime.now() - self.time_in).total_seconds()

    def preview(self):
        return self._text[0:125]


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comment_author', on_delete=models.CASCADE)
    comment_text = models.TextField()
    rates = models.ManyToManyField(User, through='Rating')

    def comment_time(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:
            return(self.time_out - self.time_in).total_seconds()
        else:
            return(datetime.now() - self.time_in).total_seconds()

class Rating(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(-1.0), MaxValueValidator(1.0)])
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    _comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
