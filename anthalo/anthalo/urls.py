from django.contrib import admin
from django.urls import path
from crud import views #import views from crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.CrudListView.as_view()), #default to root
    path('<int:pk>', views.CrudDetailView.as_view()), #added path for detailed view
    path('new/', views.CrudCreateView.as_view()), #added path for "new"
    path('<int:pk>/update/', views.CrudUpdateView.as_view()), #added path for "update"
    path('<int:pk>/update_year/', views.CrudUpdateYearView.as_view()), #added path for "update year"
    path('<int:pk>/delete/', views.CrudDeleteView.as_view()), #added path for "delete"
]
