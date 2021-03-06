from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path('members/', include('members.urls')),
    path('events/', include('events.urls')),
    path('blog/', include('blog.urls')),
    path('', IndexView.as_view(),
        name='index'),
]