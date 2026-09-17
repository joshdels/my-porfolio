from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page


class ProjectType(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Project Type"
        verbose_name_plural = "Project Types"

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProjectsIndexPage(Page):
    intro = RichTextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    subpage_types = [
        "porfolio.Project",
    ]

    class Meta:
        verbose_name = "Projects Index Page"
        verbose_name_plural = "Projects Index Pages"

    def get_context(self, request):
        context = super().get_context(request)

        context["projects"] = (
            self.get_children()
            .live()
            .public()
            .specific()
            .order_by("-first_published_at")
        )

        return context


class Project(Page):
    description = models.TextField(
        help_text="Short description shown on project cards.",
    )

    project_types = models.ManyToManyField(
        ProjectType,
        blank=True,
        related_name="projects",
    )

    tools = models.ManyToManyField(
        Tool,
        blank=True,
        related_name="projects",
    )

    client = models.CharField(
        max_length=200,
        blank=True,
    )

    location = models.CharField(
        max_length=200,
        blank=True,
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    content = RichTextField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
        help_text="Show this project as a featured project.",
    )

    selected = models.BooleanField(
        default=False,
        help_text="Include this project in the selected work section.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("project_types"),
        FieldPanel("tools"),
        FieldPanel("client"),
        FieldPanel("location"),
        FieldPanel("year"),
        FieldPanel("content"),
        FieldPanel("featured"),
        FieldPanel("selected"),
        InlinePanel(
            "project_images",
            label="Images",
            heading="Project Images",
        ),
        InlinePanel(
            "videos",
            label="Videos",
            heading="Project Videos",
        ),
        InlinePanel(
            "links",
            label="Links",
            heading="Project Links",
        ),
        InlinePanel(
            "quotes",
            label="Quotes",
            heading="Project Quotes",
        ),
    ]

    parent_page_types = [
        "porfolio.ProjectsIndexPage",
    ]

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class ProjectImage(Orderable):
    project = ParentalKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_images",
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.CASCADE,
        related_name="+",
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
    )

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]

    def __str__(self):
        return self.caption or self.image.title


class ProjectVideo(Orderable):
    project = ParentalKey(
        Project,
        on_delete=models.CASCADE,
        related_name="videos",
    )

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    url = models.URLField()

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.title or self.url


class ProjectLink(Orderable):
    project = ParentalKey(
        Project,
        on_delete=models.CASCADE,
        related_name="links",
    )

    title = models.CharField(
        max_length=100,
    )

    url = models.URLField()

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.title


class ProjectQuote(Orderable):
    project = ParentalKey(
        Project,
        on_delete=models.CASCADE,
        related_name="quotes",
    )

    quote = models.TextField()

    author = models.CharField(
        max_length=200,
        blank=True,
    )

    role = models.CharField(
        max_length=200,
        blank=True,
    )

    panels = [
        FieldPanel("quote"),
        FieldPanel("author"),
        FieldPanel("role"),
    ]

    def __str__(self):
        return self.author or "Project Quote"
