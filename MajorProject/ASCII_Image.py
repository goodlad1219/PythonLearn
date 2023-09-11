import tkinter as tk

window = tk.Tk()
window.title('ASCII Image')
resize = tk.Canvas(window,width=720, height=880)
resize.pack()
window.configure(bg='black')
window.mainloop()

