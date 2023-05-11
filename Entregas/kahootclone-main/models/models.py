from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone
from random import randint
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    """Default user class"""
    pass


class Questionnaire(models.Model):
    """Class to model a Questionnaire, composed
    of several questions which refer to it as FK.
    Questionnaires are ordered from newest.

    Author: Lía Castañeda

    """
    title = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(verbose_name='created at',
                                      default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='updated at',
                                      default=timezone.now)

    user = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        # Ordered from latest first to oldest last
        ordering = ["-updated_at"]

    # redirect to detail view automatically
    def get_absolute_url(self):
        return reverse("questionnaire-detail", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        # updated_at is set each time the object changes
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    """Class to model a Question, which belongs
    to a certain questionnaire.
    Questionnaires are ordered from newest.

    Author: Enrique Saiz

    """
    question = models.CharField(max_length=200, blank=True)

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='created at',
                                      default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='updated at',
                                      default=timezone.now)
    answerTime = models.PositiveIntegerField(verbose_name='answer time',
                                             validators=[
                                                MinValueValidator(1)],
                                             default=20, blank=True)

    class Meta:
        # Ordered from latest first to oldest last
        ordering = ["-updated_at"]

    # redirect to detail view automatically
    def get_absolute_url(self):
        return reverse("question-detail", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        # updated_at is set each time the object changes
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.question


class Answer(models.Model):
    """Class to model an Answer, which belongs to
    a certain Question. Only 4 answers per question
    are allowed, and 1 correct answer per question.

    Author: Lía Castañeda

    """
    answer = models.CharField(max_length=200, blank=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField()
    # The form to introduce the answers must take into account this limitation
    # , that is,
    # there must be only one correct answer per question

    def __str__(self) -> str:
        return self.answer


class Game(models.Model):
    """Class to model the Game, which is
    usually accessed by the publicId, and is
    composed of a questionnaire.
    Compromises several states to be traversed
    in a game simulation.

    Author: Enrique Saiz

    """

    STATE_TAG = (
        (1, 'WAITING'),
        (2, 'QUESTION'),
        (3, 'ANSWER'),
        (4, 'LEADERBOARD'),
    )

    state = models.IntegerField(choices=STATE_TAG, default=1)

    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

    created_at = models.DateTimeField(verbose_name='created at',
                                      default=timezone.now)

    # publicId is initialized in save()
    publicId = models.BigIntegerField(help_text='between 1 and 1000000.\
                                       If not specified, a random one \
                                      will be assigned',
                                      validators=[MinValueValidator(1),
                                                  MaxValueValidator(1000000)],
                                      blank=True)

    countdownTime = models.IntegerField(default=5)

    questionNo = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.publicId:
            # publicId lies in [1,1000000]
            self.publicId = randint(1, 1000000)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "[" + str(self.id) + "] " + "Game " + str(self.publicId)


class Participant(models.Model):
    """Class to model a Participant, the representation
    of the player in a certain game. They are ranked by
    score (points).

    Author: Lía Castañeda

    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    alias = models.CharField(max_length=200, blank=True)
    points = models.IntegerField(default=0)

    uuidP = models.UUIDField(default=uuid.uuid4)

    class Meta:
        # Ordered by points (from most points to fewest)
        ordering = ["-points"]

    def __str__(self) -> str:
        return self.alias


class Guess(models.Model):
    """Class to model a Guess, made by a participant
    for a certain game and question.
    Once the participant has submitted an answer (guess) it is not possible
    to modify it.

    Author: Enrique Saiz

    """

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Guesses"

    def save(self, *args, **kwargs):
        if self.answer.correct:
            self.participant.points += 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "Guess: " + self.answer.answer
