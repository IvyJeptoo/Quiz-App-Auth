from django.urls import path
from .views import *


urlpatterns=[
    path('sign-up/teacher/', TeacherSignupView.as_view()),
    path('sign-up/student/', StudentSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list_create'),
    path('teacher/dashboard/', TeacherOnlyView.as_view(), name='teacher-dashboard' ),
    path('student/dashboard/', StudentOnlyView.as_view(), name='student-dashboard')


]