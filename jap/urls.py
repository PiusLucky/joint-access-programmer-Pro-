from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include
from django.contrib.sitemaps.views import sitemap
from central.sitemaps import PostSitemap
from django.conf.urls import handler500
from central import views as central
sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
	path('admin/', admin.site.urls),
	path(r'', include(('central.urls', 'central'), namespace='central')),
	path(r'auth/', include(('authorize.urls', 'authorize'), namespace='authorize')),
	path('accounts/', include('django.contrib.auth.urls')),
  path(r'froala_editor/', include('froala_editor.urls')),
  path(r'robots.txt/', include('robots.urls')),
  path(r'robots.txt', include('robots.urls')),
  path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
       name='django.contrib.sitemaps.views.sitemap'),
  path('', include('pwa.urls'))
]

handler500 = central.error_500

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

admin.site.site_header = 'JAP Administrator@Pius_Lucky'
admin.site.site_title = 'JAP Administrator@Pius_Lucky'


"https://joint-access-programmer.com/.well-known/brave-rewards-verification.txt"



