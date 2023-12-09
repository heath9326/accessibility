from django.db import models


class Input(models.Model):
    input_text = models.CharField(max_length=250)

    def __str__(self):
        return self.input_text


class Url(models.Model):
    url = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.url


class Report(models.Model):
    pass