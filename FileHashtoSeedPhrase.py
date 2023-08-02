import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
from mnemonic import Mnemonic
from web3 import Account
Account.enable_unaudited_hdwallet_features()


def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            bytes = f.read()
            readable_hash = hashlib.sha256(bytes).hexdigest()
            return readable_hash
    except Exception as e:
        messagebox.showerror("Error", str(e))


def choose_file():
    filename = filedialog.askopenfilename()
    if filename != '':
        try:
            filename_entry.delete(0, tk.END)
            filename_entry.insert(0, filename)
            file_hash = calculate_hash(filename_entry.get())
            binary_seed = bytes.fromhex(file_hash)
            mnemo = Mnemonic("english")
            seed_phrase = mnemo.to_mnemonic(binary_seed)
            seed_text.delete('1.0', tk.END)
            seed_text.insert(tk.END, seed_phrase)
            generate_wallet()
        except Exception as e:
            messagebox.showerror("Error", str(e))


def generate_wallet(event=None):
    account = Account.from_mnemonic(mnemonic=seed_text.get('1.0', 'end-1c'), passphrase=passphrase_entry.get(), account_path="m/44'/60'/0'/0/0")
    wallet0_prv_text.delete('1.0', tk.END)
    wallet0_prv_text.insert(tk.END, account._private_key.hex())
    wallet0_add_text.delete('1.0', tk.END)
    wallet0_add_text.insert(tk.END, account.address)


root = tk.Tk()
root.title('File hash to SeedPhrase with PassPhrase check')

choose_file_button = tk.Button(root, text="Choose File...", command=choose_file)
choose_file_button.pack(pady=10)

filename_entry = tk.Entry(root, width=100)
filename_entry.pack(pady=10)
filename_entry.insert(0, "Enter file path here")

seed_label = tk.Label(root, text="Seed Phrase from File Hash (or enter manually):")
seed_label.pack()
seed_text = tk.Text(root, width=80, height=3)
seed_text.pack(pady=10)
seed_text.bind('<KeyRelease>', generate_wallet)

passphrase_label = tk.Label(root, text="Enter passphrase here (optional)")
passphrase_label.pack()
passphrase_entry = tk.Entry(root, width=80)
passphrase_entry.pack(pady=10)
passphrase_entry.insert(0, "")
passphrase_entry.bind('<KeyRelease>', generate_wallet)

wallet0_prv_label = tk.Label(root, text="Derived ETH Wallet #0 Private Key")
wallet0_prv_label.pack()
wallet0_prv_text = tk.Text(root, width=80, height=1)
wallet0_prv_text.pack(pady=10)

wallet0_add_label = tk.Label(root, text="Derived ETH Wallet #0 Address")
wallet0_add_label.pack()
wallet0_add_text = tk.Text(root, width=60, height=1)
wallet0_add_text.pack(pady=10)

root.mainloop()
