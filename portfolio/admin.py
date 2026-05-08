from django.contrib import admin
from .models import Project, Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'order')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('-order', '-created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description')
        }),
        ('Media & Links', {
            'fields': ('image', 'github_url', 'live_url')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'order')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category', 'level')
    search_fields = ('name', 'category')
    ordering = ('category', 'name')
