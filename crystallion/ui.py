import customtkinter as ctk

from constants import *

class MainCard(ctk.CTkFrame):

    def __init__(self,parent):

        super().__init__(

            parent,

            fg_color=CARD,

            corner_radius=25,

            border_width=2,

            border_color=CYAN

        )

        self.place(relx=.5,rely=.5,anchor="center",relwidth=.9,relheight=.9)