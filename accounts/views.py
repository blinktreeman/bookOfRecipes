from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, ProfileEditForm

from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


def register(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = SignupForm()
        return render(request,
                      'registration/register.html',
                      {'user_form': user_form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         profile_form = ProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)
#         if profile_form.is_valid():
#             profile_form.save()
#     else:
#         profile_form = ProfileEditForm(instance=request.user)
#         return render(request,
#                       'registration/edit_profile.html',
#                       {'profile_form': profile_form})


class EditUserProfile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'registration/edit_profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile')
    success_message = 'User data has been changed'
    user_id = None

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
