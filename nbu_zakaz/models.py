from django.db import models


class Client(models.Model):
    chat_id = models.IntegerField()
    user_name = models.CharField(max_length=150)
    settings = models.JSONField()
    last_viewed = models.CharField(max_length=300)


class Nbu_parser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    kyku_draiver = models.FileField()
    poshuk_monetu = models.TextField()
    cart_scrinshot = models.FileField()






