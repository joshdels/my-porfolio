from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactInquiryForm


def contact(request):
    if request.method == "POST":
        form = ContactInquiryForm(request.POST)

        if form.is_valid():
            inquiry = form.save()

            email = EmailMessage(
                subject=f"New portfolio inquiry from {inquiry.name}",
                body=(
                    f"Name: {inquiry.name}\n"
                    f"Email: {inquiry.email}\n"
                    f"Industry: {inquiry.get_industry_display()}\n\n"
                    f"Inquiry:\n{inquiry.inquiry}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[inquiry.email],
            )

            email.send()

            messages.success(
                request,
                "Thanks for reaching out. I'll get back to you soon.",
            )

            return redirect("contact")

    else:
        form = ContactInquiryForm()

    return render(
        request,
        "porfolio/contact.html",
        {"form": form},
    )
