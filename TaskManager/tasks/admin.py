from django.contrib import admin
from .models import Task, Invitation
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_at', 'used')
    actions = ['send_invitation_email']

    def send_invitation_email(self, request, queryset):
        for invitation in queryset.filter(used=False):
            link = f"{request.scheme}://{request.get_host()}{reverse('register')}?token={invitation.token}"
            send_mail(
                subject="You're Invited to Join TaskManager!",
                message=(
                    f"Hello,\n\n"
                    f"We're excited to invite you to join TaskManager. To get started, simply click the link below and "
                    f"complete your registration:\n\n"
                    f"{link}\n\n"
                    f"Make sure to register as soon as possible!\n\n"
                    f"Looking forward to having you on board.\n\n"
                    f"Best regards,\n"
                    f"The TaskManager Team"
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[invitation.email],
                fail_silently=False,
            )
        self.message_user(request, "🎉 Invitation emails sent successfully! 🎉")
    send_invitation_email.short_description = "Send invitation email"
