#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    if 'test' in sys.argv:
        os.environ["DJANGO_GALLERY_ENVIRONMENT"] = "testing"
    elif not os.environ.get("DJANGO_GALLERY_ENVIRONMENT"):
        os.environ["DJANGO_GALLERY_ENVIRONMENT"] = "development"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redirect.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
