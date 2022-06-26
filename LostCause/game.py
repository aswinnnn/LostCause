# The main file running the game.
# Bugs cleared and errors accounted for, 26 June 2022
# By Aswin, under MIT License 


from handler import *
from dbtypes import *
from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
import time
from banners import *
import os
import random

try:
    createDB()
except:
    pass

def Death(name:str):

    # Announces Physical Death in a custom way.

    os.system('cls' if os.name == 'nt' else 'clear')
    char = Character(name)
    print("[red]You", end=" "); time.sleep(1); print("[red]are", end=" "); time.sleep(1); print("[red]dead.\n")
    time.sleep(3)
    print(f"[yellow]You're PH is now 0 and you have died. Your character struggled a lot. They had {char.money} bucks at last and lived to be {char.age} years old. {char.name} didn't live happily because climate change took up half of their grown life.")
    time.sleep(3)
    non = Prompt.ask("[PRESSING ENTER WILL TAKE YOU BACK TO MAIN MENU]")
    main(name, char.loc)

def DeathMH(name:str):

    # Announces Mental Death in a custom way.

    os.system('cls' if os.name == 'nt' else 'clear')
    char = Character(name)
    print("[red]You", end=" "); time.sleep(1); print("[red]are", end=" "); time.sleep(1); print("[red]dead.\n")
    time.sleep(3)
    print(f"[yellow]You're MH is now 0 and you have died. Your character struggled a lot, mentally. They had {char.money} bucks at last and lived to be {char.age} years old. {char.name} didn't live happily because climate change took up half of their grown life.\n{char.name} died sad, young and miserable.")
    time.sleep(3)
    non = Prompt.ask("[PRESSING ENTER WILL TAKE YOU BACK TO MAIN MENU]")
    main(name, char.loc)

def checkForDeath(name):

    # Simple check for low PH and MH. Implemented on choices

    char = Character(name)
    if char.ph == 0:
        Death(name)
    elif char.mh == 0:
        DeathMH(name)
    else:
        pass


