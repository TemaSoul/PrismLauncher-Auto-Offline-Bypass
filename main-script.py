from art import tprint
from simple_term_menu import TerminalMenu
import os
import json

tprint("Prism-Auto-Offline-Bypass")
print("Что вы используете?")
menu = TerminalMenu(['Linux', 'Linux(Flatpak)', 'MacOS'])
selected_index = menu.show()

options = ['Linux', 'Linux(Flatpak)', 'MacOS']
selected_system = options[selected_index]
print(f"\nВыбрана система: {selected_system}")

# Выполнение
account_data = {
    "accounts": [{
        "entitlement": {"canPlayMinecraft": True, "ownsMinecraft": True},
        "type": "MSA"
    }],
    "formatVersion": 3
}

if selected_index == 0:  # Linux
    file_path = os.path.expanduser("~/.local/share/PrismLauncher/accounts.json")
elif selected_index == 1:  # Linux (Flatpak)
    file_path = os.path.expanduser("~/.var/app/org.prismlauncher.PrismLauncher/data/PrismLauncher/accounts.json")
elif selected_index == 2:  # MacOS
    file_path = os.path.expanduser("~/Library/Application Support/PrismLauncher/accounts.json")

# Записываем JSON
with open(file_path, 'w') as f:
    json.dump(account_data, f, indent=2)

print(f"Успешно! Файл создан: {file_path}")
print("\nГотово!")















