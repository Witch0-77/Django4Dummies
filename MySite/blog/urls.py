from django.urls import path, include
from . import views
app_name = 'blog'

urlpatterns = [
# widoki posta
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('blog/', include('blog.urls', namespace='blog')),

]