from django import forms
from multiupload.fields import MultiFileField

class EmailForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    recipients = forms.CharField(label='To', widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
    attach = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 5)
