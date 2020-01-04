from django.contrib import admin
from .models import Blogging, BloggingSeries, BloggingCategory
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class BlogginAdmin(admin.ModelAdmin):
	fieldsets = [("Title/Date", {"fields": ["blog_title","blog_published"]}),
				 ("URL", {"fields": ["blog_slug"]}),
				 ("Series", {"fields": ["blog_series"]}),
				 ("Content", {"fields": ["blog_content"]})
				 ]
	formfield_overrides = {
			models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(BloggingSeries)
admin.site.register(BloggingCategory)
admin.site.register(Blogging, BlogginAdmin)


