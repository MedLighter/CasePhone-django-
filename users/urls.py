from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users.views import login, registration, profile


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    
    # path('logout/', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