def main(name:str, loc:str):

    # main recursive function that acts as a "home" menu of sorts.
    # main choices after introduction + welcome happen here.

    os.system('cls' if os.name == 'nt' else 'clear')
    char = Character(name)
    charinfo = f'''---- {char.name} ----
    [green]Age: {char.age}[/green]
    [yellow]PH: {char.ph}[/yellow]
    [blue]MH: {char.mh}[/blue]
    [green]Money: {char.money}[/green]
    [yellow]Job: {char.job}[yellow]'''
    print(banner)
    print(charinfo)
    print("\n")
    print("[red]What would you like to do?")
    print("")
    print("[green][L] live[/green]  [yellow][I] info[/yellow]  [red][W] work[/red]  [blue][CTRL + C] quit[/blue]   ")
    print("")
    choice = Prompt.ask("--->", choices=["L", "I", "W"])

    # --- MAIN CHOICES ---

    match choice:
        case "L": # LIVE [INCREMENT PLAYERS AGE BY 2 YEARS.]
            os.system('cls' if os.name == 'nt' else 'clear')
            checkForDeath(name)
            age = char.age + 2
            addAge(name=name, amt=2)
            match loc:
                case "greenland":
                    b10 = ["you're a kid just kidding around. You'll grow up to face the world soon.",
                    "The current population of greenland seems to be decreasing. Migration? You don't care. More space for yourself!",
                    "You've been enjoying the summers a ton. The winters get really wintery but you like playing in the fields more than the ice.",
                    "You go around exploring the little parts of the land. You like how the sun shines off the ice sheets like a large mirror."]
                    b20 = ["You haven't been yourself lately so you go outside. You notice that there isn't much ice around anymore. The fields look dry.",
                    "The sea level in greenland has risen by 8mm since you were born. 'Well, that's kind of small', you think to yourself.",
                    "The population went from 50,300 from when you were born to 47,598. You wish more people happened to see the beauty of your country.",
                    "You start to think about moving. There's places where its less dry and more fun anyway.",
                    "The melting ice sheet has enabled a lot of people to mine minerals, oil and gas. You start to wonder if you'd like to be in bussiness with that.",
                    "Your friend is moving out of town. His father was a farmer who went bankrupt due to there not being enough fishes to capture. You feel sad."]
                    b30 = ["You talk to your Inuit friends and understand that they can't fish anymore. Their fathers switched from seal hunting to fishing but they have nothing to switch to other than leaving their traditional lives and buying food.",
                    "You don't see much ice anymore even though it gets really cold every once in a while. You wonder why.",
                    "Work is making you lazy and angry. You don't have time to do fun stuff anymore.",
                    "You're living. Just passing."]
                    b40 = ["You can't take the heat anymore. Both outside and inside the aluminium smelter you work at. You think of retiring early.",
                    "The Greenlandic Minister for finance and foreign affairs affirms that the government is working towards ending the climate crisis. You are not so sure."
                    "The sea level has rose by 5cm since you were born. Its getting hotter and hotter and your electricity bills take up half your paycheck.",
                    "When its raining the rain doesn't seem to stop. Its heavy and annoying. Better than the soaring hots, anyway."]
                    b50 = ["You barely live.",
                    "You're barely alive. You can't move because your house went down due to the rainfall and you paid to fix it and the electricity bills for the a.c have been emptying your pockets.",
                    "You think about buying an extra fan. Probably not worth it. You think about buying an extra heater.",
                    "You feel like dying. It's unbearable. The heats, the colds, the dry winds, its really starting to make you feel sad for the children you might have one day.",
                    "You think about not having children."]

                    if age < 10:
                        quote = random.choice(b10)
                        print("[yellow]-----------------------[/yellow]")
                        print(quote)
                        print("[yellow]-----------------------[/yellow]\n")
                        print('\n')
                        print(f"[green]You lived for 2 more years and you are now {age} years old. You feel great.")
                        print("\n")
                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)
                    elif age < 20:
                        quote = random.choice(b20)
                        print("[green]-----------------------[/green]")
                        print(quote)
                        print("[green]-----------------------[/green]\n")
                        print('\n')
                        print(f"[green]You lived for 2 more years and you are now {age} years old. You feel fine.")
                        print("\n")
                        ment = ["fine", "not"]
                        mentch = random.choice(ment)
                        match mentch:
                            case "fine":
                                pass
                            case "not":
                                print("[red]You are mentally degrading. Depression/Anxiety/Your surroundings do that.")
                                subMH(name=name, amt=5)

                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)
                    elif age < 30:
                        quote = random.choice(b30)
                        print("[blue]-----------------------[/blue]")
                        print(quote)
                        print("[blue]-----------------------[/blue]\n")
                        print('\n')
                        print(f"[green]You lived for 2 more years and you are now {age} years old. You feel fine.")
                        print("\n")
                        ment = ["fine", "not"]
                        mentch = random.choice(ment)
                        match mentch:
                            case "fine":
                                pass
                            case "not":
                                print("[red]You are physically degrading. Laziness/Too much work/Your surroundings do that.")
                                subPH(name=name, amt=10)

                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)
                    elif age < 40:
                        quote = random.choice(b40)
                        print("[red]-----------------------[/red]")
                        print(quote)
                        print("[red]-----------------------[/red]\n")
                        print('\n')
                        print(f"[green]You lived for 2 more years and you are now {age} years old. You feel fine.")
                        print("\n")
                        ment = ["fine", "not"]
                        mentch = random.choice(ment)
                        match mentch:
                            case "fine":
                                pass
                            case "not":
                                print("[red]You are physically degrading. Laziness/Too much work/Your surroundings do that.")
                                subMH(name=name, amt=15)

                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)
                    elif age < 50:
                        quote = random.choice(b50)
                        print("-----------------------")
                        print(quote)
                        print("-----------------------\n")
                        print('\n')
                        print(f"[green]You lived for 2 more years and you are now {age} years old. You feel fine.")
                        print("\n")
                        ment = ["fine", "not"]
                        mentch = random.choice(ment)
                        match mentch:
                            case "fine":
                                pass
                            case "not":
                                print("[red]You are physically degrading. Laziness/Too much work/Your surroundings do that.")
                                subPH(name=name, amt=25)

                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)
                    elif age < 60:
                        print("[yellow]You keep living, but barely, with no family or kids.")
                        non = Prompt.ask("[PRESS ENTER]")
                        main(name, loc)


        case "I": # DISPLAY PLAYER STATS IN A RENDERED TABLE.
            os.system('cls' if os.name == 'nt' else 'clear')
            ch = Character(name)
            table = Table(title=f"{ch.name}")
            table.add_column("Name")
            table.add_column("Location")
            table.add_column("Age")
            table.add_column("Physical Health")
            table.add_column("Mental Health")
            table.add_column("Money")
            table.add_column("Job")

            table.add_row(ch.name, ch.loc, str(ch.age), str(ch.ph), str(ch.mh), str(ch.money), ch.job)
            console =  Console()
            console.print(table)
            print("")
            non = Prompt.ask("[PRESS ENTER]")
            main(name=name, loc=loc)
        case "W": # WORK COMMAND TO EARN MONEY + MH/PH DEGRADATION.
            checkForDeath(name)
            char = Character(name)
            os.system('cls' if os.name == 'nt' else 'clear')
            if char.age < 18:
                print("[red]Oi! You aren't allowed to work just yet. Child labour laws, man.[/red]")
                non = Prompt.ask("[PRESS ENTER]")
                main(name, loc)
            elif char.job == "not decided yet.":
                print("You're old enough to work now! Pick a job: ")
                print("[red][M] Miner[/red]    [yellow][F] Fisher[/yellow]")
                job = Prompt.ask("--->", choices=["M", "F"])
                if job == "F": job = "Fisher"
                if job == "M": job = "Miner"
                with getDB() as conn:
                    conn.execute("UPDATE chars SET job = ? WHERE name = ?", (job, name))
                    conn.commit()

                main(name, loc)

            outc = ['good', 'not', 'maybe']
            outc = random.choice(outc)
            emon = random.randint(100,500)
            emon = round(emon)
            match outc:
                case "good":
                    addMoney(name, emon)
                    print(f"-------- {name} goes to work --------")
                    print("")
                    print(f"You did good at work today and earned [green]{emon} bucks[/green]")
                    print("")
                    print(f"-------- {name} comes back from work --------")
                    print("")
                    non = Prompt.ask("[PRESS ENTER]")
                    main(name, loc)
                case "not":
                    emon = random.randint(10, 200)
                    emon = round(emon)
                    subMoney(name, emon)
                    print(f"-------- {name} goes to work --------")
                    print("")
                    print(f"You did good at work today and lost [red]{emon} bucks[/red] for violating rules. And for parking, fuel, etc.")
                    print("")
                    print(f"-------- {name} comes back from work --------")
                    print("")
                    non = Prompt.ask("[PRESS ENTER]")
                    main(name, loc)
                case "maybe":
                    print(f"-------- {name} goes to work --------")
                    print("")
                    print(f"[yellow]Your boss docked your pay for today because you were not focusing on work.[/yellow]")
                    print("")
                    print(f"-------- {name} comes back from work --------")
                    print("")
                    non = Prompt.ask("[PRESS ENTER]")
                    main(name, loc)







