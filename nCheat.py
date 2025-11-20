import customkinter as ctk
import pymem

# config

APP_SIZE = "420x220"
FONT = ("Montserrat ExtraBold",13)

# pymem

pm = pymem.Pymem("GAME_NAME.exe")
module_base = pymem.process.module_from_name(
    pm.process_handle, "GAME_NAME.exe"
).lpBaseOfDll

# functions

def GODMODE(enable: bool):
    adress = module_base + YOUR_ADRESS
    if enable:
        pm.write_bytes(adress, b"\x90" * 100, 8) # 100 is for health (adjust if needed)
        return "godmode enabled!", "green"
    else:
        original_bytes = b"\YOURBYTES\YOURBYTES"
        pm.write_bytes(adress,original_bytes,len(original_bytes))
        return "godmode disabled!", "red"
    
def set_money(new_money: int):
    pm.write_int(module_base + YOURBYTE,new_money)
    return f"Money set to {new_money}", "green"

ctk.set_appearance_made("dark")
ctk.set_default_color_theme("red")

app = ctk.CTk()
app.title("nCheat Vers. 1.0")
app.geometry(APP_SIZE)

frame = ctk.CTkFrame(app)
frame.pack(pady=20,padx=20, fill="both",expand=True)

def toggle_health():
    msg, color = set_infinite_health(checkbox.get())
    status.set(msg)
    status_label.configure(text_color=color)

checkbox = ctk.CTkCheckBox(frame,texdt="GOD MODE", font=FONT,command=toggle_health)
checkbox.pack(anchor="w",pady=10)

ctk.CTkLabel(frame,text="money", font=FONT).pack(anchor="w", pady=(10,0))
input_frame = ctk.CTkFrame(frame,fg_color="transparent")
input.frame.pack(fill="x",pady=8)

entry = ctk.CTkEntry(input_frame,placeholder_text="Change Money val...")
entry.pack(side="left",fill="x",expand=True,padx=(0,8))

def confirm_money():
    try:
        value = int(entry.get() or 0)
        msg, color = set_money(value)
        status.set(msg)
        status_label.configure(text_color=color)
    except ValueError:
        status.set("invalid value")
        status_label.configure(text_color="yellow")

ctk.CTkButton(input_frame,text="Confirm", font=FONT,command=confirm_money).pack(side="right")
status = ctk.StringVar(val="Ready")
status_label = ctk.CTkLabel(frame,textvariable=status, font=FONT,text_color="green")
status_label.pack(anchor="w", pady=(15,0))

app.mainloop()