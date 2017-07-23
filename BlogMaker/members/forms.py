from django import forms


class SignIn(forms.Form):
    username = forms.CharField(label='', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignUp(forms.Form):
    username = forms.CharField(label='', max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))


class TestForm(forms.Form):
    post_id = forms.IntegerField()
    text = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
