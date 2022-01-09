from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
	 PasswordResetView,
	 PasswordResetDoneView, 
	 PasswordResetConfirmView,
	 PasswordResetCompleteView
 )
from authorize.views import (
	login,
	signup,
	post_login,
	activate
)

urlpatterns = [
	path(r'reset-password/done/', PasswordResetDoneView.as_view(),
		{"template_name":"registration/reset_password_done.html"},
		name='password_reset_done'),		
	path(r'reset-password/',PasswordResetView.as_view(),
		{ "template_name":"registration/password_reset_form.html",
		"post_reset_redirect":"authorize:password_reset_done",
		"html_email_template_name": "registration/password_reset_email.html"},
		 name='reset_password'),
	re_path(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
		PasswordResetConfirmView.as_view(),
		{"post_reset_redirect":"authorize:password_reset_complete",
		"template_name":"registration/reset_password_confirm.html"}, 
		name='password_reset_confirm' ),
	path(r'reset-password/complete/', PasswordResetCompleteView.as_view(),
		{"template_name":"registration/reset_password_complete.html"},
		name="password_reset_complete"),
	path(r'verification/', activate, name='activation'),
	path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
	path(r'login/', login, name="login"),
	path(r'post/login/', post_login, name ='post_login'),
	path(r'signup/', signup, name="signup")
]





