from models.models import Participant, Game, Guess
from .serializers import ParticipantSerializer, GameSerializer
from .serializers import GuessSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from models import constants


class ParticipantViewSet(viewsets.ModelViewSet):
    """ViewSet for the API that handles the participant
    join to the game. It receives a dictionary {"game": int, "alias": string}
    with the game.publicID and participant.alias. The method creates a
    participant and returns the created participant, containing the uuiDP.
    Also lists participants.

    Allowed actions are list, create.

    Author: Enrique Saiz

    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def create(self, request):
        # Note that participants can join a game that is already started,
        # but not a game that has ended.
        # POST action
        try:
            # Retrieve request data
            pId = request.data['game']
            alias = request.data['alias']
        except KeyError:
            # If the request is not well formed
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # Retrieve the game
        games = Game.objects.filter(publicId=pId)
        data = 'Game does not exist.'
        st = status.HTTP_404_NOT_FOUND
        # Check if the game exists
        if games:
            if len(games) > 1:
                # This should not happen as publicId has a wide range
                # and therefore game per publicId should be unique
                return Response(status=status.HTTP_300_MULTIPLE_CHOICES)
            game = games[0]
            # Check if the game is finished or not
            if game.state == constants.LEADERBOARD:
                return Response(data='Game has already ended.',
                                status=status.HTTP_403_FORBIDDEN)
            # Check if the alias is not being used
            if not game.participant_set.filter(alias=alias):
                # Create new participant for that game
                part = Participant.objects.create(alias=alias, game=game)
                # Serialize the participant
                serializer = ParticipantSerializer(part)
                st = status.HTTP_201_CREATED
                data = serializer.data
            else:
                # Alias is being used, return error
                st = status.HTTP_403_FORBIDDEN
                data = 'Alias not available.'

        return Response(data=data, status=st)

    def retrieve(self, request, pk=None):
        # Retrieving a certain participant is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # Deleting a participant is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        # Updating a participant is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # Patching (updating) a participant is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        # Define authentication permissions for the api
        if self.action in ['destroy', 'retrieve',
                           'update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class GameViewSet(viewsets.ModelViewSet):
    """Viewset for the API that handles game information
    retrieval. It receives a dictionary {"publicId": int} including a
    game.publicId and returns a serialized game object.

    Allowed actions are retrieve (by publicId), list

    Author: Lia Castañeda

    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # Searches are performed by pId, not game.id
    lookup_field = 'publicId'

    def create(self, request):
        # Creating a game is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, publicId=None):
        # Deleting a game is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, publicId=None):
        # Updating a game is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, publicId=None):
        # Patching (updating) a game is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        # Define authentication permissions for the api
        if self.action in ['destroy', 'update',
                           'partial_update', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class GuessViewSet(viewsets.ModelViewSet):
    """Viewset for the API that handles guess creation.
    It receives a dictionary {"game": int, "uuidp": string,
    "answer": int} with a game.publicId, a participant.uuidP, together with
    an integer number in the range [0-3] (answer). A guess is then created,
    which is unique for each tuple (participant, question). A guess may only
    be made when state of the game is QUESTION.

    Allowed actions are list, create

    Author: Enrique Saiz

    """
    queryset = Guess.objects.all()
    serializer_class = GuessSerializer

    def create(self, request):
        # POST action
        try:
            # Retrieve request data
            pId = request.data['game']
            uuidP = request.data['uuidp']
            answerNo = request.data['answer']
        except KeyError:
            # If the request is not well formed
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # Retrieve the game
        games = Game.objects.filter(publicId=pId)
        if not games:
            return Response(data='Game does not exist.',
                            status=status.HTTP_404_NOT_FOUND)
        # Retrieve the participant
        participants = Participant.objects.filter(uuidP=uuidP)
        if not participants:
            return Response(data='Participant does not exist.',
                            status=status.HTTP_404_NOT_FOUND)

        if len(games) > 1 or len(participants) > 1:
            # This should not happen as publicId has a wide range
            # and therefore game per publicId should be unique
            # Also, uuidP of Participant should be unique (it is uuid)
            # so usually there would be just one participant
            return Response(status=status.HTTP_300_MULTIPLE_CHOICES)
        game = games[0]
        part = participants[0]
        # Check that the game is awaiting answers (QUESTION)
        if game.state != constants.QUESTION:
            if game.state == constants.LEADERBOARD:
                data = 'The game has already ended.'
            else:
                data = 'wait until the question is shown'
            return Response(data=data,
                            status=status.HTTP_403_FORBIDDEN)
        # Check that the guess is unique (for that participant and question)
        question = game.questionnaire.question_set.all()[game.questionNo]
        if Guess.objects.filter(participant=part, question=question):
            return Response(data='Guess already submitted for the question',
                            status=status.HTTP_403_FORBIDDEN)
        # Check that answer number is correct
        try:
            if answerNo not in [0, 1, 2, 3]:
                raise IndexError()
            answer = question.answer_set.all()[answerNo]
        except IndexError:
            return Response(data='Answer number is not valid.',
                            status=status.HTTP_400_BAD_REQUEST)
        # Checks OK: create and return the Guess
        guess = Guess.objects.create(participant=part, game=game,
                                     question=question, answer=answer)

        serializer = GuessSerializer(guess)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # Retrieving a certain guess is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # Deleting a guess is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        # Updating a guess is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk=None):
        # Patching (updating) a guess is not allowed
        return Response(status=status.HTTP_403_FORBIDDEN)

    def get_permissions(self):
        # Define authentication permissions for the api
        if self.action in ['retrieve', 'destroy',
                           'update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
