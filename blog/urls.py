from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post2/<int:pk>/', views.post_detail2, name='post_detail2'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        # グラフ描画
    path('plot/', views.get_svg, name='plot'),
    # path('test/', views.viewFunction, name='test'),
]
