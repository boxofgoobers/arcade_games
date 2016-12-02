import random

import arcade

WIDTH = 800
HEIGHT = 600


class MyApplication(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        self.all_sprites_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("character.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)

        self.score: int = 0
        self.is_stopped: bool = True

        self.coin_list = arcade.SpriteList()
        for i in range(50):
            coin = arcade.Sprite("coin_01.png", 0.2)
            coin.center_x = random.randrange(800)
            coin.center_y = random.randrange(600)
            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        output = f"Score: {self.score:02d}"
        if self.is_stopped:
            arcade.draw_text(output, 10, 10, arcade.color.WHITE, 10)
        self.is_stopped = True
        self.all_sprites_list.draw()

    def animate(self, delta_time):
        self.all_sprites_list.update()
        hit_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.coin_list
        )
        for coin in hit_list:
            coin.kill()
            self.score += 1

    def on_mouse_motion(self, x, y, dx, dy):
        self.is_stopped = False
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


if __name__ == '__main__':
    window = MyApplication(WIDTH, HEIGHT, "Demo")
    arcade.run()
