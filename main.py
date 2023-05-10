from tkinter_commands import *
import tkinter
from tkinter import messagebox

# States
MESSAGE_EMPTY = True
IMG_PATH_EMPTY = True

# Return messageboxes
def error_message(e: str) -> None:
    messagebox.showerror(title= "Error", message=e)

def success_message(e: str) -> None:
    messagebox.showinfo(title="Berhasil!", message=e)
    
# Get datas
def get_img_path():
    global IMG_PATH_EMPTY
    img_path = document_entry.get()
    if not img_path:
        IMG_PATH_EMPTY = True
    else:
        IMG_PATH_EMPTY = False
    return img_path

def get_message():
    global MESSAGE_EMPTY
    msg = message_textarea.get("1.0",'end-1c')
    if not msg:
        MESSAGE_EMPTY = True
        error_message("Pesan tidak boleh kosong")
    else:
        MESSAGE_EMPTY = False
    return msg

# Handlers below
def handler_add_data():
    # Get name and phone
    name = name_entry.get()
    phone = phone_entry.get()
    # error handling
    if not name:
        error_message("Nama tidak boleh kosong")
    if not phone:
        error_message("Nomor telfon tidak boleh kosong")
    # Add the data
    if name and phone:
        success = add_data(name, phone)
        # If successful
        if success:
            success_message("Data berhasil ditambahkan!")
            return
    # If error
    else:
        error_message(success)
    

def handler_send_to_all():
    message = get_message()
    img_path = get_img_path()
    # If image is not empty , then we send with picture.
    if not IMG_PATH_EMPTY and not MESSAGE_EMPTY:
        success = send_with_picture(msg= message, img_path=img_path)
        if success is True:
            success_message("Pesan anda telah dikirim ke semua kontak")
            return
    # If image is empty , then we send with no picture.
    elif IMG_PATH_EMPTY and not MESSAGE_EMPTY:
        success = send_to_all(message)
        if success is True:
            success_message("Pesan anda telah dikirim ke semua kontak")
            return
    # Create an error notification  
    else:  
        error_message(success)
        
def handler_message_in_range():
    # Get start and stop integer
    start = int(start_entry.get())
    stop = int(end_entry.get())
    # If one of them is not filled
    if not start or not stop:
        error_message("Mulai / Sampai tidak boleh kosong")
        return
    if start >= stop:
        error_message("Mulai harus lebih besar dari sampai.")
        return
    start-=1
    stop-=start
    # Get the image and message
    img_path = get_img_path()
    message = get_message()
    # If image is empty , then we send with no picture.
    if IMG_PATH_EMPTY and not MESSAGE_EMPTY:
        success = send_in_range(message, start, stop)
        if success is True:
            success_message(f"Pesan anda telah dikirim dari range {start} sampai {stop}.")
            return
    # If image is not empty , then we send with picture.
    elif not IMG_PATH_EMPTY and not MESSAGE_EMPTY:
        success = send_with_picture(msg= message, img_path=img_path, ranged=True, start=start, stop=stop)
        if success is True:
            success_message(f"Pesan anda telah dikirim dari range {start + 1} sampai {stop + 1}.")
            return
    # Create an error notification
    else:
        error_message(success)

# GUI Below
window = tkinter.Tk()
window.title("BENI Wa Blast")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="Tambah Nomor")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

name_label = tkinter.Label(user_info_frame, text="Nama")
name_label.grid(row=0, column=0)
phone_label = tkinter.Label(user_info_frame, text="Nomor Telf")
phone_label.grid(row=0, column=1)

name_entry = tkinter.Entry(user_info_frame)
name_entry.grid(row=1, column=0)
phone_entry = tkinter.Entry(user_info_frame)
phone_entry.grid(row=1, column=1)

add_user_button = tkinter.Button(user_info_frame, text="Tambah", command=handler_add_data)
add_user_button.grid(row=1, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Message info
message_data_frame = tkinter.LabelFrame(frame, text="Pesan")
message_data_frame.grid(row= 1, column=0, padx=20, pady=10)

message_label = tkinter.Label(message_data_frame, text="Pesan *")
message_label.grid(row=0, column=0)
document_label = tkinter.Label(message_data_frame, text="Path & Nama Photo")
document_label.grid(row=0, column=1)

message_textarea = tkinter.Text(message_data_frame, width=25, height=10)
message_textarea.grid(row=1, column=0)
document_entry = tkinter.Entry(message_data_frame)
document_entry.grid(row=1, column=1)

for widget in message_data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Send with range
send_with_range_frame =tkinter.LabelFrame(frame, text="Kirim dengan range")
send_with_range_frame.grid(row= 3, column=0, padx=20, pady=10)

start_label = tkinter.Label(send_with_range_frame, text="Mulai dari")
start_label.grid(row=0, column=0)
end_label = tkinter.Label(send_with_range_frame, text="Sampai dengan")
end_label.grid(row=0, column=1)

start_entry = tkinter.Spinbox(send_with_range_frame)
start_entry.grid(row=1, column=0)
end_entry = tkinter.Spinbox(send_with_range_frame)
end_entry.grid(row=1, column=1)

submit_button = tkinter.Button(send_with_range_frame, text="Kirim", command=handler_message_in_range)
submit_button.grid(row=1, column=2)

for widget in send_with_range_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Send to all button
send_to_all_frame = tkinter.LabelFrame(frame)
send_to_all_frame.grid(row=4, column=0, padx=20, pady=10)
send_to_all_button = tkinter.Button(send_to_all_frame, text="Kirim ke semua contact", command=handler_send_to_all)
send_to_all_button.grid(row=0, column=0, padx=20, pady=10, sticky='nesw')

 
window.mainloop()