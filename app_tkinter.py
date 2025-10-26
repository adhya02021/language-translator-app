from tkinter import *
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from playsound import playsound

def translate_text():
    src = source_lang.get().strip()
    tgt = target_lang.get().strip()
    text = input_text.get("1.0", END).strip()
    if text:
        try:
            translated = GoogleTranslator(source=src, target=tgt).translate(text)
            output_text.delete("1.0", END)
            output_text.insert(END, translated)
        except Exception as e:
            output_text.delete("1.0", END)
            output_text.insert(END, f"Error: {e}")

def speak_text():
    text = output_text.get("1.0", END).strip()
    if text:
        tts = gTTS(text=text, lang=target_lang.get().strip())
        tts.save("speech.mp3")
        playsound("speech.mp3")
        os.remove("speech.mp3")

root = Tk()
root.title("Language Translator")
root.geometry("600x500")
root.config(bg="#f2f2f2")

Label(root, text="Enter Text:", font=("Arial", 12, "bold"), bg="#f2f2f2").pack(pady=5)
input_text = Text(root, height=6, width=60)
input_text.pack(pady=5)

frame = Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

Label(frame, text="Source Lang (e.g. 'auto'):", bg="#f2f2f2").grid(row=0, column=0, padx=5)
source_lang = StringVar(value='auto')
Entry(frame, textvariable=source_lang, width=10).grid(row=0, column=1, padx=5)

Label(frame, text="Target Lang (e.g. 'hi', 'fr', 'en'):", bg="#f2f2f2").grid(row=0, column=2, padx=5)
target_lang = StringVar(value='en')
Entry(frame, textvariable=target_lang, width=10).grid(row=0, column=3, padx=5)

Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
output_text = Text(root, height=6, width=60)
output_text.pack(pady=5)

Button(root, text="Speak Output", command=speak_text, bg="#2196F3", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

root.mainloop()
