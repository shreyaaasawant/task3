import tkinter as tk
import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        number_criteria,
        special_criteria
    ])
    
    feedback = []
    
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character.")
    
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }
    
    return {
        "strength_score": strength_score,
        "strength": strength_levels[strength_score],
        "feedback": feedback
    }

class PasswordStrengthChecker:
    def __init__(self, master):
        self.master = master
        master.title("Password Strength Checker")
        
        self.password_label = tk.Label(master, text="Enter Password:", font=("Helvetica", 12))
        self.password_label.pack(pady=10)
        
        self.password_entry = tk.Entry(master, width=30, font=("Helvetica", 12))
        self.password_entry.pack(pady=10)
        
        self.check_button = tk.Button(master, text="Check Password Strength", command=self.check_password, 
                                       bg="green", fg="white", font=("Helvetica", 12))
        self.check_button.pack(pady=10)
        
        self.result_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
        
        self.feedback_text = tk.Text(master, width=40, height=5, font=("Helvetica", 12))
        self.feedback_text.pack(pady=(10, 20))  # Increased bottom padding
        
    def check_password(self):
        password = self.password_entry.get()
        result = check_password_strength(password)
        
        self.result_label.config(text=f"Password Strength: {result['strength']}")
        
        self.feedback_text.delete(1.0, tk.END)
        for feedback in result['feedback']:
            self.feedback_text.insert(tk.END, f"- {feedback}\n")

root = tk.Tk()
root.geometry("400x350")  # Increased window height
my_gui = PasswordStrengthChecker(root)
root.mainloop()
