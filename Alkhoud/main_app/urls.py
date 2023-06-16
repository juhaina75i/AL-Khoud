from . import views
from django.urls import path

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/',views.search_page,name='search_page'),
    path('Clubs/add-club/', views.add_club, name='add_club'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('clubs/',views.clubs,name='clubs'),
    path('club_home/',views.club_home,name='club_home'),
    path('add_package/',views.add_package,name='add_package'),
    path('add_coach/',views.add_coach,name='add_coach'),
    path('add_tournament/',views.add_tournament,name='add_tournament'),
    path('add_ad/',views.add_ad,name='add_ad'),
    path('clube_tournament/',views.clube_tournament,name='clube_tournament'),
    path('clube_subscriper/',views.clube_subscriper,name='clube_subscriper'),
    path('tournament_sbscriper/',views.tournament_sbscriper,name='tournament_sbscriper'),
    path('club_coach/',views.club_coach,name='club_coach'),
    path('clube_packages/',views.clube_packages,name='clube_packages'),
    path('club_ad/',views.club_ad,name='club_ad'),
    path('Offers/add-offer/', views.add_offer, name='add_offer'),
    path('Packges/add-package/', views.add_package, name='add_package'),
    path('Subscribers/add-subscriber/', views.add_subscriber, name='add_subscriber'),
    path('Coaches/add-coach/', views.add_coach, name='add_coach'),
    path('Tournaments/add-tournament/', views.add_tournament, name='add_tournament'),
    path('payment/', views.payment_page, name='payment_page'),
    path('Clubs/details/<club_id>', views.club_details, name='club_details'),
    path("Clubs/<club_id>/review/add/", views.add_review, name="add_review"),

   
]