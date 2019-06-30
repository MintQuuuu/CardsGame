from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window


class GameLayout(BoxLayout):
    def __init__(self):
        super(GameLayout, self).__init__()
        self.get_links()

    def get_links(self):
        for i in range(5):
            link_button = LinkButton(
                text='btn: ' + str(i)
            )
            self.ids.links_grid.add_widget(link_button)


class LinkButton(Button):
    pass


class CardsApp(App):
    def build(self):
        Builder.load_file('GameLayout.kv')
        return GameLayout()


if __name__ == "__main__":
    CardsApp().run()















