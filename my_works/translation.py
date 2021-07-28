from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ArticleTranslation(TranslationOptions):
    fields = ('name','file',)

translator.register(Articles, ArticleTranslation)

class BookTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Books, BookTranslation)

class PresentationsTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Presentations, PresentationsTranslation)

class ProjectsTranslation(TranslationOptions):
    fields = ('name',)
 
translator.register(Projects, ProjectsTranslation)

class EventsTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Events, EventsTranslation)

class VideosTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Videos, VideosTranslation)