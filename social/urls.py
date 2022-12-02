from django.urls import path
from .views import PostListView, PostDetailView, PostEditView,PostDeleteView,CommentDeleteView,ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, Dislike

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
#Comment
    path(f'post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
#Like
    path(f'post/<int:pk>/like', AddLike.as_view(), name='like'),
    path(f'post/<int:pk>/dislike', Dislike.as_view(), name='dislike'),
#Profile
    path(f'profile/<int:pk>',ProfileView.as_view(), name='profile'),
    path(f'profile/edit/<int:pk>',ProfileEditView.as_view(), name='profile-edit'),
#Follower
    path(f'profile/<int:pk>/followers/add',AddFollower.as_view(), name='add-follower'),
    path(f'profile/<int:pk>/followers/remove',RemoveFollower.as_view(), name='remove-follower'),
]