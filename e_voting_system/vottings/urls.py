from django.urls import path
from . import views

urlpatterns = [
    path('vote/', views.vote_page, name='vote_page'),
    path('results/', views.results_page, name='results'),
    path('candidates/', views.candidates_page, name='candidates'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
