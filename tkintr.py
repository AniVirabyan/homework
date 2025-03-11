
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import requests
import os

# Функция для получения данных о криптовалютах
def get_crypto_data(symbols):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(symbols),
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("API Response:", response.json())  # Отладочный вывод
        return response.json()
    else:
        print("Error fetching data:", response.status_code, response.text)  # Отладочный вывод
        return None

# Функция обработки файла и генерации отчёта
def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")])
    if not file_path:
        return
    
    with open(file_path, "r") as file:
        symbols = [line.strip().lower() for line in file.readlines()]
    
    print("Symbols to fetch:", symbols)  # Отладочный вывод
    data = get_crypto_data(symbols)
    if not data:
        messagebox.showerror("Error", "Failed to retrieve cryptocurrency data")
        return
    
    rows = []
    for symbol, info in data.items():
        rows.append([
            symbol.upper(),
            info.get("usd", "N/A"),
            info.get("usd_market_cap", "N/A"),
            info.get("usd_24h_vol", "N/A"),
            info.get("usd_24h_change", "N/A")
        ])
    
    df = pd.DataFrame(rows, columns=["Symbol", "Current Price (USD)", "Market Cap", "Total Volume", "24h Change (%)"])
    
    save_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx", initialdir=os.path.expanduser("~/Downloads"),
        filetypes=[("Excel Files", "*.xlsx")]
    )
    if save_path:
        df.to_excel(save_path, index=False)
        messagebox.showinfo("Success", f"Excel file saved: {save_path}")

# Создание GUI приложения
root = tk.Tk()
root.title("Crypto Data Fetcher")
root.geometry("400x200")

tk.Label(root, text="Upload a file with crypto symbols").pack(pady=10)
btn_upload = tk.Button(root, text="Upload File", command=process_file)
btn_upload.pack(pady=10)

root.mainloop()
