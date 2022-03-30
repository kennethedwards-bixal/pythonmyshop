# import celery
from .celery import app as celery_app

# The CELERY_ALWAYS_EAGER setting allows 
# you to execute tasks locally in a synchronous 
# way, instead of sending them to the queue. This 
# is useful for running unit tests or executing 
# the application in your local environment without running Celery.