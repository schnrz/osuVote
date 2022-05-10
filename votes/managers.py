from django.contrib.auth import models

class PlayerOAuth2Manager(models.UserManager):
    def create_player(self, player):
        new_player = self.create(
            nick=player.json().get('username'),
            user_id=player.json().get('id'),
            user_avatar=player.json().get('avatar_url'),
            cover_url=player.json().get('cover_url')
        )
        return new_player