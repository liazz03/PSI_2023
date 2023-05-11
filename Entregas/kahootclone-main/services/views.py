from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import Http404
from models.models import Questionnaire
from models.models import Question
from models.models import Answer
from models.models import Game, Participant
from models.forms import CreateQuestionnaireForm, CreateAnswerForm
from models.forms import RemoveQuestionnaireForm, RemoveAnswerForm
from models.forms import RemoveQuestionForm
from models.forms import CreateQuestionForm
from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
import models.constants


class HomeView(ListView):
    """Displays the home view, which contains a
    series of actions and a simple list with the
    latest 5 questionnaires from the user, as long
    as it is connected.

    Author: Lía Castañeda

    """
    template_name = 'home.html'
    model = Questionnaire
    # Includes the list of questionnaires (defined in the queryset)
    context_object_name = 'questionnaire_list'

    def get_queryset(self):
        # If there is a user identified, then their
        # latest 5 questionnaires are shown
        if self.request.user.is_authenticated:
            return (
                # Questionnaires are ordered by newest by default
                Questionnaire.objects.filter(user=self.request.user)[:5]
            )


class QuestionnaireListView(LoginRequiredMixin, ListView):
    """Displays a listing of the questionnaires

    Author: Enrique Saiz

    """
    model = Questionnaire
    context_object_name = 'questionnaire_list'
    template_name = 'questionnaire_listing.html'

    def get_queryset(self):
        return Questionnaire.objects.filter(user=self.request.user)


class QuestionnaireCreateView(LoginRequiredMixin, CreateView):
    """Displays a view for creating questionnaire

    Author: Lía Castañeda

    """
    template_name = 'questionnaire_create.html'
    model = Questionnaire
    form_class = CreateQuestionnaireForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionnaireDetailView(LoginRequiredMixin, UserPassesTestMixin,
                              DetailView):
    """Displays a view to the questionnaire detail,
    showing the questions related to it.

    Author: Enrique Saiz

    """

    template_name = "questionnaire_detail.html"

    model = Questionnaire

    def test_func(self):
        # Tests whether the request user is the creator
        obj = self.get_object()
        return obj.user == self.request.user


class QuestionnaireRemoveView(LoginRequiredMixin, UserPassesTestMixin,
                              DeleteView):
    """Displays a view for removing the questionnaire,
    if the user has access.

    Author: Lía Castañeda

    """
    model = Questionnaire
    template_name = "questionnaire_remove.html"
    form_class = RemoveQuestionnaireForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Questionnaire, pk=pk_)

    def get_success_url(self):
        return reverse('questionnaire-list')

    def test_func(self):
        # Tests whether the request user is the creator
        obj = self.get_object()
        return obj.user == self.request.user


class QuestionnaireUpdateView(LoginRequiredMixin,
                              UserPassesTestMixin, UpdateView):
    """Displays a view for updating the questionnaire,
    if the user has access. The functionallity is
    similar to questionnaireCreate

    Author: Enrique Saiz

    """

    # QuestionnaireUpdate will use the same template
    # & form as QuestionnaireCreate
    template_name = 'questionnaire_create.html'
    model = Questionnaire
    form_class = CreateQuestionnaireForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Tests whether the request user is the creator
        obj = self.get_object()
        return obj.user == self.request.user


class QuestionCreateView(LoginRequiredMixin, CreateView):
    """Displays a view for creating a question

    Author: Lía Castañeda

    """

    model = Question
    template_name = "question_create.html"

    form_class = CreateQuestionForm

    def form_valid(self, form):
        questionnaireid_ = self.kwargs.get("questionnaireid")
        questionnaireobj = get_object_or_404(Questionnaire,
                                             id=questionnaireid_)
        form.instance.questionnaire = questionnaireobj
        if questionnaireobj.user == self.request.user:
            # If the user is the creator of the parent questionnaire
            return super().form_valid(form)
        else:
            # The user is not allowed, it is not the creator
            form.add_error('question', 'The user is not the creator\
                            of the questionnaire')
            return self.form_invalid(form)


class QuestionDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Displays a view for question detail, if the
    user has access. Note that a cetain question can only
    hold 4 answers, this is controlled in the template.

    Author: Enrique Saiz

    """
    template_name = "question_detail.html"
    model = Question

    def test_func(self):
        # Tests whether the request user is the creator
        # of the parent questionnaire
        obj = self.get_object()
        return obj.questionnaire.user == self.request.user


class QuestionRemoveView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Displays a view for removing a question, if the
    user has access.

    Author: Lía Castañeda

    """
    model = Question
    template_name = "question_remove.html"
    form_class = RemoveQuestionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Question, pk=pk_)

    def get_success_url(self):
        question = self.get_object()
        questionnaire = get_object_or_404(Questionnaire, question=question)

        return reverse('questionnaire-detail', kwargs={'pk': questionnaire.pk})

    def test_func(self):
        # Tests whether the request user is the creator
        # of the parent questionnaire
        obj = self.get_object()
        return obj.questionnaire.user == self.request.user


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Displays a view for modifing a question, if the
    user has access. Functionallity similar to QuestionCreate

    Author: Enrique Saiz

    """
    # QuestionUpdate will use the same template & form as QuestionCreate
    template_name = 'question_create.html'
    model = Question
    form_class = CreateQuestionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Tests whether the request user is the creator
        # of the parent questionnaire
        obj = self.get_object()
        return obj.questionnaire.user == self.request.user


class AnswerCreateView(LoginRequiredMixin, CreateView):
    """Displays a view for creating an answer, if the
    user has access.

    Author: Lía Castañeda

    """
    model = Answer
    template_name = "answer_create.html"

    form_class = CreateAnswerForm

    def form_valid(self, form):
        questionid_ = self.kwargs.get("questionid")
        questionobj = get_object_or_404(Question, id=questionid_)
        form.instance.question = questionobj

        if questionobj.questionnaire.user == self.request.user:
            # If the user is the creator of the parent
            # question's questionnaire, then it is allowed

            if form.instance.correct:
                # If the sent new answer is correct, then
                # check that there are no already correct answers
                for answerobj in questionobj.answer_set.all():
                    if answerobj.correct:
                        form.add_error(field=None,
                                       error="The field 'correct' can be set\
                                          to true in a single answer")
                        return super().form_invalid(form)

            return super().form_valid(form)
        else:
            # The user is not allowed, it is not the creator
            form.add_error('answer', 'The user is not the creator\
                            of the questionnaire')
            return self.form_invalid(form)

    def get_success_url(self):
        return self.object.question.get_absolute_url()


class AnswerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Displays a view for updating an answer, if the
    user has access. Only one correct answer per question is allowed.

    Author: Enrique Saiz

    """
    # AnswerUpdate will use the same template & form as AnswerCreate
    model = Answer
    template_name = "answer_create.html"

    form_class = CreateAnswerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.correct:
            # If the sent updated answer is correct, then
            # check that there are no already correct answers
            for answerobj in self.get_object().question.answer_set.all():
                if answerobj.correct and answerobj != self.get_object():
                    form.add_error(field=None,
                                   error="The field 'correct' can be set\
                                    to true in a single answer")
                    return super().form_invalid(form)
        return super().form_valid(form)

    def test_func(self):
        # Tests whether the request user is the creator
        # of the parent question's questionnaire
        obj = self.get_object()
        return obj.question.questionnaire.user == self.request.user

    def get_success_url(self):
        return self.object.question.get_absolute_url()


class AnswerRemoveView(LoginRequiredMixin, DeleteView):
    """Displays a simple view for removing an answer

    Author: Lía Castañeda

    """
    model = Answer
    template_name = "answer_remove.html"
    form_class = RemoveAnswerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Answer, pk=pk_)

    def get_success_url(self):
        answer = self.get_object()
        question = get_object_or_404(Question, answer=answer)
        return question.get_absolute_url()

    def test_func(self):
        # Tests whether the request user is the creator
        # of the parent question's questionnaire
        obj = self.get_object()
        return obj.question.questionnaire.user == self.request.user


class GameCreateView(LoginRequiredMixin, DetailView):
    """Displays the starting game screen, if the
    user has access.

    Author: Enrique Saiz

    """
    model = Game
    template_name = "game_create.html"

    def get_object(self):
        # Retrieves the parent Questionnaire
        questionnaire_id = self.kwargs.get("questionnaireid")
        questionnaireobj = get_object_or_404(Questionnaire,
                                             id=questionnaire_id)
        # Instantiates the Game with the given Questionnaire
        new_game = Game.objects.create(questionnaire=questionnaireobj)
        # Saves the game id in a session variable for later
        self.request.session['game_id'] = new_game.id
        # For testing-check purposes:
        self.request.session['game_state'] = new_game.state

        return new_game

    def get_template_names(self):
        obj = self.get_object()
        if obj.questionnaire.user == self.request.user:
            # If it is the owner, return the proper template
            return ['game_create.html']
        else:
            # Otherwise there is no permission
            # The user is not allowed, it is not the creator
            return ['game_error.html']


