# 💣 Hangman Bomb Game

This is a unique take on the classic *Hangman* game — instead of a stick figure, a burning bomb animation is used. If the player makes too many mistakes, the bomb explodes! The game is built using Python and the `tkinter` library.

## 📸 Screenshot (Example)

_Add a screenshot here if you'd like to show how the game looks._

## 📦 Requirements

- Python 3.7+
- Standard `tkinter` library (usually included with Python)

## 🗂 Project Structure

```
project/
├── main.py
├── bomboclad/
│   ├── 1.gif
│   ├── 2.gif
│   ├── ...
│   └── 157.gif
```

> The `bomboclad/` folder must contain **157 GIF frames**: 40 for the fuse animation and 117 for the explosion.

## ▶️ Running the Game

```bash
python main.py
```

## 🎮 Controls

- Type a letter into the entry field and press **Enter** or click **Check**
- Guess the word before the bomb explodes (maximum 5 mistakes)

## 🔥 Features

- Unique bomb fuse animation as a countdown
- Explosion sequence on game over
- Random word selection from a preset list
- Simple GUI built with `tkinter`

## 📄 License

MIT License
