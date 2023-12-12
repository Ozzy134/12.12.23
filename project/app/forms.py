from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=False, min_length=5, max_length=15,
                           label='Ваше имя', help_text='fddfd',
                           widget=forms.TextInput(attrs={'class': 'myclass',
                            "placeholder": "Name", 'name': 'MyName'}))
    age = forms.IntegerField(min_value=1, max_value=100,
                             widget=forms.NumberInput(attrs={'class': 'myclass'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'myclass'}))

class VxodForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'myclass'}))
    password = forms.CharField(widget=forms.PasswordInput)

class Reg(forms.Form):
    name = forms.CharField(required=False, min_length=5, max_length=15,
                           label='Ваше имя',
                           widget=forms.TextInput(attrs={'class': 'myclass'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'myclass'}))
    password = forms.CharField(widget=forms.PasswordInput)