import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def shift_lrc_text(text, shift_ms):
    pattern = r"\[(\d+):(\d+)\.(\d+)\]"

    def replace_time(match):
        minutes = int(match.group(1))
        seconds = int(match.group(2))
        millis = int(match.group(3))

        total_ms = (minutes * 60 + seconds) * 1000 + millis
        total_ms += shift_ms

        if total_ms < 0:
            total_ms = 0

        new_minutes = total_ms // 60000
        new_seconds = (total_ms % 60000) // 1000
        new_millis = total_ms % 1000

        return f"[{new_minutes:02d}:{new_seconds:02d}.{new_millis:03d}]"

    return re.sub(pattern, replace_time, text)


def process_shift():
    input_text = input_box.get("1.0", tk.END)
    shift_value = shift_entry.get().strip()

    try:
        shift_seconds = float(shift_value)
    except ValueError:
        messagebox.showerror("エラー", "秒数は数値で入力してね")
        return

    shift_ms = int(shift_seconds * 1000)

    result = shift_lrc_text(input_text, shift_ms)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


# ===== GUI構築 =====

root = tk.Tk()
root.title("LRCタイムシフトツール")
root.geometry("1000x600")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill=tk.BOTH, expand=True)

top_frame = ttk.Frame(main_frame)
top_frame.pack(fill=tk.X)

ttk.Label(top_frame, text="ずらす秒数（例: -0.10 や 0.25）:").pack(side=tk.LEFT)

shift_entry = ttk.Entry(top_frame, width=10)
shift_entry.pack(side=tk.LEFT, padx=5)
shift_entry.insert(0, "-0.10")

shift_button = ttk.Button(top_frame, text="実行", command=process_shift)
shift_button.pack(side=tk.LEFT, padx=10)

text_frame = ttk.Frame(main_frame)
text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

input_box = tk.Text(text_frame, wrap=tk.NONE)
input_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_box = tk.Text(text_frame, wrap=tk.NONE)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()