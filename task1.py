import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short, should be at least 8 characters long.")
    elif len(password) >= 12:
        strength += 1
        feedback.append("Good length.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")
    
    if strength == 5:
        feedback.append("Your password is very strong!")
    elif strength >= 3:
        feedback.append("Your password is moderately strong.")
    else:
        feedback.append("Your password is weak, consider making it stronger.")

    return strength, "\n".join(feedback)

# Function to evaluate password and display feedback
def evaluate_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    messagebox.showinfo("Password Strength", feedback)

# Function to handle key press and temporarily show the typed character
def on_key_press(event):
    global full_password  # Track the full password
    
    # Handle backspace
    if event.keysym == "BackSpace":
        full_password = full_password[:-1]
    else:
        full_password += event.char

    password_entry.delete(0, tk.END)
    password_entry.insert(0, full_password)
    root.after(500, mask_password)  # Wait 500 ms before masking the last character
    
    # Update strength feedback
    update_strength_feedback()

# Function to mask the password with *
def mask_password():
    masked_password = '*' * len(full_password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, masked_password)

# Function to update the strength feedback label
def update_strength_feedback():
    password = full_password
    strength, _ = check_password_strength(password)
    
    if strength == 5:
        strength_label.config(text="Very Strong", fg="green")
    elif strength >= 3:
        strength_label.config(text="Moderately Strong", fg="orange")
    else:
        strength_label.config(text="Weak", fg="red")

# Setting up the main application window
root = tk.Tk()
root.title("Nathan's Password Checker")
root.geometry("400x400")
root.configure(bg="#2E4053")  # Dark blue background

# Track the full password
full_password = ""

# Title of the application
title_label = tk.Label(root, text="Nathan's Password Checker", font=("Helvetica", 18, "bold"), fg="white", bg="#2E4053")
title_label.pack(pady=20)

# Label for instruction
label = tk.Label(root, text="Enter your password:", font=("Helvetica", 14), fg="white", bg="#2E4053")
label.pack(pady=10)

# Entry field for password
password_entry = tk.Entry(root, width=30, fg="black", bg="#D5DBDB", highlightbackground="#1ABC9C", highlightthickness=2)
password_entry.pack(pady=10)
password_entry.bind("<KeyRelease>", on_key_press)  # Bind key release event to on_key_press function

# Strength feedback label
strength_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg="white", bg="#2E4053")
strength_label.pack(pady=10)

# Button to check password with a white background and black text
check_button = tk.Button(root, text="Check Password", command=evaluate_password, font=("Helvetica", 12), bg="white", fg="black", activebackground="#EAECEE", activeforeground="black")
check_button.pack(pady=20)

# Run the application
root.mainloop()