#!/usr/bin env python3
import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]
    def __init__(self, controller):
        super().__init__()
        self.title('PythonExcel')
        self.config(bg='black')
        self.controller = controller

        self.value_var = tk.StringVar()
        
        self.__make_main_frame()
        self.__make_label()
        self.__make_buttons()
        self.__configure_buttons_styles()

    def __configure_buttons_styles(self):
        style = ttk.Style()
        #style.theme_use('clam')

        # Numbers
        style.configure(
            'N.TButton', foreground='white', background='grey'
        )
        # Operators
        style.configure(
            'O.TButton', foreground='white', background='blue'
        )
        # Misc
        style.configure(
            'M.TButton',
        )

        print(style.theme_names())
        print(style.theme_use())

    def main(self):
        self.mainloop()
    
    def __make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def __make_label(self):
        ent = tk.Label(
            self.main_frm,
            anchor='e',
            textvariable=self.value_var,
            bg='black', fg='white', font=('Arial', 30)
        )
        ent.pack(fill='x')
    
    def __make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        is_first_row = True
        buttons_in_row = 0

        for caption in self.button_captions:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False

                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x')

                buttons_in_row = 0
            
            if isinstance(caption, int):
                style_prefix = 'N'
            elif caption in ['/', '*', '=', '+', '-']:
                style_prefix = 'O'
            else:
                style_prefix = 'M'
                
            style_name = f'{style_prefix}.TButton'

            btn = ttk.Button(
                frm,
                text=caption,
                command=(lambda caption=caption: self.controller.on_button_click(caption)),
                style=style_name
            )
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none'
                expand = 0

            btn.pack(fill=fill, expand=expand, side='left')
            buttons_in_row += 1
