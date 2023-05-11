from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Answer, Game, Guess, Participant, \
    Question, Questionnaire, User

# Register your models here.
admin.site.register(Guess)


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 0


class GameInline(admin.TabularInline):
    model = Game
    extra = 0


class GuessInline(admin.TabularInline):
    model = Guess
    extra = 0


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline, GameInline]


class AnswersInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersInline, GuessInline]


class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 0


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline, GuessInline]


class QuestionnaireInline(admin.TabularInline):
    model = Questionnaire
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [QuestionnaireInline]


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    inlines = [GuessInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    inlines = [GuessInline]
