import random                              # Import the random module to select random words and characters
import tkinter as tk                      # Import tkinter for GUI elements
from tkinter import filedialog, messagebox  # Import dialog and message tools from tkinter
import os  # Add this at the top if not already present
import tkinter.ttk as ttk  # Add this for the slider

# 📝 Lists of words to use in password generation
# Each list contains 50 words, and we randomly choose one word from each to form a passphrase

# List of adjectives (descriptive words)
adjectives = [
    "Happy", "Cactus", "Tiger", "Velvet", "Monkey", "Silent", "Bubble",
    "Magic", "Frozen", "Dizzy", "Golden", "Solar", "Echo", "Lunar", "Storm",
    "Arctic", "Waffle", "Puzzle", "Nebula", "Rocket", "Brave", "Bouncy",
    "Chilly", "Cozy", "Dusty", "Fancy", "Grumpy", "Jolly", "Lofty",
    "Nimble", "Plucky", "Quirky", "Rusty", "Snappy", "Twisty", "Vivid",
    "Whimsical", "Zesty", "Nifty", "Tasty", "Witty", "Gloomy", "Cheery",
    "Swift", "Silly", "Meek", "Zany", "Yawning"
]

# List of nouns (naming words)
nouns = [
    "Hammer", "Planet", "Salad", "Mirror", "Cactus", "Shadow", "Forest",
    "Candle", "Pencil", "Dagger", "Melon", "Feather", "Zebra", "Coffee",
    "Sunset", "Panther", "Breeze", "Scooter", "Knight", "Guitar", "Helmet",
    "Rocket", "Lantern", "Toaster", "Jungle", "Pickle", "Puzzle",
    "Castle", "Donut", "Sofa", "Ladder", "Igloo", "Banana", "Volcano",
    "Tornado", "Cabin", "Canyon", "Cricket", "Walrus", "Lobster", "Pelican",
    "Treasure", "Anchor", "Piano", "Planet", "Whistle", "Bridge", "Tunnel"
]

# List of verbs (action words)
verbs = [
    "Run", "Jump", "Fly", "Build", "Craft", "Think", "Drive", "Zoom",
    "Climb", "Spin", "Catch", "Throw", "Grow", "Blink", "Slide",
    "Shout", "Drift", "Push", "Pull", "Dig", "Tinker", "Toss",
    "Launch", "Hide", "Peek", "Search", "Spin", "Race", "Dash",
    "Sketch", "Whistle", "March", "Glide", "Roar", "Sniff", "Whirl",
    "Bounce", "Kick", "Snap", "Doodle", "Ramble", "Nudge", "Peek",
    "Forge", "Shape", "Lift", "Wander", "Sprint", "Hover"
]

# List of adverbs (describing how actions are done)
adverbs = [
    "Quickly", "Silently", "Bravely", "Happily", "Eagerly", "Lazily", "Carefully",
    "Boldly", "Gently", "Loudly", "Quietly", "Rapidly", "Smoothly", "Calmly",
    "Brightly", "Sadly", "Cheerfully", "Roughly", "Wildly", "Slowly", "Warmly",
    "Softly", "Sharply", "Neatly", "Messily", "Proudly", "Wisely", "Fiercely",
    "Cleverly", "Oddly", "Boldly", "Briskly", "Gladly", "Rudely", "Sweetly",
    "Kindly", "Roughly", "Easily", "Barely", "Truly", "Simply", "Boldly",
    "Bravely", "Freely", "Openly", "Neatly", "Quickly", "Smoothly", "Swiftly"
]

# List of allowed special characters for password endings
allowed_symbols = ['-', '(', ')', '.', '&', '@', '?', "'", '#', ',', '/', ';', '+']

# 🔐 Function to generate one password in the format: Adjective-Noun-Verb<digit><symbol>
def generate_password():
    adverb = random.choice(adverbs)                                 # Randomly pick one adverb
    adjective = random.choice(adjectives)                           # Randomly pick one adjective
    noun = random.choice(nouns)                                     # Randomly pick one noun
    verb = random.choice(verbs)                                     # Randomly pick one verb
    digit = str(random.randint(0, 9))                               # Pick a random digit 0-9 and convert to string
    symbol = random.choice(allowed_symbols)                         # Pick a random symbol from allowed list
    return f"{adjective}-{noun}-{verb}{digit}{symbol}-{adverb}"     # Return formatted password

# --- Update generate_and_display to use new controls ---
def generate_and_display():
    try:
        count = get_count()
        if count <= 0:
            raise ValueError

        passwords = [generate_password() for _ in range(count)]

        # Output to file
        if save_to_file_var.get():
            output_file = file_path_var.get()
            with open(output_file, 'w') as file:
                for password in passwords:
                    file.write(password + '\n')
            messagebox.showinfo("Success", f"{count} passwords saved to {output_file}")

        # Output to display
        if display_var.get():
            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)
            for password in passwords:
                output_box.insert(tk.END, password + '\n')
            output_box.config(state="normal")
        else:
            output_box.delete("1.0", tk.END)

        # Copy to clipboard
        if copy_var.get():
            root.clipboard_clear()
            root.clipboard_append('\n'.join(passwords))
            messagebox.showinfo("Copied", "Passwords copied to clipboard.")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number of passwords.")

