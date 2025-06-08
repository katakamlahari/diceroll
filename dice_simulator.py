import tkinter as tk
import random

class DiceGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Roll Simulator - Two Players")
        self.root.geometry("600x700")
        self.root.configure(bg="#2C3E50")
        self.root.resizable(False, False)

        self.dice_unicode = {
            1: "\u2680", 2: "\u2681", 3: "\u2682",
            4: "\u2683", 5: "\u2684", 6: "\u2685"
        }

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        tk.Label(self.root, text="🎲 Dice Roll Simulator",
                 font=("Helvetica", 20, "bold"), fg="white",
                 bg="#2C3E50").pack(pady=10)

        # Winning Score Input
        self.win_frame = tk.Frame(self.root, bg="#2C3E50")
        self.win_frame.pack(pady=5)

        tk.Label(self.win_frame, text="Set Winning Score: ",
                 font=("Helvetica", 12), fg="white",
                 bg="#2C3E50").pack(side="left")
        self.win_entry = tk.Entry(self.win_frame, width=5, font=("Helvetica", 12))
        self.win_entry.pack(side="left", padx=5)
        self.win_entry.insert(0, "50")

        self.set_win_btn = tk.Button(self.win_frame, text="Set",
                                     command=self.set_winning_score,
                                     bg="#2980B9", fg="white",
                                     font=("Helvetica", 10, "bold"))
        self.set_win_btn.pack(side="left", padx=5)

        # Player area
        self.dice_frame = tk.Frame(self.root, bg="#34495E", pady=20)
        self.dice_frame.pack(pady=10)

        self.p1_label = tk.Label(self.dice_frame, text="Player 1",
                                 font=("Helvetica", 14, "bold"),
                                 fg="#E74C3C", bg="#34495E")
        self.p1_label.grid(row=0, column=0, padx=20)

        self.p2_label = tk.Label(self.dice_frame, text="Player 2",
                                 font=("Helvetica", 14, "bold"),
                                 fg="#3498DB", bg="#34495E")
        self.p2_label.grid(row=0, column=1, padx=20)

        self.p1_dice = tk.Label(self.dice_frame, text=self.dice_unicode[1],
                                font=("Arial", 80), fg="#E74C3C", bg="#34495E")
        self.p1_dice.grid(row=1, column=0, padx=20, pady=10)

        self.p2_dice = tk.Label(self.dice_frame, text=self.dice_unicode[1],
                                font=("Arial", 80), fg="#3498DB", bg="#34495E")
        self.p2_dice.grid(row=1, column=1, padx=20, pady=10)

        self.p1_score_label = tk.Label(self.dice_frame, text="Score: 0",
                                       font=("Helvetica", 12),
                                       fg="#E74C3C", bg="#34495E")
        self.p1_score_label.grid(row=2, column=0)

        self.p2_score_label = tk.Label(self.dice_frame, text="Score: 0",
                                       font=("Helvetica", 12),
                                       fg="#3498DB", bg="#34495E")
        self.p2_score_label.grid(row=2, column=1)

        # Buttons
        self.button_frame = tk.Frame(self.root, bg="#2C3E50")
        self.button_frame.pack(pady=15)

        self.roll_button = tk.Button(self.button_frame,
                                     text="Roll Dice",
                                     command=self.roll_dice,
                                     font=("Helvetica", 14, "bold"),
                                     bg="#27AE60", fg="white",
                                     width=15)
        self.roll_button.grid(row=0, column=0, padx=10)

        self.reset_button = tk.Button(self.button_frame,
                                      text="Reset Game",
                                      command=self.reset_game,
                                      font=("Helvetica", 14, "bold"),
                                      bg="#C0392B", fg="white",
                                      width=15)
        self.reset_button.grid(row=0, column=1, padx=10)

        self.status_label = tk.Label(self.root,
                                     text="Player 1's turn",
                                     font=("Helvetica", 12, "italic"),
                                     fg="white", bg="#2C3E50")
        self.status_label.pack(pady=10)

    def set_winning_score(self):
        try:
            score = int(self.win_entry.get())
            if score <= 0:
                raise ValueError
            self.winning_score = score
            self.status_label.config(text=f"Winning Score set to {self.winning_score}")
        except ValueError:
            self.status_label.config(text="Enter a valid positive number!")

    def roll_dice(self):
        roll = random.randint(1, 6)

        if self.current_player == 1:
            self.p1_dice.config(text=self.dice_unicode[roll])
            self.p1_score += roll
            self.p1_score_label.config(text=f"Score: {self.p1_score}")
            if self.p1_score >= self.winning_score:
                self.status_label.config(text="🎉 Player 1 Wins!")
                self.roll_button.config(state="disabled")
                return
            self.current_player = 2
            self.status_label.config(text="Player 2's turn")
        else:
            self.p2_dice.config(text=self.dice_unicode[roll])
            self.p2_score += roll
            self.p2_score_label.config(text=f"Score: {self.p2_score}")
            if self.p2_score >= self.winning_score:
                self.status_label.config(text="🎉 Player 2 Wins!")
                self.roll_button.config(state="disabled")
                return
            self.current_player = 1
            self.status_label.config(text="Player 1's turn")

    def reset_game(self):
        self.p1_score = 0
        self.p2_score = 0
        self.current_player = 1
        self.winning_score = int(self.win_entry.get()) if self.win_entry.get().isdigit() else 50

        self.p1_score_label.config(text="Score: 0")
        self.p2_score_label.config(text="Score: 0")
        self.p1_dice.config(text=self.dice_unicode[1])
        self.p2_dice.config(text=self.dice_unicode[1])
        self.status_label.config(text="Player 1's turn")
        self.roll_button.config(state="normal")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DiceGameApp(root)
    root.mainloop()
