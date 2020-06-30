from central.models import Post
from django.contrib.sitemaps import Sitemap

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    def items(self):
    	verified_posts = Post.objects.filter(draft=False).all()
    	return verified_posts
    def lastmod(self, obj):
        return obj.last_updated
