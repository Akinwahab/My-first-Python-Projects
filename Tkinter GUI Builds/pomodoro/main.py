from tkinter import *
import math
from plyer import notification

# ---------------------------- CONSTANTS ------------------------------- #
BASIL_GREEN = "#2D6A4F"
OLIVE_GREEN = "#606C38"
TOMATO_RED = "#D62828"
BEIGE = "#FEFAE0"
FONT_NAME = "Helvetica"

DEFAULT_WORK_MIN = 25
DEFAULT_SHORT_BREAK_MIN = 5
DEFAULT_LONG_BREAK_MIN = 20

WORK_MIN = DEFAULT_WORK_MIN
SHORT_BREAK_MIN = DEFAULT_SHORT_BREAK_MIN
LONG_BREAK_MIN = DEFAULT_LONG_BREAK_MIN

reps = 0
timer = None
cycle_count = 0
paused = False
remaining_time = 0


# ---------------------------- NOTIFICATION ------------------------------- #
def notify(title, message):
    window.bell()
    notification.notify(title=title, message=message, timeout=10)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer, paused, remaining_time
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    count_text.config(text="TIMER", fg=TOMATO_RED)
    check_marks.config(text="")
    reps = 0
    paused = False
    remaining_time = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, paused
    if paused:  # resume from pause
        count_down(remaining_time)
        paused = False
        return

    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        count_text.config(text="BREAK", fg=OLIVE_GREEN)
        update_cycle_counter()
        notify("Pomodoro", "Long break started 🌙")
    elif reps % 2 == 0:
        count_down(short_break_secs)
        count_text.config(text="BREAK", fg=BASIL_GREEN)
        notify("Pomodoro", "Short break started ☕")
    else:
        count_down(work_secs)
        count_text.config(text="WORK", fg=TOMATO_RED)
        notify("Pomodoro", "Work session started 💪")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, remaining_time
    remaining_time = count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = "✔" * math.floor(reps / 2)
        check_marks.config(text=marks)


# ---------------------------- PAUSE ------------------------------- #
def pause_timer():
    global paused, timer
    if not paused:
        window.after_cancel(timer)
        paused = True


# ---------------------------- SESSION COUNTER ------------------------------- #
def update_cycle_counter():
    global cycle_count
    cycle_count += 1
    session_label.config(text=f"Sessions: {cycle_count}")


# ---------------------------- OPTIONS POPUP ------------------------------- #
def open_options():
    def save_custom_times():
        global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
        try:
            WORK_MIN = int(work_input.get()) if work_input.get() else DEFAULT_WORK_MIN
            SHORT_BREAK_MIN = (
                int(short_input.get()) if short_input.get() else DEFAULT_SHORT_BREAK_MIN
            )
            LONG_BREAK_MIN = (
                int(long_input.get()) if long_input.get() else DEFAULT_LONG_BREAK_MIN
            )
        except ValueError:
            WORK_MIN = DEFAULT_WORK_MIN
            SHORT_BREAK_MIN = DEFAULT_SHORT_BREAK_MIN
            LONG_BREAK_MIN = DEFAULT_LONG_BREAK_MIN
        options_win.destroy()

    def restore_defaults():
        global WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN
        WORK_MIN = DEFAULT_WORK_MIN
        SHORT_BREAK_MIN = DEFAULT_SHORT_BREAK_MIN
        LONG_BREAK_MIN = DEFAULT_LONG_BREAK_MIN
        options_win.destroy()

    options_win = Toplevel(window)
    options_win.title("Options")
    options_win.config(padx=20, pady=20, bg=BEIGE)

    Label(options_win, text="Work (min):", bg=BEIGE, font=(FONT_NAME, 12)).grid(
        row=0, column=0, pady=5
    )
    work_input = Entry(options_win, width=5)
    work_input.insert(0, str(WORK_MIN))
    work_input.grid(row=0, column=1)

    Label(options_win, text="Short Break (min):", bg=BEIGE, font=(FONT_NAME, 12)).grid(
        row=1, column=0, pady=5
    )
    short_input = Entry(options_win, width=5)
    short_input.insert(0, str(SHORT_BREAK_MIN))
    short_input.grid(row=1, column=1)

    Label(options_win, text="Long Break (min):", bg=BEIGE, font=(FONT_NAME, 12)).grid(
        row=2, column=0, pady=5
    )
    long_input = Entry(options_win, width=5)
    long_input.insert(0, str(LONG_BREAK_MIN))
    long_input.grid(row=2, column=1)

    Button(
        options_win, text="Save", command=save_custom_times, bg=BASIL_GREEN, fg=BEIGE
    ).grid(row=3, column=0, pady=10, sticky="ew")
    Button(
        options_win,
        text="Restore Default",
        command=restore_defaults,
        bg=TOMATO_RED,
        fg="white",
    ).grid(row=3, column=1, pady=10, sticky="ew")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

options_button = Button(
    text="⚙",
    command=open_options,
    bg=OLIVE_GREEN,
    fg=BEIGE,
    font=(FONT_NAME, 12, "bold"),
)
options_button.grid(row=0, column=3, sticky="ne")

count_text = Label(text="TIMER", fg=TOMATO_RED, bg=BEIGE, font=(FONT_NAME, 50, "bold"))
count_text.grid(row=1, column=2)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=244, bg=BEIGE, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(row=2, column=2)

# Button Style
button_style = {
    "bg": BASIL_GREEN,
    "fg": BEIGE,
    "font": (FONT_NAME, 14, "bold"),
    "relief": "flat",
    "activebackground": OLIVE_GREEN,
    "activeforeground": BEIGE,
    "width": 8,
    "height": 2,
}

start_button = Button(text="Start", command=start_timer, **button_style)
start_button.grid(row=3, column=1)

pause_button = Button(text="Pause", command=pause_timer, **button_style)
pause_button.grid(row=3, column=2)

reset_button = Button(text="Reset", command=reset_timer, **button_style)
reset_button.grid(row=3, column=3)

check_marks = Label(fg=TOMATO_RED, bg=BEIGE)
check_marks.grid(row=4, column=2)

session_label = Label(
    text="Sessions: 0", fg=OLIVE_GREEN, bg=BEIGE, font=(FONT_NAME, 14, "bold")
)
session_label.grid(row=5, column=2)

window.mainloop()
