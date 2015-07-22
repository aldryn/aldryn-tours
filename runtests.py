import os
import sys

import django


cmd = 'coverage run `which djangocms-helper` aldryn_tours test --cms --extra-settings=test_settings'

if django.VERSION[:2] < (1, 6):
    cmd += ' --runner=discover_runner.DiscoverRunner'

sys.exit(os.system(cmd))
