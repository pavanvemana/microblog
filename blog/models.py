from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now_add=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, blank=True, default='')
	content = models.TextField()
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User, related_name="posts")

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	@models.permalink
	def get_absolute_url(self):
		return ("blog:detail",(),{"slug": self.slug})

	class Meta:
		ordering = ['-created_at', 'title']

class Follower(models.Model):
	creator_uname = models.ForeignKey(User,related_name='request_set')
	following_uname = models.ForeignKey(User,related_name='following_set')