def welcome(loc:str):

    # custom welcome for different locations. There's probably a better way to do this.

    match loc:
        case "greenland":
            print(greenland)
            print("")
            print("[green]The year is 2067.\nYou are born to a nice little family in Greenland. Its a bit cold but\nyou'll get used to it.");time.sleep(2)
            print("[green]You have 100 PH (Physical Health) and 100 MH (Mental Health) and 0 money");time.sleep(3)
            print("[red]Here's how you can live your life in Lost Cause : [/red]\n")
            print('''[green][L] live :[/green] Use this to live 2 years. This lets you live your life for 2 years, but really fast.
            \n[yellow] [I] info :[/yellow] Use this to view your stats, info and health.
            \n[red][W] work :[/red] Use this to work yourself and earn money! dolla dolla bills, y'all
            \n[blue][CTRL + C] quit[/blue] Lets you quit the game. All progress is automatically saved.''')
            print("\n")
            time.sleep(3)
            print("If you're done reading and understanding, can we begin the game?")
            non = Prompt.ask("--->[PRESS ENTER]")
            os.system('cls' if os.name == 'nt' else 'clear')
            main(name=name, loc=location)
        case "india":
            print(india)
            print("\n")
            print("[green]The year is 2067 and you are born in a lovely place in India. Its pretty tropical, humid but\n you'll get used to it.");time.sleep(3)
            print("[green]You have 100 PH (Physical Health) and 100 MH (Mental Health) and 0 money");time.sleep(3)
            print("[red]Here's how you can live your life in Lost Cause : [/red]\n")
            print('''[green][L] live :[/green] Use this to live 2 years. This lets you live your life for 2 years, but really fast.
            \n[yellow] [I] info :[/yellow] Use this to view your stats, info and health.
            \n[red][W] work :[/red] Use this to work yourself and earn money! dolla dolla bills, y'all
            \n[blue][CTRL + C] quit[/blue] Lets you quit the game. All progress is automatically saved.''')
            print("\n")
            time.sleep(3)
            print("If you're done reading and understanding, can we begin the game?")
            non = Prompt.ask("--->[PRESS ENTER]")
            main(name=name, loc=location)

        case "australia":
            print(australia)
            print("\n")
            print("[green]The year is 2067 and you are born to a lovely family in Brisbane. Its bloody cold in the winter but\nyou'd love spending your summer at Rainbow beach where it gets nice and hot.");time.sleep(3)
            print("[green]You have 100 PH (Physical Health) and 100 MH (Mental Health) and 0 money");time.sleep(2)
            print("[red]Here's how you can live your life in Lost Cause : [/red]\n")
            print('''[green][L] live :[/green] Use this to live 2 years. This lets you live your life for 2 years, but really fast.
            \n[yellow] [I] info :[/yellow] Use this to view your stats, info and health.
            \n[red][W] work :[/red] Use this to work yourself and earn money! dolla dolla bills, y'all
            \n[blue][CTRL + C] quit[/blue] Lets you quit the game. All progress is automatically saved.''')
            print("\n")
            time.sleep(3)
            print("If you're done reading and understanding, can we begin the game?")
            non = Prompt.ask("--->[PRESS ENTER]")
            main(name=name, loc=location)
        case "venice":
            print(venice)
            print("\n")
            print("[green]The year is 2067 and you are born to a small but beautiful family in Venice. You're already loving the waters and pizza.");time.sleep(2)
            print("[green]You have 100 PH (Physical Health) and 100 MH (Mental Health) and 0 money");time.sleep(3)
            print("[red]Here's how you can live your life in Lost Cause : [/red]\n")
            print('''[green][L] live :[/green] Use this to live 2 years. This lets you live your life for 2 years, but really fast.
            \n[yellow] [I] info :[/yellow] Use this to view your stats, info and health.
            \n[red][W] work :[/red] Use this to work yourself and earn money! dolla dolla bills, y'all
            \n[blue][CTRL + C] quit[/blue] Lets you quit the game. All progress is automatically saved.''')
            print("\n")
            time.sleep(3)
            print("If you're done reading and understanding, can we begin the game?")
            non = Prompt.ask("--->[PRESS ENTER]")
            main(name=name, loc=location)


