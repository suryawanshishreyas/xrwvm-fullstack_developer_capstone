# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from yourapp.views import IndexView

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration

    # path for login
    # path(route='login', view=views.login_user, name='login'),
    path('about/', TemplateView.as_view(template_name="About.html")),
    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
