from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
            ('Expert', 'Expert'),
        ],
        default='Intermediate'
    )
    category = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'name']


class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    business_problem = models.TextField(blank=True)
    key_features = models.TextField(blank=True)
    role = models.CharField(max_length=200, blank=True)
    challenges = models.TextField(blank=True)
    lessons_learned = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    static_image = models.CharField(
        max_length=200, blank=True,
        help_text="Static file path relative to STATICFILES_DIRS, e.g. images/chatbot_screenshot.png"
    )
    screenshot_caption = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-order', '-created_at']
