from django.urls import path
from services import views

# revisar --> ¿¿¿añadir test that can be used to verify each view ??

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]

# questionnaire URLs
urlpatterns += [
    path('questionnaire-list/', views.QuestionnaireListView.as_view(),
         name='questionnaire-list'),
    path('questionnaire/<int:pk>', views.QuestionnaireDetailView.as_view(),
         name='questionnaire-detail'),
    path('questionnairecreate/', views.QuestionnaireCreateView.as_view(),
         name='questionnaire-create'),
    path('questionnaireremove/<int:pk>',
         views.QuestionnaireRemoveView.as_view(),
         name='questionnaire-remove'),
    path('questionnaireupdate/<int:pk>',
         views.QuestionnaireUpdateView.as_view(),
         name='questionnaire-update'),
]

# question URLs
urlpatterns += [
    path('question/<int:pk>', views.QuestionDetailView.as_view(),
         name='question-detail'),
    path('questionremove/<int:pk>', views.QuestionRemoveView.as_view(),
         name='question-remove'),
    path('questionupdate/<int:pk>', views.QuestionUpdateView.as_view(),
         name='question-update'),
    path('questioncreate/<int:questionnaireid>',
         views.QuestionCreateView.as_view(), name='question-create'),
]

# answer URLs
urlpatterns += [
    path('answercreate/<int:questionid>', views.AnswerCreateView.as_view(),
         name='answer-create'),
    path('answerremove/<int:pk>', views.AnswerRemoveView.as_view(),
         name='answer-remove'),
    path('answerupdate/<int:pk>', views.AnswerUpdateView.as_view(),
         name='answer-update'),
]

# game URLs
urlpatterns += [
    path('gamecreate/<int:questionnaireid>', views.GameCreateView.as_view(),
         name='game-create'),
    path('gameUpdateParticipant/<int:publicid>',
         views.GameUpdateParticipant.as_view(),
         name='game-updateparticipant'),
    path('gamecountdown/', views.GameCountDownTime.as_view(),
         name='game-count-down'),
]
