print("__________\n"
     "|  HARAM FINDER|\n"
    "|    (◕‿◕)    |\n"
    "|______________|\n"
    "   /     \   \n"
    "  /       \  \n"
    "(_____)_____)\n")
print("Welcome to HARAM Finder.\n"
      "I hope you always be HALAL!")

# List of haram things
haram_list = {
    "eating pork": "BROOO, ASTAGHFIRULLAH! 🐷🚨",
    "drinking alcohol": "Haram level: 100% 🍷🔥",
    "gambling": "Say goodbye to your money AND the hereafter 🎰💸",
    "lying": "Liar, liar, jahannam fire! 🤥🔥",
    "stealing": "Hope you like prison AND hell 🏴‍☠️🔥",
    "bribery": "Bribing your way to jahannam 💰😬",
    "backbiting": "Talking behind someone's back? Shaitan is clapping 👏👹",
    "oppressing others": "May Allah have mercy on your victims ⚖️😡",
    "practicing magic": "Harry Potter? More like Harry Haram 🔮🚫",

    # Funny ones
    "using php for backend": "Bro, you need serious guidance 🖥️😂",
    "not grilling kebabs during holidays": "This is cultural treason 🍢🚨",
    "ignoring your mom’s messages": "Jahannam speedrun 📱🔥",
    "replying 😂 to a sad message": "Certified heartless 💔😂",
    "going to the gym just for pictures": "All flex, no reps 🏋️‍♂️📸",
    "choosing the rival team in fifa": "You're dead to us 🎮😤",
    "reading a message but not marking it as seen": "Shaitan’s favorite move 👀😈"
}

# Get user input and clean it up
user_input = input("Enter something to check if it's haram: ").strip().lower()

# Function to check if input contains any haram words
def check_haram(user_input):
    for key, message in haram_list.items():
        if key in user_input:
            return message
    return "Hmm... I can't judge that. But be careful, bro! 🤔"

# Check if input is haram
result = check_haram(user_input)
print(result)