import time

# Die with a simle Lyrics
lyrics=[
    "If the world was ending, I'd wanna be next to you 🌍❤️",
    "If the party was over and our time on Earth was through 🎉⏳",
    "I'd wanna hold you just for a while 🤗💖",
    "and die with a smile 😊🕊️",
    "If the world was ending, I'd wanna be next to you 🌍❤️",
    "Right next to you 👫",
    "Next to you 👫"
]

# Delay for each lyric line in seconds
delays = [4, 3.5, 1, 2.2, 3, 2.5, 0]  # Delay before the next line starts

# Delay between each letter
char_delay = 0.1 # Delay in seconds between each letter (adjust as desired)

# Function to display lyrics with typing effect
def display_lyrics_with_typing_effect(lyrics, delays, char_delay):
    for i, line in enumerate(lyrics):
        for char in line:
            print(char, end='', flush=True)  # Display each letter without changing rows
            time.sleep(char_delay)  # Waiting for the specified time per letter
        print()  # Move to the next line after the whole sentence is displayed
        time.sleep(delays[i])  # Wait for the specified time before proceeding to the next line

# Call a function with predefined lyrics, delay, and typing speed
display_lyrics_with_typing_effect(lyrics, delays, char_delay)
