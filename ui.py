
import tkinter
from tkinter import font
from main import predict_email

window = tkinter.Tk()
fonnt = font.Font(family="Helvetica", size=15, weight=font.NORMAL)
window.title("Spam Filter")
window.geometry("550x600")  
window.resizable(False, False)
window.configure(bg="#d9dbda")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

header_label = tkinter.Label(window, text="Email Spam Filter", bg="#d9dbda", font=("Helvetica", 18, "bold"))
header_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

subheader_label = tkinter.Label(window, text="Enter your email subject and text to check for spam", bg="#d9dbda", font=fonnt)
subheader_label.grid(row=1, column=0, columnspan=2, pady=5, sticky="n")

sub = tkinter.LabelFrame(window, text="Subject", font=fonnt, bg="#d9dbda")
sub.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

subject_entry = tkinter.Entry(sub, width=40, font=fonnt)
subject_entry.pack(padx=10, pady=10)

email_frame = tkinter.LabelFrame(window, text="Email Content", font=fonnt, bg="#d9dbda")
email_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

email_text = tkinter.Text(email_frame, width=50, height=10, font=fonnt)
email_text.pack(padx=10, pady=10)

result_frame = tkinter.LabelFrame(window, text="Filter Result", font=fonnt, bg="#d9dbda")
result_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

result_label = tkinter.Label(result_frame, text="No result yet", bg="#ffffff", font=fonnt, width=40, height=2, anchor="center", relief="solid")
result_label.pack(padx=10, pady=10)

def on_predict():
    subject = subject_entry.get()
    email_content = email_text.get("1.0", tkinter.END).strip()
    
    if email_content:
        result = predict_email(email_content)
        result_label.config(text=f"Prediction: {result}")
    else:
        result_label.config(text="Please enter the email content.") 


predict_button = tkinter.Button(window, text="Check Spam", font=fonnt, command=on_predict)
predict_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
