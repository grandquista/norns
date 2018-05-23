from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.generics import (CreateAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from player.models import Player

from .serializers import RoomSerializer, TileSerializer


def _serialize(player, message, **kwargs):
    return Response(
        {
            'message': message,
            'tiles': TileSerializer(
                player.tile.room.tile_set, many=True).data},
        **kwargs)


class RoomView(CreateAPIView, RetrieveAPIView, UpdateAPIView):
    """
    Parse form data and relevant room state.
    """

    def post(self, request, _format=None):
        """
        Response to action post.
        """
        user = User.objects.filter(username=request.user.username).first()
        player = get_object_or_404(Player, user=user)
        player = Player.get_active_player(user)
        user_input = self.request.data['user_input'].split()
        if not user_input:
            return _serialize(player, 'no user input')
        verb = user_input[0]
        if verb == 'look':
            return _serialize(player, player.tile.look())

        if verb == 'take':
            weapon = player.tile.weapons.filter(name=user_input[1]).first()
            if weapon:
                player.inventory.weapons.add(weapon)
                weapon.tiles.remove(player.tile)
                return _serialize(
                    player,
                    'You picked up {}'.format(weapon.name))
            return _serialize(player, 'No {} found'.format(user_input[1]))

        return _serialize(player, player.handle_user_input(user_input))


class NewRoomView(CreateAPIView):
    """
    Create a new game.
    """

    serializer_class = RoomSerializer

    def post(self, request, _format=None):
        """
        Response to create room post.
        """
        user = User.objects.filter(username=request.user.username).first()
        for player in Player.objects.filter(user=user, active=True).all():
            player.active = False
        player = Player.objects.create(user=user, active=True)
        player.tile = player.tile.room.tile_set.order_by('?').first()
        return _serialize(player, 'Welcome to Hel.', status=201)


class TileView(RetrieveAPIView):
    """
    Get tile data.
    """

    serializer_class = TileSerializer
