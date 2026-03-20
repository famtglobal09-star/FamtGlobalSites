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


def home(request):
    form = CallbackForm()

    if request.method == "POST":
        form = CallbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We will reach you shortly.")
            return redirect('home')  # use URL name if possible

    return render(request, 'website/base.html', {'form': form})

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
def contact(request):
    return render(request,'website/contact.html')
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