# 🚀 Setup the GUI window using Tkinter
root = tk.Tk()
root.title("Passphrase Generator")
root.geometry("800x600")  # Bigger window

# --- Styles for accessibility ---
BIG_FONT = ("Segoe UI", 16)
MONO_FONT = ("Consolas", 16)

# --- Output options frame at the top ---
output_options_frame = tk.Frame(root)
output_options_frame.pack(fill="x", pady=10, padx=10)

# --- Checkbox style for bigger checkboxes ---
style = ttk.Style()
style.configure("Big.TCheckbutton", font=("Segoe UI", 20))

# Select/Deselect all checkboxes with dynamic text
select_all_var = tk.BooleanVar(value=True)
def update_select_all_text():
    if select_all_var.get():
        chk_select_all.config(text="All options below on")
    else:
        chk_select_all.config(text="All options below off")
def toggle_all():
    val = select_all_var.get()
    save_to_file_var.set(val)
    display_var.set(val)
    copy_var.set(val)
    update_select_all_text()
select_all_var.trace_add("write", lambda *args: update_select_all_text())
chk_select_all = ttk.Checkbutton(
    output_options_frame,
    text="All options below on",
    variable=select_all_var,
    style="Big.TCheckbutton",
    command=toggle_all
)
chk_select_all.grid(row=0, column=0, columnspan=4, sticky="w", pady=(0,10))

# Output to file
save_to_file_var = tk.BooleanVar(value=True)
chk_save_to_file = ttk.Checkbutton(
    output_options_frame,
    text="Output to file",
    variable=save_to_file_var,
    style="Big.TCheckbutton"
)
chk_save_to_file.grid(row=1, column=0, sticky="w", pady=(0,0))

# File path entry and browse button, indented and resizable
file_path_frame = tk.Frame(output_options_frame)
file_path_frame.grid(row=2, column=0, columnspan=4, sticky="ew", padx=(40,0), pady=(0,10))
output_options_frame.grid_columnconfigure(0, weight=1)
file_path_frame.grid_columnconfigure(0, weight=1)
file_path_frame.grid_columnconfigure(1, weight=0)

default_path = os.path.join(os.getcwd(), "passphrases.txt")
file_path_var = tk.StringVar(value=default_path)
entry_file_path = tk.Entry(file_path_frame, textvariable=file_path_var, font=BIG_FONT)
entry_file_path.grid(row=0, column=0, sticky="ew", padx=(0,5))
def browse_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        initialfile="passphrases.txt"
    )
    if file:
        file_path_var.set(file)
btn_browse = tk.Button(file_path_frame, text="Browse", font=BIG_FONT, command=browse_file)
btn_browse.grid(row=0, column=1, sticky="ew")

# Output to display
display_var = tk.BooleanVar(value=True)
chk_display = ttk.Checkbutton(
    output_options_frame,
    text="Display down below",
    variable=display_var,
    style="Big.TCheckbutton"
)
chk_display.grid(row=3, column=0, sticky="w", pady=(0,0))

# Copy to clipboard below display
copy_var = tk.BooleanVar(value=True)
chk_copy = ttk.Checkbutton(
    output_options_frame,
    text="Copy to clipboard",
    variable=copy_var,
    style="Big.TCheckbutton"
)
chk_copy.grid(row=4, column=0, sticky="w", pady=(0,0))

# --- Number of passwords slider ---
slider_frame = tk.Frame(root)
slider_frame.pack(fill="x", pady=10)
label_count = tk.Label(slider_frame, text="Number of passwords:", font=BIG_FONT)
label_count.pack(side=tk.LEFT, padx=(0,10))

def slider_tick(val):
    val = int(float(val))
    if val < 25:
        slider.set(1)
    elif val % 25 != 0:
        slider.set(round(val / 25) * 25)
    entry_count_var.set(str(int(slider.get())))

slider = tk.Scale(
    slider_frame, from_=1, to=200, orient="horizontal", length=400,
    showvalue=0, tickinterval=25, resolution=1, font=BIG_FONT, command=slider_tick
)
slider.set(25)
slider.pack(side=tk.LEFT, fill="x", expand=True)

entry_count_var = tk.StringVar(value="25")
entry_count = tk.Entry(slider_frame, width=5, font=BIG_FONT, textvariable=entry_count_var, state="readonly")
entry_count.pack(side=tk.LEFT, padx=10)

def get_count():
    return int(entry_count_var.get())

# --- Generate button ---
btn_generate = tk.Button(root, text="Generate", font=BIG_FONT, command=lambda: generate_and_display())
btn_generate.pack(pady=10)

# --- Output box (multi-line text area) ---
output_box = tk.Text(root, font=MONO_FONT, wrap="none")
output_box.pack(fill="both", expand=True, padx=10, pady=10, anchor="sw")

# Make output_box resize with window
output_box.config(height=1)
root.grid_rowconfigure(99, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the Tkinter event loop to run the GUI app
root.mainloop()
