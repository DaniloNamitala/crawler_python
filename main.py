from tkinter import *
from Noticia import Noticia
import webbrowser
from crawler_g1 import *
from ScrollableFrame import ScrollableFrame

COLOR_BG = "#f2f2f2"
COLOR_BLACK = "#000000"

class Crawler:
    def __init__(self):
        self._root = Tk()
        self._root.geometry("500x700")
        self._root.title("Crawler ")
        self._root.configure(background=COLOR_BG)
        self._create_top_frame()
        self._divider = Frame(self._root, bg=COLOR_BLACK, height=3)
        self._divider.pack(side=TOP, fill="x")
        self._create_video_frame()
        self._video_list = list()

    def _create_video_frame(self):
        self._video_frame = ScrollableFrame(self._root)
        self._video_frame.pack(fill=BOTH, anchor='n', expand=True, side=TOP)
        
    
    def _create_top_frame(self):
        self._top_frame = Frame(self._root, background=COLOR_BG)
        self._top_frame.pack(side=TOP, anchor="w", fill="x")
        self._root.bind('<Return>', self._sarch)

        self._url_text = Entry(self._top_frame, relief=FLAT, highlightcolor=COLOR_BLACK, highlightbackground="grey")
        self._url_text.pack(side=RIGHT, anchor="e", fill="x", pady=3, padx=3, expand=True)
    
    def _sarch(self, event):
        for child in self._video_frame.scrollable_frame.winfo_children():
            child.destroy()
        _search = self._url_text.get()
        if _search != "":
            _url = get_search_url(_search)
            _results = get_search_tree(_url[0])
            _results2 = get_search_tree(_url[1])
            res = get_next_g1(_results)
            res2 = get_next_r7(_results2)
            while(res != None):
                _new = Noticia(self._video_frame.scrollable_frame, res[0], res[1], res[2])
                _new.bind("<Button-1>", self._open_link)
                _new.pack(padx=5, fill="x", pady=2)
                self._root.update()
                res = get_next_g1(res[3])
            
            while(res2 != None):
                _new = Noticia(self._video_frame.scrollable_frame, res2[0], res2[1], res2[2])
                _new.bind("<Button-1>", self._open_link)
                _new.pack(padx=5, fill="x", pady=2)
                self._root.update()
                res2 = get_next_r7(res2[3])

    def _open_link(self, event):
        
        webbrowser.open_new(event.widget.url)
        print(event.widget.url)
    def start(self):
        self._root.mainloop()

def main():
    myApp = Crawler()
    myApp.start()
    

if __name__ == "__main__":
    main()
