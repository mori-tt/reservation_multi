from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm
# from accounts.forms import CusSignupUserForm
from django.shortcuts import render, redirect
from allauth.account import views
from app.models import Staff, Booking
from django.utils import timezone


# スタッフサインアップビュー
class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm


# カスタマーサインアップビュー
# class CusSignupView(views.SignupView):
#         template_name = 'accounts/cus_signup.html'
#         form_class = CusSignupUserForm



# スタッフログインビュー
class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

# カスタマーログインビュー
# class CusLoginView(views.LoginView):
#     template_name = 'accounts/cus_login.html'

#     def form_valid(self, form):
#         super().form_valid(form)
#         if self.request.user.user_type == '0':  # カスタマー
#             return redirect('store')
#         else:
#             return redirect('cus_login')

# ログアウトビュー
class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        staff_data = Staff.objects.get(user=user_data)
        booking_data = Booking.objects.filter(staff=staff_data, start__gte=timezone.now())
        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            'staff_data': staff_data,
            'booking_data': booking_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'description': user_data.description,
                'image': user_data.image
            }
        )
        return render(request, 'accounts/profile_edit.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.description = form.cleaned_data['description']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })