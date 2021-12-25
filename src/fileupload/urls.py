from django.urls import path
from .views import UploadFileView, HomeView, CompareView

app_name = "fileupload"

urlpatterns = [
    path('', HomeView.as_view(title="Accueil"), name="home"),
    path('compare', CompareView.as_view(title="Comparaison"), name="compare"),
    path('upload/', UploadFileView.as_view(), name='file-upload'),
]