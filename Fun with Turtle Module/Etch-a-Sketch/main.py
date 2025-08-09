from turtle import Screen
from sketch import EtchASketch
from ui import WelcomeScreen, InfoPanel

def start_etch():
    info_panel.show()
    etch = EtchASketch(screen)

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Etch-a-Sketch")


welcome = WelcomeScreen(screen)
info_panel = InfoPanel(screen)

welcome.show()
welcome.wait_for_start(start_etch)

screen.exitonclick()
