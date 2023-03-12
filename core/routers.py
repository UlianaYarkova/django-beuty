from rest_framework.routers import DefaultRouter
from master.views import MasterViewSet
from set.views import SetViewSet
from TypeOfService.views import TypeOfServiceViewSet
from service.views import ServiceViewSet
from feedback.views import FeedbackViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register('master', MasterViewSet)
router.register('set', SetViewSet)
router.register('TypeOfService', TypeOfServiceViewSet)
router.register('Service', ServiceViewSet)
router.register('Feedback', FeedbackViewSet)
router.register('auth', UserViewSet)