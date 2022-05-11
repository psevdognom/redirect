from django.urls import path

from links.views import CreateLinkView

urlpatterns = [
    path('create/', CreateLinkView.as_view(), name='create_link'),
]