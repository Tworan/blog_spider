import datetime
from django import db
from django.db import models


# def make_table_name(model_class):
#     model_name = model_class
#     return model_name.lower() + '-' + str(datetime.date.today())


# Create your models here.

class BlogUser(models.Model):
    user_name = models.CharField(verbose_name="user_name", max_length=20, null=False)
    verified_reason = models.CharField(verbose_name="verified_reason", max_length=100, null=False)
    follows_counts = models.CharField(verbose_name="follows_counts", max_length=10, null=False)
    description = models.CharField(verbose_name="description", max_length=100, null=False)
    potential_followings = models.CharField(verbose_name='potential_followings', max_length=200, null=False)
    text = models.CharField(verbose_name='text', max_length=10000, null=False)

    class Meta:
        db_table = 'bloguser' + '_' + str(datetime.date.today()).replace('-', '_')

    def __str__(self):
        return self.blog_user_name, self.verified_reason, self.follows_counts, self.description, self.potential_followings


class Activation(models.Model):
    text = models.CharField(verbose_name="text", max_length=10000, null=False, unique=True)

    def __str__(self):
        return self.text


class HotBoard(models.Model):
    hot_board = models.CharField(verbose_name="hot_board", max_length=10000)
    plat = models.CharField(verbose_name="plat", max_length=20)

    class Meta:
        db_table = 'hotboard'

    def __str__(self):
        return self.hot_board, self.plat


class User(models.Model):
    User_name = models.CharField(verbose_name="user_name", max_length=20)
    User_passwd = models.CharField(verbose_name="user_passwd", max_length=20)
    Subscribings = models.CharField(verbose_name="Subscribings", max_length=200)


    def __str__(self):
        return self.User_name, self.User_passwd


class PlatToBlog_following(models.Model):
    uid = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    BlogUid = models.ForeignKey(BlogUser, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.uid, self.BlogUid


class PlatToBlog_potential(models.Model):
    uid = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
    BlogUid = models.ForeignKey(BlogUser, to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.uid, self.BlogUid


class BlogUserToAct(models.Model):
    uid = models.ForeignKey(BlogUser, to_field="id", on_delete=models.CASCADE)
    text = models.ForeignKey(Activation, to_field="text", on_delete=models.CASCADE)

    def __str__(self):
        return self.uid, self.text


class BlogUserAll(models.Model):
    name = models.CharField(verbose_name="name", max_length=40)

    class Meta:
        db_table = 'bloguserall'

    def __str__(self):
        return self.name
