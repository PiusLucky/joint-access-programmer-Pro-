from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from central.views import (
    landing_page, categories, user_interface, backend, algorithm, freebies,
    premium, tips, article_detail, terms_of_service, privacy_policy, cookies_policy, 
    contact, about, post_contact, post_emaillist, search, brave_rewards
)



urlpatterns = [
    path(r'', landing_page, name="landing_page"),
    path(r'categories/', categories, name="categories"),
    path(r'user-interface/', user_interface, name="user_interface"),
    path(r'backend/', backend, name="backend"),
    path(r'algorithm/', algorithm, name="algorithm"),
    path(r'freebies/', freebies, name="freebies"),
    path(r'premium/', premium, name="premium"),
    path(r'tips/', tips, name="tips"),
    path(r'terms-of-service/', terms_of_service, name="terms_of_service"),
    path(r'privacy-policy/', privacy_policy, name="privacy_policy"),
    path(r'cookies-policy/', cookies_policy, name="cookies_policy"),
    path(r'contact/', contact, name="contact"),
    path(r'about/', about, name="about"),
    path(r'post/contact/', post_contact, name="post_contact"),
    path(r'post/email/', post_emaillist, name="post_emaillist"),
    path(r'search/', search, name="search"),
    re_path(r'^(?P<slug>[-\w]+)/$', article_detail, name='article_detail'),
    path(r'.well-known/brave-rewards-verification.txt', brave_rewards, name="brave_rewards"),    
]

