from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from .forms import EmailForm
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipients = [email.strip() for email in form.cleaned_data['recipients'].split(',')]
            subject = form.cleaned_data['name']
            message = form.cleaned_data['message']
            attachments = request.FILES.getlist('attach')

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=recipients,
            )

            for attachment in attachments:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            email.send(fail_silently=False)

            return redirect('email_success')
    else:
        form = EmailForm()
    
    return render(request, 'email_form.html', {'form': form})

def email_success(request):
    return render(request, 'email_success.html')
