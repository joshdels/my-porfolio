from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from porfolio.forms import ContactInquiryForm
from porfolio.models import ContactInquiry


class ContactInquiryFormTests(TestCase):

    def test_valid_contact_form(self):
        form = ContactInquiryForm(
            {
                "name": "Test User",
                "email": "test@example.com",
                "industry": "other",
                "inquiry": "Testing the contact form.",
            }
        )

        self.assertTrue(form.is_valid())

    def test_contact_form_saves(self):
        form = ContactInquiryForm(
            {
                "name": "Test User",
                "email": "test@example.com",
                "industry": "other",
                "inquiry": "Testing the contact form.",
            }
        )

        self.assertTrue(form.is_valid())

        inquiry = form.save()

        self.assertIsNotNone(inquiry.pk)
        self.assertEqual(inquiry.name, "Test User")
        self.assertEqual(inquiry.email, "test@example.com")
        self.assertEqual(inquiry.industry, "other")


class ContactViewTests(TestCase):

    def test_contact_page_loads(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)

        self.assertIsInstance(
            response.context["form"],
            ContactInquiryForm,
        )

    @patch("porfolio.views.EmailMessage.send")
    def test_contact_form_submission(self, mock_send):
        mock_send.return_value = 1

        response = self.client.post(
            reverse("contact"),
            {
                "name": "Test User",
                "email": "test@example.com",
                "industry": "other",
                "inquiry": "Testing the production contact form.",
            },
        )

        # Redirect after successful submission
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("contact"))

        # Inquiry is saved
        self.assertEqual(
            ContactInquiry.objects.count(),
            1,
        )

        inquiry = ContactInquiry.objects.first()

        self.assertEqual(inquiry.name, "Test User")
        self.assertEqual(inquiry.email, "test@example.com")
        self.assertEqual(inquiry.industry, "other")

        # Two emails should be sent:
        # 1. Notification to Joshua
        # 2. Confirmation to the visitor
        self.assertEqual(mock_send.call_count, 2)

        notification_email = mock_send.call_args_list[0][0]
        confirmation_email = mock_send.call_args_list[1][0]

        self.assertEqual(
            notification_email,
            (),
        )

        self.assertEqual(
            confirmation_email,
            (),
        )
