from django import forms


class Form_login(forms.Form):
    un = forms.CharField(label='', max_length=50,
                         widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class Form_SignUp(forms.Form):
    un = forms.CharField(label='', max_length=50,
                         widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    fn = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    ln = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))


class Form_test(forms.Form):
    post_id = forms.IntegerField()
    text = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
