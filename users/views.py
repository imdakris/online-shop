from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from carts.models import Cart


from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    """
    Handle user login.

    If the request method is POST, validate the login form.
    If the form is valid, authenticate the user, log them in, and update the user's cart.
    Redirect to the next page if provided, otherwise redirect to the index page.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - HttpResponseRedirect: Redirect to the specified page after successful login.
        - render: Render the login page with the login form.
    """
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get("next"))
                
                return HttpResponseRedirect(reverse("main:index"))
            
            if not user:
                messages.error(request, "Неверное имя пользователя или пароль. Попробуйте снова.")
    else:
        form = UserLoginForm()

    context = {"title": "Home - Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    """
    Handle user registration.

    If the request method is POST, validate the registration form.
    If the form is valid, save the user, log them in, update the user's cart, and redirect to the index page.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - HttpResponseRedirect: Redirect to the index page after successful registration.
        - render: Render the registration page with the registration form.
    """
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, Вы успешно зарегистрированы. Добро пожаловать!")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()
    context = {"title": "Home - Регистрация", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    """
    Display and handle updates to the user profile.

    If the request method is POST, validate the profile form and update the user profile.
    If the form is valid, display a success message and redirect to the profile page.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - HttpResponseRedirect: Redirect to the profile page after successful profile update.
        - render: Render the profile page with the profile form.
    """
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлён")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {"title": "Home - Кабинет", "form": form}

    return render(request, "users/profile.html", context)


def users_cart(request):
    """
    Display the user's cart page.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - render: Render the user's cart page.
    """
    return render(request, "users/users_cart.html")


@login_required
def logout(request):
    """
    Log the user out, display a logout message, and redirect to the index page.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - redirect: Redirect to the index page after successful logout.
    """
    messages.success(request, f"{request.user.username} Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse("main:index"))
