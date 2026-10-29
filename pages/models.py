from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from django.db import models
from wagtail.images import get_image_model_string


class PrestationsPage(Page):
    introduction = RichTextField(blank=True) # nouveau champ de text riche
    content_panels = Page.content_panels + [
        FieldPanel("introduction") # rend le champ visible dans l'admin
    ]


class EquipePage(Page):
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    introduction = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("photo")
    ]


class ContactPage(Page):
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.CharField(max_length=255, blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    planity = models.URLField(blank=True)
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    lundi = models.CharField(max_length=50, blank=True)
    mardi = models.CharField(max_length=50, blank=True)
    mercredi = models.CharField(max_length=50, blank=True)
    jeudi = models.CharField(max_length=50, blank=True)
    vendredi = models.CharField(max_length=50, blank=True)
    samedi = models.CharField(max_length=50, blank=True)
    dimanche = models.CharField(max_length=50, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("photo"),
        FieldPanel("email"),
        FieldPanel("telephone"),
        FieldPanel("adresse"),
        FieldPanel("linkedin"),
        FieldPanel("instagram"),
        FieldPanel("planity"),
        FieldPanel("lundi"),
        FieldPanel("mardi"),
        FieldPanel("mercredi"),
        FieldPanel("jeudi"),
        FieldPanel("vendredi"),
        FieldPanel("samedi"),
        FieldPanel("dimanche") 
    ]