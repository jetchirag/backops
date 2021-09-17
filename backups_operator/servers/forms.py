from django import forms

from backups_operator.servers.models import AuthData, models

class SSHKeyForm(forms.ModelForm):
    
    class Meta:
        model = AuthData
        fields = ['name', 'ssh_key', 'ssh_key_passphrase']

        # widgets = {
        #   'name': forms.TextInput(attrs={
        #     'size': 50,
        #     'placeholder': "username@hostname, or leave blank to use key comment",
        #   }),
        #   'key': forms.Textarea(attrs={
        #     'cols': 72,
        #     'rows': 15,
        #     'placeholder': "Paste in the contents of your public key file here",
        #   }),
        # }