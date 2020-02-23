from django import forms
from django.core import validators

def checkforz(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("First value isn't z")

class FormName(forms.Form):
    Name = forms.CharField(validators=[checkforz])
    Email = forms.EmailField()
    verify_email = forms.CharField(label="Enter email again:")
    Text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0, message="not doing right")])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA")
    #     return botcatcher

    def clean(self):
        clean_alldata= super().clean()

        email = clean_alldata['Email']
        vmail = clean_alldata['verify_email']

        if email != vmail:
            raise forms.ValidationError("check your email again") 
