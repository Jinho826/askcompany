# 로그인 성공 실패, 메세지 커스텀해보기 성공

# from django.shortcuts import render
# from django.contrib.auth.views import LoginView
# from django.conf import settings
# from django.contrib import messages
# from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy

# class LoginCustom(LoginView):
#     template_name='accounts/login_form.html'

#     def dispatch(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             if self.redirect_authenticated_user and self.request.user.is_authenticated:
#                 redirect_to = self.get_success_url()
#                 if redirect_to == self.request.path:
#                     raise ValueError(
#                         "Redirection loop for authenticated user detected. Check that "
#                         "your LOGIN_REDIRECT_URL doesn't point to a login page."
#                     )
#                 return HttpResponseRedirect(redirect_to)
#             elif self.redirect_authenticated_user != self.request.user.is_authenticated:
#                 messages.error(self.request, '로그인 실패')
#         return super().dispatch(request, *args, **kwargs)
    
#     def get_success_url(self):
#         url = self.get_redirect_url()
#         messages.success(self.request, '로그인 성공')


# account_login = LoginCustom.as_view()


from urllib import response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


from accounts.forms import ProfileForm
from accounts.models import Profile

from django.contrib.auth import get_user_model, login as auth_login
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

@login_required
def profile_edit(request):
    print(request.user.profile)
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })

User = get_user_model()

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/signup_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        return response


signup = SignupView.as_view()


