from django.db import models


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted__isnull=True)


class PollTypes:
    TEXT = "TEXT"
    SINGLE_CHOICE = "SINGLE_CHOICE"
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"

    @classmethod
    def choices(cls):
        return (
            (cls.TEXT, "Ответ текстом"),
            (cls.SINGLE_CHOICE, "Один ответ"),
            (cls.MULTIPLE_CHOICE, "Несколько ответов"),
        )


class Poll(models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(editable=False, auto_now=True)
    date_closed = models.DateTimeField(null=True)
    deleted = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField("poller.Voter", related_name="voted_polls", null=True, blank=True)

    objects = NotDeletedManager()

    def __str__(self):
        return f"Poll #{self.id} <{self.title}>"


class QuestionAnswer(models.Model):
    text = models.TextField()
    question = models.ForeignKey("poller.PollQuestion", related_name="answers", on_delete=models.DO_NOTHING)
    voter = models.ForeignKey("poller.Voter", related_name="votes", on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"Answer for question {self.question.short_text} in poll #{self.question.poll_id}"


class PollQuestion(models.Model):
    text = models.TextField()
    type = models.CharField(max_length=20, choices=PollTypes.choices())
    poll = models.ForeignKey("poller.Poll", related_name="questions", on_delete=models.DO_NOTHING, editable=False)
    deleted = models.DateTimeField(null=True)

    objects = NotDeletedManager()

    def __str__(self):
        return f"Question \"{self.short_text}\" for poll #{self.poll.id}"

    @property
    def short_text(self):
        return self.text if len(self.text) < 50 else self.text[:47] + "..."


class Voter(models.Model):
    id = models.BigIntegerField(primary_key=True)
    deleted = models.DateTimeField(null=True)

    objects = NotDeletedManager()
