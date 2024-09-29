from django.urls import path
import quiz.views as quiz_views

urlpatterns = [
	path(r'', quiz_views.qpage),
	
]
