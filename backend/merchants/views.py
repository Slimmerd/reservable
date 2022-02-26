from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import RegisterUserForm, UserLoginForm


@require_POST
def registerMerchant(request):
    form = RegisterUserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return JsonResponse({'success': 'User registered'})
    else:
        return JsonResponse({'error': 'An error occurred during registration'})


@require_POST
@csrf_exempt
def loginMerchant(request):
    form = UserLoginForm(request.POST)
    if not form.is_valid():
        return JsonResponse({'error': 'Invalid credentials'})

    email = request.POST.get('email').lower()
    password = request.POST.get('password')

    try:
        user = User.objects.get(email=email)
    except:
        return JsonResponse({'error': 'User doesn\'t exist'})

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'success': 'authorised'})
    else:
        return JsonResponse({'error': 'Invalid credentials'})


@require_POST
def logOutMerchant(request):
    logout(request)
    return JsonResponse({'success': 'Logout'})
