from django.utils import timezone
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from poller import models
from poller import permissions as poller_permissions
from poller import serializers


class PollViewSet(ModelViewSet):
    serializer_class = serializers.PollSerializer
    permission_classes = (poller_permissions.IsAdminOrReadOnly, )
    queryset = models.Poll.objects.all()

    def perform_destroy(self, instance: models.Poll):
        instance.deleted = timezone.now()
        instance.save(update_fields=["deleted"])


class QuestionViewSet(ModelViewSet):
    serializer_class = serializers.PollQuestionSerializer
    permission_classes = (poller_permissions.IsAdminOrReadOnly, )
    queryset = models.PollQuestion.objects.filter(poll__deleted__isnull=True)


class AnswerViewSet(ModelViewSet):
    serializer_class = serializers.QuestionAnswerSerializer
    permission_classes = (poller_permissions.CreateOrAdminOnly, )
    queryset = models.QuestionAnswer.objects.filter(question__poll__deleted__isnull=True)


class VoterViewSet(ModelViewSet):
    serializer_class = serializers.VoterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.Voter.objects.get_queryset()
