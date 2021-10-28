import tkinter as tk

def kg_to_lbs():
    kilogram = ent_weight.get()
    pounds = int(kilogram) * 2.2046
    lbl_result["text"] = f"{round(pounds, 2)}", "lbs"

def lbs_to_kg():
    pounds = ent_weight2.get()
    kilogram = int(pounds) / 2.2046
    lbl_result["text"] = f"{round(kilogram, 2)}", "kg"

window = tk.Tk() 
window.title("Weight Converter") # Navnet som kommer opp på selve vinduet, "navnet på programmet"

frm_entry = tk.Frame(master=window)
ent_weight = tk.Entry(master=frm_entry, width=10)
lbl_weight = tk.Label(master=frm_entry, text="kg")

frm_entry2 = tk.Frame(master=window)
ent_weight2 = tk.Entry(master=frm_entry, width=10)
lbl_weight2 = tk.Label(master=frm_entry, text="lbs")

ent_weight.grid(row=0, column=0, sticky="n")
lbl_weight.grid(row=0, column=1, sticky="w")

ent_weight2.grid(row=3, column=0, sticky="n")
lbl_weight2.grid(row=3, column=1, sticky="w")

# btn_convert lager en knapp, konverterer vekten med definisjonen over
btn_convert = tk.Button(
    width = 2,
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}", # Dette er det så står inni knappen, "\N"{} Er for ett symbol.
    command = kg_to_lbs # Her henter den kg_to_lbs, som ble definert på linje 3
)

btn_convert2 = tk.Button(
    width = 2,
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command = lbs_to_kg # Her henter den lbs_to_kg, som ble defintert på linje 8. motsatt som "btn_convert"
)

lbl_result = tk.Label(master=window, text="Converted \n weight")

#Dette setter funksjonene inn i vinduet.
frm_entry.grid(row=1, column=0, padx=20, pady= 7)
frm_entry2.grid(row=3, column=0, padx=20, pady = 7)
btn_convert.grid(column=1, row=1, sticky="n", pady= 1)
btn_convert2.grid(column=1, row=1, sticky="s", pady = 1)
lbl_result.grid(row=1, column=2, padx=10)

window.mainloop()