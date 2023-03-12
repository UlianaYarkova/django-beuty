from rest_framework.viewsets import ModelViewSet
from feedback.serializers import FeedbackSerializer
from feedback.models import Feedback

class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