class GameUpdateParticipant(LoginRequiredMixin, ListView):
    """Displays a view for updating participants in game,
    which can then be loaded peridiocally.

    Author: Lía Castañeda

    """

    model = Participant
    template_name = 'game_update_participant.html'
    context_object_name = 'participants_list'

    def get_queryset(self):
        publicId = self.kwargs.get("publicid")
        gameobj = get_object_or_404(Game, publicId=publicId)
        return Participant.objects.filter(game=gameobj)


class GameCountDownTime(LoginRequiredMixin, TemplateView):
    """Displays different templates depending on the game state,
    and updates de game state and context variables accordingly.
    All the game simulation is handled from here.

    Author: Enrique Saiz

    """

    def get_game_state(self):
        # Auxiliary method to
        # retrieve the game state
        game_id = self.request.session['game_id']
        gameobj = get_object_or_404(Game, id=game_id)

        return gameobj.state

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_id = self.request.session['game_id']
        gameobj = get_object_or_404(Game, id=game_id)
        qNo = gameobj.questionNo
        game_state = self.get_game_state()

        if game_state == models.constants.WAITING:
            # Loads the countdown
            context['countdown'] = gameobj.countdownTime

        elif game_state == models.constants.QUESTION:
            # Loads the question, the answers and the countdown
            questionobj = gameobj.questionnaire.question_set.all()[qNo]
            context['question'] = questionobj.question
            context['answers'] = questionobj.answer_set.all()
            # Answer time to miliseconds
            context['answer_time'] = questionobj.answerTime * 1000

        elif game_state == models.constants.ANSWER:
            # Loads the correct answer (we assume there is only 1)
            questionobj = gameobj.questionnaire.question_set.all()[qNo]
            answerobj = questionobj.answer_set.filter(correct=True)[0]
            context['answer'] = answerobj
            # Loads data about the answer (correct guesses, total)
            num_correct = 0
            for guess in questionobj.guess_set.filter(game=gameobj):
                if guess.answer.correct:
                    num_correct += 1
            context['correct'] = num_correct
            context['total'] = len(questionobj.guess_set.filter(game=gameobj))
            # Loads the game's participant list to show data
            context['participants_list'] = gameobj.participant_set.all()

        elif game_state == models.constants.LEADERBOARD:
            # Loads the game's final participant list
            context['participants_list'] = gameobj.participant_set.all()

        return context

    def get_template_names(self):
        templates = []
        game_id = self.request.session['game_id']
        gameobj = get_object_or_404(Game, id=game_id)
        qNo = gameobj.questionNo
        game_state = self.get_game_state()

        # Selects the template regarding the state
        if game_state == models.constants.WAITING:
            if len(gameobj.questionnaire.question_set.all()) == 0:
                # If there are no questions go directly to leaderboard
                gameobj.state = models.constants.LEADERBOARD
            else:
                # Navigates to FIRST QUESTION (default qNo is already 0)
                gameobj.state = models.constants.QUESTION
            # Adds the template
            templates = ['game_count_down.html']
        elif game_state == models.constants.QUESTION:
            # Modifies the state to the question's ANSWER
            gameobj.state = models.constants.ANSWER
            # Adds the template
            templates = ['game_questions_answers.html']
        elif game_state == models.constants.ANSWER:
            newNo = qNo + 1
            if newNo < len(gameobj.questionnaire.question_set.all()):
                # Navigates to next question
                gameobj.questionNo = newNo
                # Modifies the state to the next QUESTION
                gameobj.state = models.constants.QUESTION
            else:
                # No more questions; go to LEADERBOARD next
                gameobj.state = models.constants.LEADERBOARD
            # Adds the template
            templates = ['game_answer.html']
        elif game_state == models.constants.LEADERBOARD:
            # Adds the template
            templates = ['game_leaderboard.html']
        else:
            raise Http404()

        gameobj.save()
        # For testing-check purposes:
        self.request.session['game_state'] = gameobj.state

        return templates
