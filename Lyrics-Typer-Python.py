import time

# Previous lyrics (commented out)
# lyrics = [
#     "I have faith in what I see",
#     "Now I know I have met an angel",
#     "in person",
#     "And she looks perfect",
#     "I don't deserve this",
#     "You look perfect tonight"
# ]

# # Delay for each lyric line in seconds
# delays = [0.5, 2, 1, 1, 2, 2]  # Delay before the next line starts

# lyrics = [
#     "If the world was ending, I'd wanna be next to you 🌍❤️",
#     "If the party was over and our time on Earth was through 🎉⏳",
#     "I'd wanna hold you just for a while 🤗💖",
#     "and die with a smile 😊🕊️",
#     "If the world was ending, I'd wanna be next to you 🌍❤️",
#     "Right next to you 👫",
#     "Next to you 👫"
# ]

# # Delay for each lyric line in seconds
# delays = [4, 3.5, 1, 2.2, 3, 2.5, 0]  # Delay before the next line starts

# lyrics = [
#     "Galat kya, sahi kya, mujhe na pata hai 🤔",
#     "Tumhe 'gar pata ho, bata dena 🗣️",
#     "Main arse se khud se zara lapata hoon 🧭",
#     "Tumhe 'gar miloon to pata dena 📝",
#     "Kho na jana mujhe dekhte-dekhte 👀",
#     "Tu hi zariya, ✨",
#     "Tu hi manzil hai 🛤️",
#     "Ya ki dil hai ❤️",
#     "Itna bata? 🤔",
#     "Tune chhua 🤲",
#     "Zakhmon ko mere 🩹",
#     "Marham-marham dil pe laga 💖"
# ]

# # Delay for each lyric line in seconds
# delays = [1.9, 2.9, 2.2, 3, 2, 2, 1.3, 1.9, 1.9, 1.9, 1.8, 2.5]  # Delay before the next line starts

# lyrics = [
#     "Rehte Ho Aake Jo Tum Paas Mere 💑",
#     "Tham Jaaye Pal Ye Wahin, Bass Main Yeh Sochun... 🤔",
#     "Sochu Main Tham Jaaye Pal Yeh Paas Mere Jab Ho Tum... 💭",
#     "Sochu Main Tham Jaaye Pal Yeh Paas Mere Jab Ho Tum... 💭",
#     "Chalti Hai Saansein Pehle Se Zyada 😮‍💨",
#     "Pehle Se Zyada Dil Theharne Laga... ❤️",
# ]

# # Delay for each lyric line in seconds
# delays = [0, 0, 0, 0, 1.5, 1.5]  # Delay before the next line starts

# # Bhojpuri Lyrics (Previously given lyrics)
# lyrics += [
#     "Nokarani bana ke rakhla tu 🧹",
#     "Rani ke sapna dekha ke 👑",
#     "Ola bola ke chalni hum 🚗",
#     "Ae Raja Ji, maike 🏠",
#     "Pehile je janti, chulha-chauki karwaiba 🍳",
#     "Nadiya kinara bheji paani bharwaiba 🏞️",
#     "Ta kabo na biyahwa rachaiti, aho Raja 💍",
#     "Mange na senura-tikawaiti, aho Raja 💄",
#     "Kabo na biyahwa rachaiti... 💑."
# ]

# # Delay for each lyric line in seconds for Bhojpuri song
# delays += [0, 0, 0, 0, 1.5, 1, 0.5, 0.3, 0]  


# New Lyrics Added: "Musafir - Atif Aslam"
lyrics = [
    "Tera mera jahan ✨", 
    "Le chalun main wahaan 🚀", 
    "Koi tujhko na mujhse chura le ❤️", 
    "Rakh loon aankhon mein main 👁️", 
    "Kholun palke na main 😌", 
    "Koi tujhko na mujhse chura le 💕",
    "Main andheron se ghira hoon 🌑", 
    "Aa dikha de tu mujhko savera mera 🌅", 
    "Main bhatakta ik Musafir 🚶‍♂️", 
    "Aa dila de tu mujhko basera mera 🏡"
]

# Delay for each lyric line in seconds
delays = [1, 1, 1.5, 1, 1.5, 1.8, 2.0, 2.5, 2.8, 2.8]  

# Delay between each letter
char_delay = 0.1  # Delay in seconds between each letter (adjust as desired)

# Function to display lyrics with typing effect
def display_lyrics_with_typing_effect(lyrics, delays, char_delay):
    for i, line in enumerate(lyrics):
        for char in line:
            print(char, end='', flush=True)  # Display each letter without changing rows
            time.sleep(char_delay)  # Waiting for the specified time per letter
        print()  # Move to the next line after the whole sentence is displayed
        time.sleep(delays[i])  # Wait for the specified time before proceeding to the next line

# Call the function with predefined lyrics, delay, and typing speed
display_lyrics_with_typing_effect(lyrics, delays, char_delay)
