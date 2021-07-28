from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .validators import validate_file_extension
from django.utils.translation import gettext_lazy as _

class Articles(models.Model):
    name = models.CharField(_('name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='articles')
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Articles,self).save(*args, **kwargs)


class Books(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='books')
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Books,self).save(*args, **kwargs)


class Presentations(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='presentations')
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Presentations,self).save(*args, **kwargs)


class Projects(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='projects')
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Projects,self).save(*args, **kwargs)


class Events(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='events')
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Events,self).save(*args, **kwargs)


class Videos(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='videos', validators=[validate_file_extension])
    link = models.URLField(_('Link'), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author') )
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False, null=False, unique=True, max_length=500)
 
    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
    
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Videos,self).save(*args, **kwargs)


