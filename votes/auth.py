from django.contrib.auth.backends import BaseBackend
from .models import Player

class PlayerAuthenticationBackend(BaseBackend):
    def authenticate(self, request, player) -> Player:
        find_player = Player.objects.filter(user_id=player.json().get('id'))
        if len(find_player) == 0:
            # Player was not found, saving...
            new_user = Player.objects.create_player(player)
            return new_user
        return find_player

    # TODO: check if this works ffs
    # def get_player(self, user_id):
    #     print('entró al get player del auth.python wn la conehcuiotshskldfnskldnfslkjdfnaklndfkjlalk;adjlfa')
    #     try:
    #         return Player.objects.get(pk=user_id)
    #     except Player.DoesNotExist:
    #         return None            