from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from poller import models


class QuestionAnswerSerializer(WritableNestedModelSerializer):

    def to_internal_value(self, data):
        if voter := data.get("voter"):
            models.Voter.objects.get_or_create(id=voter)

        return super(QuestionAnswerSerializer, self).to_internal_value(data)

    def create(self, validated_data):
        instance = super(QuestionAnswerSerializer, self).create(validated_data)
        instance.voter.voted_polls.add(instance.question.poll)
        return instance

    class Meta:
        model = models.QuestionAnswer
        fields = ("id", "text", "question", "voter")


class PollQuestionSerializer(serializers.ModelSerializer):
    answers = QuestionAnswerSerializer(many=True, required=False)
    poll_id = serializers.IntegerField(required=True)

    class Meta:
        model = models.PollQuestion
        fields = ("id", "text", "type", "answers", "poll_id")


class PollSerializer(serializers.ModelSerializer):
    questions = PollQuestionSerializer(many=True, required=False)

    class Meta:
        model = models.Poll
        fields = ("id", "title", "description", "date_created", "questions")


class VoterSerializer(WritableNestedModelSerializer):
    voted_polls = PollSerializer(many=True, required=False)

    class Meta:
        model = models.Voter
        fields = ("id", "voted_polls")
