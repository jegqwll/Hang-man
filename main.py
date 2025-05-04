from tkinter import *
from tkinter import messagebox
import random

word_list = ["python", "hangman", "bomb", "explosion", "fire"]
word = random.choice(word_list).upper()
guessed_letters = set()
wrong_letters = []
wrong_guesses = 0
max_mistakes = 5

root = Tk()
root.title("Hang man")
root.configure(bg="white")

frames = [PhotoImage(file=f"bomboclad/{i}.gif") for i in range(1, 158)]
normal_frames = frames[:40]
explosion_frames = frames[40:]

bomb_label = Label(root, image=normal_frames[0], bg="white")
bomb_label.pack()

word_label = Label(root, text="_ " * len(word), font=("Arial", 24), bg="white")
word_label.pack()

wrong_label = Label(root, text="Mistakes: ", font=("Arial", 14), fg="red", bg="white")
wrong_label.pack()

entry = Entry(root, font=("Arial", 18))
entry.pack()

def update_display():
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    word_label.config(text=display_word)
    wrong_label.config(text="Mistakes: " + " ".join(wrong_letters))
    if "_" not in display_word:
        messagebox.showinfo("Win", "You guessed the word!")
        root.quit()

def animate_burn(start_frame, end_frame, callback=None):
    def show_frame(frame_idx):
        if frame_idx < end_frame - 1:
            bomb_label.config(image=frames[frame_idx])
            root.after(100, show_frame, frame_idx + 1)
        else:
            if callback:
                callback()
    show_frame(start_frame)

def start_explosion():
    def game_over_massage():
        messagebox.showinfo("Loss", f'You lost! The word was {word}')
        root.quit()
    
    animate_burn(40, 158, game_over_massage)
    
def check_letter(event=None):
    global wrong_guesses
    letter = entry.get().upper()
    entry.delete(0, END)
    if len(letter) == 1 and letter.isalpha() and letter not in guessed_letters:
        guessed_letters.add(letter)
        if letter not in word:
            wrong_guesses +=1
            wrong_letters.append(letter)
            if wrong_guesses <= max_mistakes:
                start_frame = (wrong_guesses - 1)*8
                end_frame = min(start_frame +8, 40)
                animate_burn(start_frame, end_frame, update_display)
            if wrong_guesses == max_mistakes:
                start_explosion()
        else:
            update_display()
            
    

check_button = Button(root, text="Check", font=("Arial", 14), command=check_letter)
check_button.pack()

root.bind("<Return>", check_letter)

update_display()
root.mainloop()
