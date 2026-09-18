from django.test import TestCase

from porfolio.models import ContactInquiry
from porfolio.models import (
    ContactInquiry,
    Project,
    ProjectLink,
    ProjectQuote,
    ProjectType,
    ProjectVideo,
    Tool,
)


class ContactInquiryModelTests(TestCase):
    def test_contact_inquiry_creation(self):
        inquiry = ContactInquiry.objects.create(
            name="Test User",
            email="test@example.com",
            industry="other",
            inquiry="Testing the contact inquiry model.",
        )

        self.assertIsNotNone(inquiry.pk)
        self.assertEqual(inquiry.name, "Test User")
        self.assertEqual(inquiry.email, "test@example.com")
        self.assertEqual(inquiry.industry, "other")
        self.assertEqual(str(inquiry), "Test User — other")


class ProjectTypeTests(TestCase):
    def test_project_type_creation(self):
        project_type = ProjectType.objects.create(
            name="GIS Development",
        )

        self.assertEqual(project_type.name, "GIS Development")
        self.assertEqual(str(project_type), "GIS Development")


class ToolTests(TestCase):
    def test_tool_creation(self):
        tool = Tool.objects.create(
            name="Django",
        )

        self.assertEqual(tool.name, "Django")
        self.assertEqual(str(tool), "Django")


class ProjectTests(TestCase):
    def test_project_creation(self):
        project = Project(
            title="Test GIS Project",
            description="A test GIS project.",
            client="Test Client",
            location="Davao",
            selected=True,
            featured=True,
        )

        self.assertEqual(str(project), "Test GIS Project")
        self.assertTrue(project.selected)
        self.assertTrue(project.featured)


class ProjectRelatedModelTests(TestCase):
    def test_project_video_string(self):
        video = ProjectVideo(
            title="Project Demo",
            url="https://example.com/video",
        )

        self.assertEqual(str(video), "Project Demo")

    def test_project_video_uses_url_when_title_is_empty(self):
        video = ProjectVideo(
            title="",
            url="https://example.com/video",
        )

        self.assertEqual(str(video), "https://example.com/video")

    def test_project_link_string(self):
        link = ProjectLink(
            title="Project Website",
            url="https://example.com",
        )

        self.assertEqual(str(link), "Project Website")

    def test_project_quote_string(self):
        quote = ProjectQuote(
            quote="A test quote.",
            author="Test Author",
        )

        self.assertEqual(str(quote), "Test Author")
