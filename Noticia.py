from tkinter.ttk import Progressbar
import PIL.Image
import PIL.ImageTk
from io import BytesIO
from urllib.request import urlopen
from tkinter import *

class Noticia (Frame):
    def __init__(self, parent, titulo, url, image) -> None:
        Frame.__init__(self, parent, highlightbackground="blue", highlightthickness=2)
        Frame.__init__(self, parent, highlightbackground="blue", highlightthickness=2, width=350, height=90)
        self._image_url = image
        if (not self._image_url.startswith('http')):
          self._image_url = "https:" + self._image_url
        self._title = titulo
        self.url = url
        if (not self.url.startswith('http')):
          self.url = "https:" + self.url
        self._create_frame()

    def _create_frame(self):
        self._create_thumb()
        self._create_title()

    def _create_thumb(self):
        with urlopen(self._image_url) as url:
          _raw = url.read()
          url.close() 
        self._photo_image = PIL.ImageTk.PhotoImage(PIL.Image.open(BytesIO(_raw)).resize((160,90)))
        self._image = Label(self, image=self._photo_image)
        self._image.pack()
        self._image.pack(side=LEFT, padx=5, anchor="w")

    def _create_title(self):
        self._title = Label(self, text=self._title, font=("Calibri",10), justify=LEFT, wraplength=290, anchor="w")
        self._title.pack(side=TOP, padx=(0,5), fill="x")