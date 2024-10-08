from django.urls import path

from apps.booking.views.views import ApartmentCreateView, ApartmentListView,ApartmentUpdateView,ApartmentChangeActiveView

urlpatterns = [
    path('create/', ApartmentCreateView.as_view(), name='create'), #http://127.0.0.1:8000/apartments/create/ (post) создание записей
    path('get_apartments/', ApartmentListView.as_view(), name='get_apartment'), #http://127.0.0.1:8000/apartments/get_apartments/ (get) only available houses
    path('get_apartments/<int:pk>/', ApartmentListView.as_view()), #http://127.0.0.1:8000/apartments/get_apartments/1/ wird erste id aus db angezeigt
    path('update_apartments/<int:pk>/', ApartmentUpdateView.as_view(), name='put_apartment'),#http://127.0.0.1:8000/apartments/update_apartments/3/ Updeten von Zimmer straßen ect..
    path('delete_apartments/<int:pk>/',ApartmentUpdateView.as_view(), name='put_apartment'),#http://127.0.0.1:8000/apartments/delete_apartments/1/ Anzeige löschen
    path('change_active/<int:pk>/', ApartmentChangeActiveView.as_view(), name='change_active'),#http://127.0.0.1:8000/apartments/change_active/1/ Die Anzeige auf active stellen oder unactive
]