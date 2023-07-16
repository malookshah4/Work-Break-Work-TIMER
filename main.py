import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_text.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        update_top_text("Break", RED)
    elif reps % 2 == 0:
        update_top_text("Break", PINK)
        count_down(short_break_sec)
    else:
        update_top_text("Work", GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
def update_top_text(text, color):
    top_text.config(text=text, fg=color)


window = tk.Tk()
window.title("Pamadora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Times New Roman", 30, "bold"))
canvas.grid(column=2, row=2)

top_text = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Times New Roman", 36, "bold"))
top_text.grid(column=2, row=0)

btn_start = tk.Button(text="Start", command=start_timer)
btn_start.config(padx=10)
btn_start.grid(column=0, row=3)

btn_reset = tk.Button(text="Reset", command=reset_timer)
btn_reset.config(padx=10)
btn_reset.grid(column=3, row=3)

check = tk.Label(text="", fg=GREEN, bg=YELLOW, font=("Times New Roman", 15, "normal"))
check.grid(column=2, row=4)

window.mainloop()
