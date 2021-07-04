from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
 

class MyWorks(models.Model):
    
    CATEGORIES = (
        ('articles','Maqolalar'),
        ('books','Kitoblar'),
        ('events','Tadbirlar'),
        ('presentations','Taqdimotlar'),
        ('projects','Loyihalar'),
        ('videos','Videolar'),   
    )

    category = models.CharField(max_length=15, choices=CATEGORIES)
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='articles')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'My Work'
        verbose_name_plural = 'My Works'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(MyWorks,self).save(*args, **kwargs)



class Articles(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='articles')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Articles,self).save(*args, **kwargs)


class Books(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='books')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Books,self).save(*args, **kwargs)


class Presentations(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='presentations')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Presentations,self).save(*args, **kwargs)


class Projects(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='projects')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Projects,self).save(*args, **kwargs)


class Events(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='events')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Events,self).save(*args, **kwargs)


class Videos(models.Model):
    name = models.CharField(max_length=500, blank=True)
    file = models.FileField(blank=True, null=True, upload_to='videos')
    link = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Videos,self).save(*args, **kwargs)


