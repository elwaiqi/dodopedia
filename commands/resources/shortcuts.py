import os
from random import randint

#resources path
resources_path = os.getcwd() + "/commands/resources/ACNHAPI/"

#acnhapi
acnhapi = "https://acnhapi.com/v1/"

#string cleanup
def cleanup_str(str_to_clean: str):
    clean_str = str_to_clean.lower().replace("'", "").replace(" ", "_").replace("._", "")

    return clean_str

#random color for embeds
def embed_colour():
    random_number = randint(0, 16777215)
    
    return random_number

#emoji
emoji_bells = "<:bells:713809370416152597>"
emoji_nmt = "<:nmt:713809371242692688>"
emoji_yellow_heart = "\U0001F49B"

#other
embed_footer_text = f"Made with {emoji_yellow_heart} by @Waiqi#0813 | Info from acnhapi.com"