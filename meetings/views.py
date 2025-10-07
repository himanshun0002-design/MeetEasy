from django.shortcuts import render

# Create your views here.


# meetings/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

CustomUser = get_user_model()


# Homepage view
def homepage(request):
    """
    Renders the homepage with user's display info.
    """
    if request.user.is_authenticated:
        user_email = request.user.email
        full_name = request.user.full_name
    else:
        user_email = None
        full_name = None

    context = {
        "user_email": user_email,
        "full_name": full_name,
    }
    return render(request, "home.html", context)


from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        error = None

        if not full_name or not email or not password or not confirm_password:
            error = "All fields are required."
        elif password != confirm_password:
            error = "Passwords do not match."
        elif CustomUser.objects.filter(email=email).exists():
            error = "Email already registered."

        if error:
            return render(request, "signup.html", {"error": error, "form": request.POST})

        user = CustomUser.objects.create_user(email=email, full_name=full_name, password=password)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "signup.html")



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email").strip()
        password = request.POST.get("password")

        if not email or not password:
            return render(request, "login.html", {"error": "Please enter email and password."})

        user = authenticate(request, username=email, password=password)  # username=email because of custom user
        if user is not None:
            auth_login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid email or password."})

    return render(request, "login.html")
