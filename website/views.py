from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, redirect

from consulting_site.forms import CallbackForm


from django.contrib import messages
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'website/base.html')

def incorporation(request):
    return render(request,'website/incorporation.html')

def bookkeeping(request):
    return render(request,'website/bookkeeping.html')

def itin(request):
    return render(request,'website/itin.html')

def cpa_letter(request):
    return render(request,'website/cpa_letter.html')

def tax_filing(request):
    return render(request,'website/tax_filing.html')

def finance_solutions(request):
    return render(request,'website/finance_solutions.html')

def finance_analysis(request):
    return render(request,'website/finance_analysis.html')
def about(request):
    return render(request,'website/about.html')
def testimonials(request):
    return render(request,'website/testimonials.html')
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect



def contact(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)

        if form.is_valid():
            callback = form.save()

            # Send email notification to admin
            subject = f"New Callback Request from {callback.name}"
            message = f"""
You have received a new callback request:

Name: {callback.name}
Email: {callback.email}
Phone: {callback.phone}
Service: {callback.service}
Message: {callback.message}
"""
            admin_email = settings.DEFAULT_FROM_EMAIL  # or your team email
            recipient_list = ['subbutext999@gmail.com','admin@refundsuper.com']  # replace with your email

            send_mail(subject, message, admin_email, recipient_list, fail_silently=False)

            messages.success(request, "We got your request! A consultant will contact you soon.")
            return redirect('contact')

    else:
        form = CallbackForm()

    return render(request, 'website/contact.html', {'form': form})
def privacy_policy(request):
    return render(request,'website/privacy_policy.html')
def terms(request):
    return render(request,'website/terms.html')
def who_we_help(request):
    return render(request,'website/who_we_help.html')
def index(request):
    return render(request,'website/index.html')
def privacy_policy(request):
    return render(request,'website/privacy_policy.html')
def terms(request):
    return render(request,'website/terms.html')
def disclaimer(request):
    return render(request, 'website/disclaimer.html')
def payroll(request):
    return render(request, 'website/payroll.html')
def management(request):
    return render(request,'website/management.html')



from django.http import HttpResponse

def robots_txt(request):
    return HttpResponse(
        "User-agent: *\nAllow: /\nSitemap: https://famtglobal.com/sitemap.xml",
        content_type="text/plain"
    )