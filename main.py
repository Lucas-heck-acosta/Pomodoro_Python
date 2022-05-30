from tkinter import *
import winsound
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = 0
counting = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, marks
    reps = 0
    marks = 0
    window.after_cancel(counting)
    lbl_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    lbl_check.config(text='')
    btn_start.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps, marks
    reps += 1
    work_secs = WORK_MIN * 60
    s_break_secs = SHORT_BREAK_MIN * 60
    l_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer(l_break_secs)
        lbl_timer.config(text="Break", fg=PINK)
        lbl_check.config(text="✔" * marks)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    elif reps % 2 == 0:
        timer(s_break_secs)
        lbl_timer.config(text="Break", fg=PINK)
        lbl_check.config(text="✔" * marks)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    else:
        timer(work_secs)
        lbl_timer.config(text="Work", fg=RED)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
        marks += 1
    btn_start.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    global counting
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds <= 9:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        counting = window.after(1000, timer, count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(padx=45, pady=55, bg=YELLOW)

canvas = Canvas(width=250, height= 250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato)


timer_text = canvas.create_text(125, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lbl_timer = Label(text="Timer", font=(FONT_NAME, 38, 'bold'),bg=YELLOW, fg=GREEN)
lbl_timer.grid(column=1, row=0)

btn_start = Button(text="Start", font=(FONT_NAME, 13), highlightthickness=0, command=start)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", font=(FONT_NAME, 13), highlightthickness=0, command= reset)
btn_reset.grid(column=2, row=2)

lbl_check = Label(text="✔" * marks, font=(FONT_NAME,  0), fg=GREEN, bg=YELLOW)
lbl_check.grid(column=1, row=2)


window.mainloop()