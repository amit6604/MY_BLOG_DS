from django.db import models
from datetime import datetime
# Create your models here.
class BloggingCategory(models.Model):
	blog_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.blog_category

class BloggingSeries(models.Model):
	blog_series = models.CharField(max_length=200)
	blog_category = models.ForeignKey(BloggingCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)

	class  Meta: 
		verbose_name_plural = "Series"

	def __str__(self):
		return self.blog_series


class Blogging(models.Model):
	blog_title = models.CharField(max_length=200)
	blog_content = models.TextField()
	blog_published = models.DateTimeField("date published", default = datetime.now)

	blog_series = models.ForeignKey(BloggingSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
	blog_slug = models.CharField(max_length=200, default=1 )
	def __str__(self):
		return self.blog_title