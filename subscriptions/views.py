from django.shortcuts import render
from django.http import JsonResponse
from .forms import EmailForm
from .tasks import send_welcome_email  

def subscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
           
            send_welcome_email.delay(email)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = EmailForm()
    return render(request, 'subscriptions/subscribe.html', {'form': form})