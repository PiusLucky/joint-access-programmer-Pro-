from django.contrib import admin
from central.models import Post, TagChoices, EmailList, Contact


class PostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ["id","hits", "title", "category","draft"]
    list_display_links = ["id"]
    list_editable = ["title", "draft","category"]
    list_filter = ["category", "draft", "read_time", "last_updated", "timestamp"]
    search_fields = ["id","read_time", "title","slug","category","draft","content"]
    exclude = ('url_tracking', 'hits','read_time', )
    readonly_fields = ('url_tracking', 'hits','read_time', )
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["email","subject"]
    list_display_links = ["email"]
    list_filter = ["email","subject"]
    search_fields = ["email","subject", "comment"]
    exclude = ('timestamp',)
    readonly_fields = ('timestamp',)
    class Meta:
        model = Contact
admin.site.register(Contact,ContactModelAdmin)


admin.site.register(TagChoices)
admin.site.register(EmailList)
