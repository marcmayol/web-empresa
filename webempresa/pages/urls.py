from django.urls import path
from . import views
urlpatterns = [
    path('<page_title>',views.page,name="page")
]