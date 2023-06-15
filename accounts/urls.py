from django.urls  import path, include
from .views.fbv_views import register, edit

urlpatterns = [
   path('', include('django.contrib.auth.urls')),
   path('register/', view=register, name='register'),
   path('edit/', view=edit, name='edit'),
]