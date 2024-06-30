import tkinter as tk
from tkinter import messagebox

# Define the submit_form function
def submit_form():
    name = entry_widgets[0].get()
    email = entry_widgets[1].get()
    age = entry_widgets[2].get()
    phone_number = entry_widgets[3].get()
    village = entry_widgets[4].get()
    pincode = entry_widgets[5].get()
    country = entry_widgets[6].get()
    state = entry_widgets[7].get()
    gender = gender_var.get()
    father_name = entry_widgets[8].get()
    mother_name = entry_widgets[9].get()
    father_number = entry_widgets[10].get()
    mother_number = entry_widgets[11].get()

    # Print or process the collected data as needed
    print("Name:", name)
    print("Email:", email)
    print("Age:", age)
    print("Phone Number:", phone_number)
    print("Village:", village)
    print("Pincode:", pincode)
    print("Country:", country)
    print("State:", state)
    print("Gender:", gender)
    print("Father's Name:", father_name)
    print("Mother's Name:", mother_name)
    print("Father's Number:", father_number)
    print("Mother's Number:", mother_number)

    # Optional: Show a message box indicating successful submission
    messagebox.showinfo("Success", "Registration Successful!")

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the width and height of the window and calculate the x and y coordinates
window_width = 400
window_height = 600
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the window size and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create and place widgets
heading_label = tk.Label(root, text="REGISTRATION FORM", font=("Arial", 16))
heading_label.pack(pady=20)

fields_frame = tk.Frame(root)
fields_frame.pack()

# Entry fields
fields = ["Name", "Email", "Age", "Phone Number", "Village", "Pincode", "Country", "State", "Father's Name", "Mother's Name", "Father's Number", "Mother's Number"]
entry_widgets = []

for i, field in enumerate(fields):
    label = tk.Label(fields_frame, text=field + ":")
    label.grid(row=i, column=0, sticky="e", pady=5)
    entry = tk.Entry(fields_frame)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_widgets.append(entry)

# Gender radio buttons
gender_var = tk.StringVar(value="Male")
gender_label = tk.Label(fields_frame, text="Gender:")
gender_label.grid(row=len(fields), column=0, sticky="e", pady=5)
male_radio = tk.Radiobutton(fields_frame, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=len(fields), column=1, padx=10, pady=5, sticky="w")
female_radio = tk.Radiobutton(fields_frame, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=len(fields)+1, column=1, padx=10, pady=5, sticky="w")

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()