# Below is what player sees first thing when they open the game.
# Choices are given to start a new game or load a save.
# Only Greenland is selectable as a location for now due to SimpliHacks time limit.
# I will be completing this eventually or if it recieves unexpected encouragement.


os.system('cls' if os.name == 'nt' else 'clear')

print(banner) # prints the main logo.

print("")
print("[green]|[/green]  scientifically accurate, survival text-based adventure\nset in the future where climate change is inevitable  [green]|[/green]")
print(" ")

print("[bold red]Welcome to Lost Cause.\nWould you like to load a save or start a new game?")
print(" ")
print("[bold yellow] [L] [/bold yellow] LOAD")
print("[bold yellow] [N] [/bold yellow] NEW GAME")
choice = Prompt.ask("--->", choices=["N", "L"])
print("")
if "L" in choice:
    names = []
    with getDB() as conn:
        chars = conn.execute("SELECT name FROM chars")
        for char in chars:
            names.append(char[0])
    print("[yellow]Current saved characters:[/yellow]\n")
    print("\n".join(names))
    if names == []:
        print("There are no saved characters. Do [red]CTRL + C[/red] to [blue]quit[/blue] and [yellow]start the game again.[/yellow]")

    pick = Prompt.ask("--->", choices=names)
    charloc = Character(pick)
    main(pick, charloc.loc)

