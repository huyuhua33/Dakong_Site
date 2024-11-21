# Create your models here.
# WebSite App
# WebSite/models.py (Example of Static Page Model)
from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class HomePageContent(TranslatableModel):
    translations = TranslatedFields(
        headline=models.CharField(max_length=200),
        subheadline=models.TextField(),
    )
    promotional_image = models.ImageField(upload_to='homepage/')

    def __str__(self):
        return self.safe_translation_getter('headline', any_language=True)
