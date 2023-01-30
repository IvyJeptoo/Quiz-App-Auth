from django.urls import path
from .views import TeacherSignupView, StudentSignupView,CustomAuthToken, LogoutView, TeacherOnlyView, StudentOnlyView


urlpatterns=[
    path('signup/teacher/', TeacherSignupView.as_view()),
    path('signup/student/', StudentSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('teacher/dashboard/', TeacherOnlyView.as_view(), name='teacher-dashboard' ),
    path('student/dashboard/', StudentOnlyView.as_view(), name='student-dashboard')


]