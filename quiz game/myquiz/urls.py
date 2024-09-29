from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from myquiz import views as index_views
from rest_framework.urlpatterns import format_suffix_patterns
from quizapi import views

urlpatterns = [
	path(r'', index_views.index),
	path(r'login/', index_views.login),
	path(r'questions/', include('quiz.urls')),
	path(r'quizapi/', views.QuizApiList.as_view()),
    path(r'admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)