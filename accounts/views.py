from django.shortcuts import render


def sign_in(request):
    return render(request, "accounts/sign-in.html")

def sign_up(request):
    return render(request, "accounts/sign-up.html")