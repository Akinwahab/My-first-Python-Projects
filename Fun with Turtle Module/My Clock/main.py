import turtle
from face import ClockFace
from hands import ClockHand
from display import DigitalDisplay
from utils import get_time_parts, time_string

class HybridClock:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Akinwahab's Clock")
        self.wn.bgcolor("#1c1c1c")
        self.wn.setup(width=650, height=650)
        self.wn.tracer(0)

        # Draw face
        ClockFace()

        # Draw hands (store as instance attributes!)
        self.hour_hand = ClockHand(color="gold", length=14, width=0.6)
        self.minute_hand = ClockHand(color="white", length=17, width=0.4)
        self.second_hand = ClockHand(color="red", length=20, width=0.2, center_dot=False)

        # Digital display
        self.digital = DigitalDisplay(y_offset=-100, theme="futuristic")
    
    def update(self):
        hours, minutes, seconds, am_pm = get_time_parts()

        # Calculate angles
        sec_angle = 6 * seconds
        min_angle = 6 * minutes + seconds / 10
        hour_angle = 30 * hours + minutes / 2

        # Update hands
        self.hour_hand.update_angle(hour_angle)
        self.minute_hand.update_angle(min_angle)
        self.second_hand.update_angle(sec_angle)

        # Update digital display
        self.digital.draw_glow_text(f"{time_string()} {am_pm}")

        # Refresh screen and schedule next update
        self.wn.update()
        self.wn.ontimer(self.update, 1000)

    def run(self):
        self.update()
        self.wn.mainloop()

if __name__ == "__main__":
    clock = HybridClock()
    clock.run()