elif "N" in choice:
    print("[bold green]Congratulations!", end=""); time.sleep(0.8); print("[bold green] You are a newborn.\n", end=""); time.sleep(2)
    print("[bold green]Unlike the agony of real babies, you get to choose where you're born.\n"); time.sleep(2)
    print("")
    print("[bold red]Pick a birth location below:\n")
    print("    [green][G] Greenland[/green]    [I] India    [blue][A] Australia[/blue]    [V] Venice    ")
    print(" ")
    print("[Only Greenland is available for the time due to hackathon time limits.]")
    ch = Prompt.ask("--->", choices=["G", "I", "A", "V"])
    match ch:
        case "G":
            location = "greenland"
            print("")
            print("[green]Greenland!", end=" "); time.sleep(1); print("[green]Amazing place.", end=" ");time.sleep(1); print("(Hope nothing bad happens to it anytime soon.)"); time.sleep(3)
            print("")
            print("[green]You're a baby chilling somewhere in Greenland.\n"); time.sleep(1); print("[red]What would you like to name yourself? (You cannot change this later)")
            name = Prompt.ask("--->")
            print(" ")
            print("[green]Creating you.", end=""); time.sleep(1); print("[green].", end=""); time.sleep(1);print("[green]."); time.sleep(1)
            rs = createChar(name, location)
            if rs ==  Success:
                non = Prompt.ask("You have been created. [bold green][PRESS ENTER][/bold green]")
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome("greenland")

        case "I":
            location = "india"
            print("")
            print("[green]India!", end=" "); time.sleep(1); print("[green]Awesome place.", end=" ");time.sleep(1); print("[green](Hope nothing bad happens to it anytime soon.)"); time.sleep(3)
            print("")
            print("[green]You're a baby chilling somewhere in India.\n"); time.sleep(1); print("[red]What would you like to name yourself? (You cannot change this later)")
            name = Prompt.ask("--->")
            print(" ")
            print("[green]Creating you.", end=""); time.sleep(1); print("[green].", end=""); time.sleep(1);print("[green]."); time.sleep(1)
            rs = createChar(name, location)
            if rs ==  Success:
                non = Prompt.ask("You have been created. [bold green][PRESS ENTER][/bold green]")
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome("india")
        case "A":
            location = "australia"
            print("")
            print("[green]Australia!", end=" "); time.sleep(1); print("[green]Isn't that something.", end=" ");time.sleep(1); print("(Hope nothing bad happens there anytime soon.)"); time.sleep(3)
            print("")
            print("[green]You're a baby chilling somewhere in Aussie land.\n"); time.sleep(1); print("[red]What would you like to name yourself? (You cannot change this later)")
            name = Prompt.ask("--->")
            print(" ")
            print("[green]Creating you.", end=""); time.sleep(1); print("[green].", end=""); time.sleep(1);print("[green]."); time.sleep(1)
            rs = createChar(name, location)
            if rs ==  Success:
                non = Prompt.ask("You have been created. [bold green][PRESS ENTER][/bold green]")
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome("australia")
        case "V":
            location = "venice"
            print("")
            print("[green]Odd place from the list, Venice isn't even a country but sure.", end=" "); time.sleep(1); print("[green]Cool place.", end=" ");time.sleep(1); print("(Hope nothing bad happens to it anytime soon.)"); time.sleep(3)
            print("")
            print("[green]You're a baby chilling somewhere in Venice.\n"); time.sleep(1); print("[red]What would you like to name yourself? (You cannot change this later)")
            name = Prompt.ask("--->")
            print(" ")
            print("[green]Creating you.", end=""); time.sleep(1); print("[green].", end=""); time.sleep(1);print("[green]."); time.sleep(1)
            rs = createChar(name, location)
            if rs ==  Success:
                non = Prompt.ask("You have been created. [bold green][PRESS ENTER][/bold green]")
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome("venice")

