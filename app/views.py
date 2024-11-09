from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import MyUser, Gift

def check_user_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return MyUser.objects.get(id=user_id)
        except MyUser.DoesNotExist:
            pass
    return None

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        entered_password = request.POST.get('password')

        try:
            user = MyUser.objects.get(username=username)

            
            if user.password == entered_password:
                request.session['user_id'] = user.id
                request.session.set_expiry(300)  
                return redirect('gifts')  
            else:
                messages.error(request, 'Invalid username or password.')
        except MyUser.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'home.html')



def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if MyUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif MyUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            MyUser.objects.create(username=username, email=email, password=password)
            return redirect('home')
    return render(request, 'registration.html')

def users(request):
    current_user = check_user_session(request)
    if not current_user:
        return redirect('error')
    all_users = MyUser.objects.exclude(id=current_user.id)
    return render(request, 'users.html', {'users': all_users})

def gifts(request):
    current_user = check_user_session(request)
    if not current_user:
        return redirect('error')

    users = MyUser.objects.exclude(id=current_user.id)

    if request.method == 'POST':
        gift_name = request.POST.get('gift_name')
        Gift.objects.create(user=current_user, gift_name=gift_name)

    user_gifts = current_user.gifts.all()
    return render(request, 'gifts.html', {'gifts': user_gifts, 'users': users, 'user': current_user})


def other_users_gifts(request, user_id):
  current_user = check_user_session(request)
  if not current_user:
      return redirect('error')

  try:
      other_user = MyUser.objects.get(id=user_id)
      gifts = other_user.gifts.all()
      return render(request, 'other_users_gifts.html', {'gifts': gifts, 'other_user': other_user})
  except MyUser.DoesNotExist:
      return redirect('error')

def login_view(request):
  if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = MyUser.objects.filter(username=username, password=password).first()

      if user:
          request.session['user_id'] = user.id
          request.session['last_activity'] = timezone.now().isoformat()
          return redirect('home')  
      else:
          pass

  return render(request, 'login.html')


def error(request):
    return render(request, 'error.html')
