from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .models import Profile
from discussion.models import Discussions, DiscussionComments


# Create your views here.

def login_user(request):
    if request.method == "GET":
        loginForm = LoginForm()
        return render(request, 'login.html', {'form': loginForm})
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid user name or password', extra_tags="danger")
            return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.email = form.cleaned_data.get('email')
            # user.profile.realname = form.cleaned_data.get('realname')
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token, backend='django.core.mail.backends.console.EmailBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user, backend='django.core.mail.backends.console.EmailBackend')
        return redirect('profile')
    else:
        return render(request, 'account_activation_invalid.html')


@login_required
def profile(request):
    return render(request, 'profile_page.html')


@login_required
def profile_info(request, id):
    user = User.objects.get(pk=id)
    user_discussions = user.discussions_set.values_list('id', flat=True).all()
    comment_discussions = user.discussioncomments_set.values_list('discussion_id', flat=True).all()
    user_discussions = user_discussions.union(comment_discussions)
    discussions = Discussions.objects.filter(pk__in=user_discussions)
    friends = user.req_from.filter(is_accepted=1)
    return render(request, 'profile_info.html', {'user': user, 'discussions': discussions, 'friends': friends})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            profile = form.save()
            profile.refresh_from_db()  # load the profile instance created by the signal
            request.user.profile = profile
            return redirect('profile')

    else:
        form = EditProfileForm(instance=Profile.objects.get(user=request.user))
    return render(request, 'edit_profile.html', {'form': form})
