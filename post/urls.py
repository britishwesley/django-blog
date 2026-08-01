from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.all_posts, name='all_posts'),
    path('posts/new', views.create_post, name='create_post'),
    path("posts/<int:id>", views.single_post, name="single_post"),
    path("posts/<int:id>/edit", views.edit_post, name="edit_post"),
    path("posts/<int:id>/delete", views.delete_post, name="delete_post"),
    path("profile/", views.profile, name="profile")

    # path('posts/', views.logout, name='logout'),

    # path('posts/', views.login, name='login'),
    # path("posts/", admin.site.urls)
    

]