from django.urls import path
from .views import courses,detail_courses

urlpatterns = [
    path('courses/', courses, name="courses"),
    path('detail_courses/<int:id>/', detail_courses, name="detail_courses"),

]