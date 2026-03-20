"""
URL configuration for consulting_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from website import sitemaps
from website.sitemaps import StaticViewSitemap

from website import views
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', views.home, name='home'),
     path('', views.home, name='home'),
    path('about/', views.about, name='about'),    
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms, name='terms'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    # Detailed Finance Services
   path('services/bookkeeping/', views.bookkeeping,name='bookkeeping'),   
   path('services/itin/', views.itin,name='itin'),
   path('services/cpa-letter/', views.cpa_letter,name='cpa_letter'),
   path('services/tax-filing/', views.tax_filing,name='tax_filing'),
   path('services/finance-solutions/', views.finance_solutions,name='finance_solutions'),
   path('services/finance-analysis/', views.finance_analysis,name='finance_analysis'),
   path('services/us-incorporation/', views.incorporation, name='incorporation'),
   path('who_we_help/', views.who_we_help, name='who_we_help'),
   path('payroll/', views.payroll, name='payroll'),
    path('management/', views.management, name='management'),
  
    

    path('robots.txt', views.robots_txt, name='robots_txt'),
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
     

   

    # Resources
 

]
