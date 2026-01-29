import tkinter as tk
root = tk.Tk()
root.title("Address Entry Form")

# Khung chứa các trường nhập liệu (với viền nổi)
form_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=2)
form_frame.pack(padx=10, pady=10, fill="x")

# Danh sách các nhãn
labels = [
    "First Name:", "Last Name:", "Address Line 1:", 
    "Address Line 2:", "City:", "State/Province:", 
    "Postal Code:", "Country:"
]

# Tạo các hàng nhãn và ô nhập liệu bằng grid
for i, text in enumerate(labels):
    label = tk.Label(form_frame, text=text, anchor="e")
    label.grid(row=i, column=0, sticky="e", padx=5, pady=2)
    
    entry = tk.Entry(form_frame, width=40)
    entry.grid(row=i, column=1, padx=5, pady=2, sticky="we")

# Khung chứa các nút bấm
button_frame = tk.Frame(root)
button_frame.pack(fill="x", padx=10, pady=5)

# Nút Submit và Clear (căn lề phải)
btn_submit = tk.Button(button_frame, text="Submit", width=10)
btn_submit.pack(side="right", padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="Clear", width=10)
btn_clear.pack(side="right", padx=5, pady=5)

root.mainloop()