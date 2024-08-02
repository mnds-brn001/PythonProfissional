import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from threading import Thread
import requests

class AsyncDownload(Thread):
    def __init__(self, url):
        super().__init__()
        self.html = None
        self.url = url
    def run(self):
        response= requests.get(self.url)
        self.html= response.text


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WebPage Download")
        self.geometry('680x430')
        self.resizable(False,False)

        self.create_header_frame()
        self.create_body_frame()
        self.create_footer_frame()

    # Frame do Cabeçalho - Header
    def create_header_frame(self):
        self.header = ttk.Frame(self)
        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(2, weight=10)
        self.header.columnconfigure(2, weight=1)

        # Label do Header
        self.label= ttk.Label(self.header, text='URL')
        self.label.grid(column=0, row=0, sticky= tk.W)
        
        #Entry do Header
        self.url_var = tk.StringVar()
        self.url_entry= ttk.Entry(
            self.header,
            textvariable=self.url_var,
            width= 80
        )
        self.url_entry.grid(column=1, row=0, sticky= tk.EW)

        # Botao do Header
        self.download_button = ttk.Button(self.header, text= "Download")
        self.download_button["command"] = self.handle_download
        self.download_button.grid(column=2, row=0, sticky= tk.E)

        self.header.grid(column=0, row=0, sticky= tk.NSEW, padx=10, pady=10)
    # Frame do Body
    def create_body_frame(self):
        self.body = ttk.Frame(self)
        self.html= tk.Text(self.body, height=20)
        self.html.grid(column=0, row=1)

        scrollbar = ttk.Scrollbar(
            self.body,
            orient='vertical',
            command=self.html.yview
        )
        scrollbar.grid(column=1, row=1, sticky=tk.NS)
        self.html['yscrollcommand'] = scrollbar.set
        self.body.grid(column=0, row=1, sticky= tk.NSEW, padx=10, pady=10)
    #  Frame do Footer
    def create_footer_frame(self):
        self.footer= ttk.Frame(self)
        self.footer.columnconfigure(0, weight=1)

    # Exit Button
        self.exit_button= ttk.Button(
            self.footer,
            text='Exit',
            command=self.destroy
        )
        # exit.grit
        self.exit_button.grid(column=0, row=0, sticky= tk.E)
        # footer.grid
        self.footer.grid(column=0, row=2, sticky= tk.NSEW, padx=10, pady=10)
    
    # Lógica do download
    def handle_download(self):
        url = self.url_var.get()

        if url:
            self.download_button["state"] = tk.DISABLED
            self.html.delete(1.0, "end") # Não armazena o resultado, apenas limpa o campo
            
            download_thread = AsyncDownload(url)
            download_thread.start()

            self.monitor(download_thread)

        else:
            showerror(
            title= "Erro",
            message="Insira a URL da Webpage"
            )


    def monitor(self,thread):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread))
        else:
            self.html.insert(1.0, thread.html)
            self.download_button["state"]= tk.NORMAL

if __name__ =="__main__":
    app= App()
    app.mainloop()