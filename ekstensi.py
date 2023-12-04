import os
import time
from pyfiglet import Figlet
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_text_animation(text, delay=1.0, clear=True):
    fig = Figlet(font='slant')
    if clear:
        clear_screen()
    for line in text.splitlines():
        print(Fore.RED + fig.renderText(line))
        time.sleep(delay)

def ask_question(question):
    print(Fore.GREEN + question)
    response = input(Fore.YELLOW + "mau atau gamau?: ").lower()
    return response

def main():
    display_text_animation("ku", delay=0.5)
    display_text_animation("ku cayang", delay=0.5)
    display_text_animation("ku cayang cekali ko ay", delay=0.5)

    # Display static text like animation I Like You

    response = ask_question("mau nikah ga sama aku?")

    if response == 'mau':
        display_text_animation("mwah,tungguka pale nah", delay=0.5)
        display_text_animation("mwah,tungguka pale nah", delay=0.5)

        # Display static text like animation I love you
        print(Fore.RED + "love you<3")

    elif response == 'gamau':
        display_text_animation("e", delay=0.5)
        display_text_animation("ee", delay=0.5)
        display_text_animation("eee", delay=0.5)
        display_text_animation("eeee", delay=0.5)
        display_text_animation("eeeee benerann nihh", delay=0.5)
        clear_screen()
        display_text_animation(":((((((((((", delay=0.5)

if __name__ == "__main__":
    main()