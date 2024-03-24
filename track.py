import pandas as pd
import webbrowser
import tkinter as tk
from tkinter import ttk

# function to refresh data based on the selected city
def refresh_data(event):
    selected_city = city_combobox.get()
    selected_geocode = city_geocodes[selected_city]
    
    # code for fetching and processing data
    url = f'https://info.dengue.mat.br/api/alertcity?geocode={selected_geocode}&disease=dengue'
    search_filter = (
        f'geocode={selected_geocode}&disease=dengue&format=csv&' +
        'ew_start=1&ew_end=50&ey_start=2024&ey_end=2024'
    )
    df = pd.read_csv('%s?%s' % (url, search_filter))
    
    # select and rename columns
    selected_columns = ['data_iniSE', 'SE', 'casos']
    selected_df = df[selected_columns].copy()
    selected_df.columns = ['Date', 'Week', 'Cases']
    
    # display the updated dataframe
    text.delete('1.0', tk.END)  # Clear existing text
    text.insert(tk.END, selected_df.to_string(index=False) + "\n")
    
    # update the label with city information only
    city_state_label.config(text=f"City: {selected_city}")

root = tk.Tk()
root.title("Dengue Track")
root.iconbitmap("ico/dengue.ico")

# city geocodes dictionary api has the numbers
city_geocodes = {'Brasilia - DF': '5300108', 'Camaçari - BA': '2905701', 'Rio de Janeiro - RJ': '3304557', 'São Paulo - SP': '3550308'}

# create a label for city information only
city_state_label = tk.Label(root, text="Cidade: ", font=("Helvetica", 12))
city_state_label.pack(pady=5)

# create a combobox for city selection
city_combobox = ttk.Combobox(root, values=list(city_geocodes.keys()))
city_combobox.pack(pady=5)
city_combobox.set(list(city_geocodes.keys())[0])  # set the default city
city_combobox.bind("<<ComboboxSelected>>", refresh_data)  

# create a text widget to display the data
text = tk.Text(root, height=10, width=40)
text.pack()

made_by_label = tk.Label(root, text="Made by Wesley", font=("Helvetica", 10))
made_by_label.pack(pady=2)

# gitHub repository
github_link = tk.Label(root, text="GitHub", font=("Helvetica", 10), fg="blue", cursor="hand2")
github_link.pack(pady=2)
github_link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/iw3ll"))

refresh_data(None)

root.mainloop()