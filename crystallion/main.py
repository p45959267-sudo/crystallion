import customtkinter as ctk
import random

from ui import MainCard
from constants import *

# -----------------------------
# App Setup
# -----------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x650")
app.title("Gem Randomizer")
app.configure(fg_color=BACKGROUND)

# -----------------------------
# Main Card
# -----------------------------

card = MainCard(app)

# -----------------------------
# Logo
# -----------------------------

logo = ctk.CTkLabel(
    card,
    text="💎",
    font=("Segoe UI Emoji", 72)
)
logo.pack(pady=(35, 5))

# -----------------------------
# Title
# -----------------------------

title = ctk.CTkLabel(
    card,
    text="GEM RANDOMIZER",
    font=("Segoe UI", 36, "bold"),
    text_color=CYAN
)
title.pack()

subtitle = ctk.CTkLabel(
    card,
    text="Generate beautiful random numbers",
    font=("Segoe UI", 16),
    text_color=GRAY
)
subtitle.pack(pady=(0, 35))

# -----------------------------
# Input Frame
# -----------------------------

frame = ctk.CTkFrame(
    card,
    fg_color="transparent"
)
frame.pack()

minimum = ctk.CTkEntry(
    frame,
    width=260,
    height=55,
    corner_radius=18,
    placeholder_text="Minimum"
)
minimum.grid(row=0, column=0, padx=15)

maximum = ctk.CTkEntry(
    frame,
    width=260,
    height=55,
    corner_radius=18,
    placeholder_text="Maximum"
)
maximum.grid(row=0, column=1, padx=15)

# -----------------------------
# Result Label
# -----------------------------

result = ctk.CTkLabel(
    card,
    text="READY",
    font=("Segoe UI", 48, "bold"),
    text_color=GREEN
)
result.pack(pady=45)

# -----------------------------
# Generate Function
# -----------------------------

def generate():
    try:
        low = int(minimum.get())
        high = int(maximum.get())

        if low > high:
            result.configure(
                text="MIN > MAX",
                text_color="red"
            )
            return

        number = random.randint(low, high)

        result.configure(
            text=f"💎 {number}",
            text_color=GREEN
        )

    except ValueError:
        result.configure(
            text="INVALID INPUT",
            text_color="red"
        )

# -----------------------------
# Generate Button
# -----------------------------

button = ctk.CTkButton(
    card,
    text="GENERATE",
    width=420,
    height=60,
    corner_radius=20,
    fg_color=BUTTON,
    hover_color=BUTTON_HOVER,
    text_color="black",
    font=("Segoe UI", 18, "bold"),
    command=generate
)

button.pack()

# -----------------------------
# Footer
# -----------------------------

footer = ctk.CTkLabel(
    card,
    text="Gem Randomizer v2",
    text_color=GRAY,
    font=("Segoe UI", 12)
)

footer.pack(side="bottom", pady=20)

# -----------------------------
# Enter Key Support
# -----------------------------

app.bind("<Return>", lambda event: generate())

# -----------------------------
# Start Program
# -----------------------------

app.mainloop()