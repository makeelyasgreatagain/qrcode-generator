import qrcode
from tkinter import *
from tkinter import ttk, messagebox


def generate_qrcode():
    text = text_entry.get()

    if not text.strip():
        messagebox.showerror("Error", "You should enter something to generate QRCode.")
        return
    

    try:
        img = qrcode.make(text)
        img.save(f"{text[:10].replace(" ", "").lower()}.png")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

root = Tk()
root.title("QRCode Generator")
root.geometry("400x300")
frm = ttk.Frame(root, padding=10)
frm.pack()
ttk.Label(frm, text="Text: ").pack(pady=20)
text_entry = StringVar()
ttk.Entry(frm, textvariable=text_entry).pack(pady=20)
ttk.Button(frm, text="Generate", command=generate_qrcode).pack(pady=20)
root.mainloop()




