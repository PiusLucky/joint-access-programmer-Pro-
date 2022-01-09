from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from central.formatChecker import ContentTypeRestrictedFileField
from froala_editor.fields import FroalaField
from central.utils import get_read_time
from django.db.models.signals import pre_save


class TagChoices(models.Model):
    tag_selection = (('------', '------'), ('ui_tag', 'UI tag'), 
                        ('bke_tag', 'Backend Tag'), ('algo_tag', 'Algorithm Tag'),
                        ('frb_tag', 'FreeProject Tag'), ('prm_tag', 'Premium Tag'),
                        ('tips_tag', 'Tips Tag'),
                        )
    tag = models.CharField(max_length=100, choices = tag_selection, default='------')
    def __str__(self):
        return (self.tag)
    class Meta:
        verbose_name = 'Tag Choices'
        verbose_name_plural = 'Tag Choices'


class Post(models.Model):
    badge_selection = (('------', '------'), ('python', 'Python'), 
                       ('javascript', 'Javascript'), ('all', 'All')
                      ) 
    category_selection = (('------', '------'), ('ui', 'UI/UX'), 
                          ('backend', 'Backend'), ('algorithm', 'Algorithm'),
                          ('freebies', 'Free Projects'), ('premium', 'Premium'),
                          ('video', 'Video'), ('tips_n_tricks', 'Tips & Tricks')
                         ) 
    category = models.CharField(max_length=100, choices = category_selection, default='------') 
    badges = models.CharField(max_length=100, choices = badge_selection, default='------') 
    tags = models.ManyToManyField(TagChoices, blank=False)
    title = models.CharField(max_length=60, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=True, null=True, help_text=""" 
          When django prepopulate slugs, it normally omits prepositions, do not forget
          to add it manually
        """)
    image = ContentTypeRestrictedFileField(upload_to= 'post_images/%Y/%m/%d/', 
        help_text=" @Upload image(png, webp, jpeg and svg) with 1200 x 600 (dm) & size 100kb or less",
        content_types=['image/jpeg','image/webp', 'image/svg+xml', 'image/png'],
        max_upload_size=100000, blank=True, null=True
    )
    content = FroalaField(theme='dark', blank=False, null=False, help_text= """
                               <ol>
                                 <li>Change mode to Code View and add class="prettyprint beautify" to the pre class </li>
                                 <li>Use "#2f195f" as color for headers</li>
                                 <li>In pretty-printing html-code use http://hilite.me/ </li>
                                 <li>In uploading images into the florafield, the image might become smaller
                                   compared to its original size. Adjust by clicking on image, 
                                   ruler (change_size) make it more larger than it previously was.
                                </li>
                               </ol> 
                                """
                         )      
    draft = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    url_tracking = models.TextField(_('URL'), max_length=2000, blank=True, null=True)
    hits = models.PositiveIntegerField(_('Hits'), default=0) 
    read_time = models.PositiveIntegerField(_('Read Time'), default=0)             
    meta_description = models.TextField(max_length=10000, blank=False, null=False) 

    def save(self, *args, **kwargs):
        if self.content:
            self.read_time = get_read_time(self.content)
        self.url_tracking = "{0}/{1}".format(settings.DOMAIN_NAME, self.slug)
        super(Post, self).save(*args, **kwargs)


    @property
    def slug_for_title(self):
        return slugify(self.title)
    def slug_for_post(self):
        return self.slug 
    def get_absolute_url(self):
        return reverse("central:article_detail",
        args = [self.slug
        ])
    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ["-timestamp"]


class Contact(models.Model):
    email = models.EmailField(max_length=60, blank=False, null=False)
    subject = models.CharField(max_length=120, blank=False, null=False)
    comment = models.TextField(max_length=1000, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        ordering = ["-timestamp"]




class EmailList(models.Model):
    email = models.EmailField(max_length=60, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        ordering = ["-timestamp"]
