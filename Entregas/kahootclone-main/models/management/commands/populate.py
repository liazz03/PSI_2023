# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from models.models import User as User
from models.models import Questionnaire as Questionnaire
from models.models import Question as Question
from models.models import Answer as Answer
from models.models import Game as Game

from faker import Faker
import random


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate kahootclone database
           """
    # if you want to pass an argument to the function
    # uncomment this line
    # def add_arguments(self, parser):
    #    parser.add_argument('publicId',
    #        type=int,
    #        help='game the participants will join to')
    #    parser.add_argument('sleep',
    #        type=float,
    #        default=2.,
    #        help='wait this seconds until inserting next participant')

    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # "if 'RENDER'" allows you to deal with different
        # behaviour in render.com and locally
        # That is, we check a variable ('RENDER')
        # that is only defined in render.com
        if 'RENDER' in os.environ:
            pass
        else:
            pass

        self.NUMBERUSERS = 4
        self.NUMBERQESTIONARIES = 30
        self.NUMBERQUESTIONS = 100
        self.NUMBERPARTICIPANTS = 20
        self.NUMBERANSWERPERQUESTION = 4
        self.NUMBERGAMES = 4

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        "this function will be executed by default"

        self.cleanDataBase()   # clean database
        # The faker.Faker() creates and initializes a faker generator,
        self.faker = Faker()
        self.user()  # create users
        self.questionnaire()  # create questionaries
        self.question()  # create questions
        self.answer()  # create answers
        self.game()  # create games

    def cleanDataBase(self):

        User.objects.all().delete()
        Questionnaire.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Game.objects.all().delete()

        print("clean Database")

    def user(self):
        " Insert users"
        print("Creating Users...")

        for i in range(0, self.NUMBERUSERS):
            name = self.faker.name()
            passw = self.faker.password()

            # Save to DB
            new_user = User(username=name, password=passw)
            new_user.save()

    def questionnaire(self):
        "insert questionnaires"
        print("Creating questionnaires...")

        for i in range(0, self.NUMBERQESTIONARIES):

            title = self.faker.text()

            # random user
            users_list = list(User.objects.all())
            random_user = random.choice(users_list)

            new_questionaire = Questionnaire(title=title, user=random_user)

            # Save to DB
            new_questionaire.save()

    def question(self):
        " insert questions, assign randomly to questionnaires"
        print("Inserting Questions...")

        for i in range(0, self.NUMBERQUESTIONS):

            question_text = self.faker.text()[:180] + " ?"

            # random questionaire
            questionaire_list = list(Questionnaire.objects.all())
            random_quest = random.choice(questionaire_list)

            new_question = Question(question=question_text,
                                    questionnaire=random_quest,
                                    answerTime=random.randint(10, 20))

            # Save to DB
            new_question.save()

    def answer(self):
        "insert answers, one of them must be the correct one"
        print("Inserting Answers ...")

        # your code goes here
        # assign answer randomly to the questions
        # maximum number of answers per question is four

        list = Question.objects.all()
        for quest in list:
            numasw = random.randint(1, self.NUMBERANSWERPERQUESTION)
            numasw = numasw - 1

            for i in range(0, numasw):
                answer_text = self.faker.word()
                new_answer = Answer(answer=answer_text,
                                    question=quest, correct=False)

                # save to DB
                new_answer.save()
            # correct answer
            answer_text = self.faker.word()
            new_answer = Answer(answer=answer_text,
                                question=quest, correct=True)

            # save to DB
            new_answer.save()

    def game(self):
        "insert some games"
        print("Inserting Games...")
        # your code goes here
        # choose at random the questionnaries

        for i in range(0, self.NUMBERGAMES):

            # random questionaire
            questionaire_list = list(Questionnaire.objects.all())
            random_quest = random.choice(questionaire_list)

            new_game = Game(questionnaire=random_quest)

            # save to DB
            new_game.save()
