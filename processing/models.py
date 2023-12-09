from django.db import models


class Input(models.Model):
    input_text = models.CharField(max_length=250)

    def __str__(self):
        return self.input_text


class Url(models.Model):
    url = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.url


class AItem(models.Model):
    element = models.TextField()
    url = models.ForeignKey(Url, on_delete=models.CASCADE)

    def __str__(self):
        return f"An element of type <a> of url: {self.url}"


class Report(models.Model):
    pass