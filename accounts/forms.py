from django import forms
from allauth.account.forms import SignupForm

class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    description = forms.CharField(label='備考', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False, )

# スタッフサインアップ
class SignupUserForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    def save(self, request, commit=True):
        user = super().save(request) 
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

# カスタマーサインアップ
# class CusSignupUserForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='姓')
#     last_name = forms.CharField(max_length=30, label='名')
#     def save(self, request, commit=True):
#         user = super().save(request) 
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.user_type = '0'  # カスタマー
#         if commit:
#             user.save()
#         return user

