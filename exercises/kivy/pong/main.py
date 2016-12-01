from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongGame(Widget):
    ball = ObjectProperty(None)

    def update(self, dt):
        self.ball.move()

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1/60)
        return game

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


if __name__ == '__main__':
    PongApp().run()
