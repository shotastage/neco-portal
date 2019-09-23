from django.conf import settings


def site_common_text(request):
    return {
        'APP_NAME': settings.APPLICATION_NAME,
        'SEASONABLE_EMOJI': settings.SEASONABLE_EMOJI
    }

