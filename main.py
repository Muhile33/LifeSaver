# main.py
from tracker import log_entry, load_data
from quotes import get_quote
from datetime import datetime
import time

def time_since_last(substance):
    data = load_data()
    entries = [e for e in data["entries"] if e["substance"] == substance]
    if not entries:
        return "No entries yet."
    last_time = datetime.fromisoformat(entries[-1]["timestamp"])
    diff = datetime.now() - last_time
    return f"{substance.capitalize()}: {diff}"

def main():
    while True:
        print("\n📊 Life Saver")
        print("1. Log Vape")
        print("2. Log Smoke")
        print("3. Log Drink")
        print("4. Show Time Since Last Use")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            log_entry("vape")
            print("✅ Logged vape.")
        elif choice == "2":
            log_entry("smoke")
            print("✅ Logged smoke.")
        elif choice == "3":
            log_entry("drink")
            print("✅ Logged drink.")
        elif choice == "4":
            for sub in ["vape", "smoke", "drink"]:
                print(time_since_last(sub))
        elif choice == "5":
            print(get_quote())
            break
        else:
            print("Invalid choice.")
        time.sleep(1)

if __name__ == "__main__":
   main() 
