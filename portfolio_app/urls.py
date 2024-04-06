from django.urls import path
from .views import SkillList, SkillDetail, SkillCreate, SkillUpdate, SkillDelete, SkillLogin, SkillSignUp
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', SkillList.as_view(), name='skills'),
    path('skill/<int:pk>/', SkillDetail.as_view(), name='skill'),
    path('skill-create/', SkillCreate.as_view(), name='skill-create'),
    path('skill-update/<int:pk>/', SkillUpdate.as_view(), name='skill-update'),
    path('skill-delete/<int:pk>/', SkillDelete.as_view(), name='skill-delete'),
    path('login/', SkillLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SkillSignUp.as_view(), name='signup'),
]