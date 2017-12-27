from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Category, Movie

admin.site.site_header = 'IPDB Backoffice'
admin.site.site_title = 'IPDB Backoffice'

admin.site.register(Category)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('title', 'release_date', 'rating', 'user_full_name', 'category')
    list_filter = ('category', 'user')
    search_fields = ('title', 'director_name', 'summary')

    def user_full_name(self, movie):
        return "{0} {1}".format(movie.user.first_name, movie.user.last_name)
    user_full_name.short_description = "Movie Owner"
    user_full_name.admin_order_field = "user__first_name"

    def get_image_html(self, movie):
        return mark_safe("<img src='{0}' alt='{1}' height='100px' />".format(movie.image, movie.title))
    get_image_html.short_description = "Preview Image"

    #  Custom detail of a movie
    readonly_fields = ('created_at', 'modified_at', 'get_image_html')
    fieldsets = (
        ('Datos generales', {
            'fields': ('title', 'summary')
        }),
        ('Category and Rating', {
            'fields': ('category', 'rating')
        }),
        ('Additional Info', {
            'fields': ('director_name', 'release_date', 'get_image_html', 'image', 'user')
        }),
        ('Created & Modified', {
            'fields': ('created_at', 'modified_at'),
            'classes': ('collapse',),
            'description': 'These fields are auto-generated'
        }),
    )