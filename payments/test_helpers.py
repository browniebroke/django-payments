import unittest

from django.conf import settings

if_drf_installed = unittest.skipUnless(
    "rest_framework" in settings.INSTALLED_APPS,
    reason="DRF is not installed",
)
