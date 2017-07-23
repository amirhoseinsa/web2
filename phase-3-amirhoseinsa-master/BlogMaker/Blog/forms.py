from django import forms


class Form_AddP(forms.Form):
    title = forms.CharField(max_length=150)
    summary = forms.CharField(max_length=150)
    text = forms.CharField(max_length=300)


class Form_AddC(forms.Form):
    text = forms.CharField(max_length=150)
    post_id = forms.IntegerField()
