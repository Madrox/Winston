from google.appengine.api import urlfetch
from google.appengine.ext import vendor


# Add any libraries installed in the "lib" folder.
vendor.add('lib')

# Import libraries included in the "lib" folder
from django.conf import settings


# Set namespace for App Engine
# Called only if the current namespace is not set.
# def namespace_manager_default_namespace_for_request():
#     # The returned string will be used as the Google Apps domain.
#     return settings.GAE_NAMESPACE

# Set URL Fetch deadline
# urlfetch.set_default_fetch_deadline(settings.URLFETCH_TIMEOUT)

# Enable costs tracking in appstats
appstats_CALC_RPC_COSTS = True

# Enable shell in appstats console if Django debug flag is set
#if settings.DEBUG:
#    appstats_SHELL_OK = True
#    appstats_DEBUG = False
#    appstats_DUMP_LEVEL = -1
#    appstats_DATASTORE_DETAILS = True
#    appstats_CALC_RPC_COSTS = True
#    appstats_MAX_REPR = 1000
#    appstats_MAX_DEPTH = 100
#    appstats_MAX_STACK = 100
