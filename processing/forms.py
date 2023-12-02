from django import forms

# Create your forms here.


class InputForm(forms.Form):
    url = forms.CharField()
