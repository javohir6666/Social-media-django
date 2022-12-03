from django.urls import path
from .views import PostListView, PostDetailView, PostEditView,PostDeleteView,CommentDeleteView,ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, Dislike,UserSearch,ListFollowers,CommentAddLike,CommentDislike,CommentReplyView
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
#Comment
    path(f'post/<int:post_pk>/comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete'),
    path(f'post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
#Like & Dislike
    path(f'post/<int:pk>/like', AddLike.as_view(), name='like'),
    path(f'post/<int:pk>/dislike', Dislike.as_view(), name='dislike'),
    path(f'post/<int:post_pk>/comment/<int:pk>/like', CommentAddLike.as_view(), name='comment-like'),
    path(f'post/<int:post_pk>/comment/<int:pk>/dislike', CommentDislike.as_view(), name='comment-dislike'),
#Profile
    path(f'profile/<int:pk>',ProfileView.as_view(), name='profile'),
    path(f'profile/edit/<int:pk>',ProfileEditView.as_view(), name='profile-edit'),
#Follower
    path(f'profile/<int:pk>/followers/add',AddFollower.as_view(), name='add-follower'),
    path(f'profile/<int:pk>/followers/list', ListFollowers.as_view(), name='list-followers'),
    path(f'profile/<int:pk>/followers/remove',RemoveFollower.as_view(), name='remove-follower'),
#search
    path('search/', UserSearch.as_view(), name='profile-search'),
]