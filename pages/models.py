from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from django.db import models


class Project(Orderable):
    page = ParentalKey('PortfolioPage', on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    summary = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('summary'),
        FieldPanel('tech_stack'),
        FieldPanel('github_url'),
        FieldPanel('live_url'),
    ]


class PortfolioPage(Page):
    name = models.CharField(max_length=100)
    title_role = models.CharField(max_length=200)
    bio = RichTextField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    cv_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('title_role'),
        FieldPanel('bio'),
        FieldPanel('cv_url'),
        FieldPanel('github_url'),
        FieldPanel('linkedin_url'),
        FieldPanel('email'),
        InlinePanel('projects', label='Projects'),
    ]