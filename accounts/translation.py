from modeltranslation.translator import translator, TranslationOptions
from .models import *
from accounts.models import AddressLink

class AddressLinkTranslation(TranslationOptions):
    fields = ('name',)

translator.register(AddressLink, AddressLinkTranslation)