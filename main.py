import random                              # Import the random module to select random words and characters
import tkinter as tk                      # Import tkinter for GUI elements
from tkinter import filedialog, messagebox  # Import dialog and message tools from tkinter

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

# List of allowed special characters for password endings
allowed_symbols = ['-', '(', ')', '.', '&', '@', '?', "'", '#', ',', '/', ';', '+']

# 🔐 Function to generate one password in the format: Adjective-Noun-Verb<digit><symbol>
def generate_password():
    adjective = random.choice(adjectives)            # Randomly pick one adjective
    noun = random.choice(nouns)                      # Randomly pick one noun
    verb = random.choice(verbs)                      # Randomly pick one verb
    digit = str(random.randint(0, 9))                # Pick a random digit 0-9 and convert to string
    symbol = random.choice(allowed_symbols)          # Pick a random symbol from allowed list
    return f"{adjective}-{noun}-{verb}{digit}{symbol}"  # Return formatted password

# ✍️ Function to generate and display passwords in the GUI and save to a file
def generate_and_display():
    try:
        count = int(entry_count.get())  # Read number of passwords to generate from entry box
        if count <= 0:
            raise ValueError  # If the number is not positive, raise an error

        # Ask user to choose a file location and name for saving passwords
        output_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if not output_file:
            return  # Exit if user cancels the file dialog

        # Open the file for writing
        with open(output_file, 'w') as file:
            output_box.delete("1.0", tk.END)  # Clear the output text box in GUI first
            for _ in range(count):
                password = generate_password()  # Generate a new password
                output_box.insert(tk.END, password + '\n')  # Show password in GUI
                file.write(password + '\n')  # Save password to file

        # Show success popup
        messagebox.showinfo("Success", f"{count} passwords saved to {output_file}")

    except ValueError:
        # Show error popup if input is invalid (non-integer or less than 1)
        messagebox.showerror("Invalid input", "Please enter a valid number of passwords.")

# 🚀 Setup the GUI window using Tkinter
root = tk.Tk()                      # Create the main window object
root.title("Passphrase Generator")  # Set the window title
root.geometry("500x400")            # Set the size of the window

# Create a frame to hold label and entry input for number of passwords
frame = tk.Frame(root)
frame.pack(pady=10)  # Add vertical padding around the frame

# Label that tells the user what to enter
label_count = tk.Label(frame, text="Number of passwords:")
label_count.pack(side=tk.LEFT)  # Place label to the left of entry box

# Entry box to let the user type how many passwords they want
entry_count = tk.Entry(frame, width=5)
entry_count.insert(0, "20")  # Default to 20 passwords
entry_count.pack(side=tk.LEFT, padx=5)  # Small horizontal padding

# Button to trigger password generation and saving
btn_generate = tk.Button(root, text="Generate & Save", command=generate_and_display)
btn_generate.pack(pady=10)  # Add vertical padding

# Output box (multi-line text area) to display the generated passwords
output_box = tk.Text(root, height=15, width=60)
output_box.pack()  # Pack it into the window

# Start the Tkinter event loop to run the GUI app
root.mainloop()
