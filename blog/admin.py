from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	fields = ('title','content','author', 'published', 'slug')
	prepopulated_fields = {'slug' : ('title',)}
	list_display = ['published','title', 'updated_at']
	list_display_links = ['title']
	list_editable = ['published']
	list_filter = ['published', 'updated_at']	
	search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)