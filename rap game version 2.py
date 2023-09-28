import os
import random

def display_title_screen():
    title_screen = """
 _________              __  .__                ___________.__       .__     __   
 /   _____/ ____   _____/  |_|__| ____   ____   \_   _____/|__| ____ |  |___/  |_ 
 \_____  \_/ __ \_/ ___\   __\  |/  _ \ /    \   |    __)_ |  |/ ___\|  |  \   __\
 /        \  ___/\  \___|  | |  (  <_> )   |  \  |        \|  / /_/  >   Y  \  |  
/_______  /\___  >\___  >__| |__|\____/|___|  / /_______  /|__\___  /|___|  /__|  
        \/     \/     \/                    \/          \/   /_____/      \/      
"""
    print(title_screen)

# Define the player's character class with an inventory
class HipHopArtist:
    def __init__(self, name, home_city_name):
        self.name = name
        self.city_fame = {}  # Dictionary to track fame in each city
        self.total_fame = 0  # Initialize total fame to zero
        self.money = 0
        self.inventory = {}
        self.current_city = home_city_name  # Initialize the player's current city with the specified home city name
        self.has_written_song = False  # Flag to track if the player has written a song
        self.day = 1  # Initialize the day to 1
        self.songs = {}  # Dictionary to store song titles and lyrics
        self.monthly_rent = 900  # Monthly rent for the player's home
        self.days_since_last_rent_payment = 0  # Initialize days since last rent payment
        self.dance_skill = 5

    def update_city_fame(self, city, fame_change):
        # Update city fame and total fame when the player gains or loses fame
        self.city_fame[city] = self.city_fame.get(city, 0) + fame_change
        self.total_fame += fame_change

    def get_city_fame(self, city):
        # Get the fame level in a specific city
        return self.city_fame.get(city, 0)
    
    def pay_monthly_rent(self):
       # Deduct monthly rent from the player's money
       if self.money >= self.monthly_rent:
           self.money -= self.monthly_rent
           self.days_since_last_rent_payment = 0  # Reset the days count
           return True  # Rent paid successfully
       else:
           return False  # Not enough money to pay rent
       
class Property:
    def __init__(self, name, cost, income):
        self.name = name
        self.cost = cost
        self.income = income
        
# Define the NPC class
class NPC:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Define the cities the player can travel to
cities = ["Home", "New York", "Chicago", "The Durty South", "LA", "Miami", "Atlanta", "Houston", "Detroit"]

# Define the initial fame threshold for unlocking new cities
city_unlock_fame = {
    "Home": 0,
    "New York": 100,
    "Chicago": 400,
    "The Durty South": 600,
    "LA": 800,
    "Miami": 1000,
    "Atlanta": 1200,
    "Houston": 1400,
    "Detroit": 1600,
}

# Define the initial fame level for each city
city_fame = {
    "Home": 0,             # You start with some fame at your home city
    "New York": 0,
    "Chicago": 0,
    "The Durty South": 0,
    "LA": 0,
    "Miami": 0,
    "Atlanta": 0,
    "Houston": 0,
    "Detroit": 0
}

# Define properties for each city
city_properties = {
    "New York": [
        Property("Luxury Apartment", 500000, 2000),
        Property("Nightclub", 1000000, 5000),
        Property("Recording Studio", 1500000, 7000),
    ],
    "Los Angeles": [
        Property("Beach House", 750000, 2500),
        Property("Recording Studio", 1500000, 7000),
        Property("Movie Theater", 2000000, 9000),
    ],
    "Chicago": [
        Property("Brownstone House", 400000, 1500),
        Property("Jazz Club", 800000, 3500),
        Property("Art Gallery", 1200000, 5500),
    ],
    "The Durty South": [
        Property("Southern Mansion", 600000, 2000),
        Property("Hip-Hop Club", 1000000, 4500),
        Property("BBQ Restaurant", 900000, 4000),
    ],
    "Miami": [
        Property("Beachfront Condo", 550000, 1800),
        Property("Salsa Dance Club", 1100000, 5000),
        Property("Boat Rental Business", 1800000, 8000),
    ],
    "Atlanta": [
        Property("Southern Estate", 650000, 2200),
        Property("Music Production Studio", 1300000, 6000),
        Property("Sports Bar", 950000, 3800),
    ],
    "Houston": [
        Property("Ranch House", 450000, 1700),
        Property("BBQ Joint", 850000, 3800),
        Property("Tech Startup Office", 1100000, 5000),
    ],
    "Detroit": [
        Property("Historic Mansion", 550000, 2000),
        Property("Motor City Club", 950000, 4000),
        Property("Auto Repair Shop", 750000, 3000),
    ],
    "Home": []  # You can define properties for the player's initial city as needed
}

def display_properties(city):
    print(f"Properties available in {city}:")
    for i, prop in enumerate(city_properties[city]):
        print(f"{i + 1}. {prop.name} (Cost: ${prop.cost}, Income: ${prop.income})")
        
def visit_city(player, city):
    print(f"Welcome to {city}!")
    while True:
        print("Options:")
        print("1. View available properties")
        print("2. Exit city")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_properties(city)
            property_index = int(input("Enter the number of the property you want to buy (or any other key to cancel): "))
            buy_property(player, city, property_index - 1)
        elif choice == "2":
            break

def buy_property(player, city, property_index):
    if property_index < 0 or property_index >= len(city_properties[city]):
        print("Invalid property index.")
        return

    property_to_buy = city_properties[city][property_index]
    if player.money >= property_to_buy.cost:
        player.money -= property_to_buy.cost
        player.owned_properties.append(property_to_buy)
        print(f"You bought {property_to_buy.name} in {city}!")
    else:
        print("You don't have enough money to buy this property.")


def clear_screen():
    if os.name == 'posix':  # For UNIX/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')
        
def wait_for_enter():
    input("\nPress Enter to continue...")

def random_event(player):
    # Define the chance of a random event occurring (e.g., 30% chance)
    chance_of_event = 30  # Adjust this value as needed

    # Check if a random event occurs based on the chance
    if random.randint(1, 100) <= chance_of_event:
        # Define a dictionary of events with associated fame and fortune changes
        events = {
            "Good Performance": {"fame_change": 20, "money_change": 200},
            "Technical Difficulties": {"fame_change": -10, "money_change": -100},
            "Fan Rushes Stage": {"fame_change": 30, "money_change": 0},
            "Forget Lyrics": {"fame_change": -15, "money_change": -150},
            "Wardrobe Malfunction": {"fame_change": -5, "money_change": -50},
        }

        # Choose a random event from the list
        event_name, event_changes = random.choice(list(events.items()))

        # Apply fame and fortune changes to the player
        player.total_fame += event_changes["fame_change"]
        player.money += event_changes["money_change"]

        # Display the event and its effects
        print("\nRandom Event:")
        print(f"{event_name}: {event_changes['fame_change']} Fame, {event_changes['money_change']} Fortune")
    else:
        # If no event occurs, simply proceed without displaying anything
        pass

def name_song():
    song_name = input("Enter a name for your song: ")
    return song_name

# Define a function for traveling to different cities
def travel(player):
    print("\n*** Travel Menu ***")
    print("Available Cities:")
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city}")
    print(f"{len(cities) + 1}. Back to the main menu")
    choice = input("Enter the number of the city you want to travel to: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(cities):
            destination_city = cities[choice - 1]
            if destination_city != player.current_city:
                print(f"You are traveling from {player.current_city} to {destination_city}.")
                player.current_city = destination_city
                # Update player's fame based on the destination city's fame level
                player.total_fame += city_fame[destination_city]
                print(f"Your new fame in {destination_city}: {player.total_fame}")
                # Introduce a random event when traveling
                random_event(player)
            else:
                print("You are already in that city.")
        elif choice == len(cities) + 1:
            pass  # Back to the main menu
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("Invalid input. Please enter a number.")

# Define the player's character
def create_player():
    player_name = input("Enter your artist name: ")
    home_city_name = input("Enter the name of your home city: ")
    player = HipHopArtist(player_name, home_city_name)
    return player


# Define game functions
def start_game():
    # Display the title screen
    display_title_screen()
       
    print("Welcome to the Underground Hip-Hop Journey!")
    player = create_player()  # Create the player character
    print(f"Good luck, {player.name}! Your journey begins now.")
    # Create the list of NPCs
    npc = [
       NPC("DJ Scratch", "A legendary DJ known for his incredible scratching skills."),
       NPC("Lyricist Lila", "A talented lyricist and rapper always looking for collaboration opportunities."),
       NPC("Big Money Records Agent", "An agent from a famous record label interested in signing new talent."),
       NPC("B-Boy Benny", "A breakdancer and hip-hop enthusiast who can teach you some cool moves."),
       NPC("Graffiti Guru Gabby", "A graffiti artist known for creating stunning street art. She might offer you a mural project."),
       NPC("Radio DJ Remy", "A popular radio DJ who can play your tracks and help boost your fame."),
       NPC("Beat Producer Max", "A skilled beat producer looking for a lyricist to work on his new project."),
       NPC("Street Poet Piper", "A street poet with a gift for spoken word. Collaborating with her could result in a unique fusion of styles."),
       NPC("Hip-Hop Historian Hank", "A historian of hip-hop culture who can provide insights and knowledge about the genre's roots."),
       NPC("Cypher Champion Carlos", "A rap battle champion always up for a challenge. Defeating him could earn you respect in the rap scene."),
       NPC("Dance Crew Leader Destiny", "The leader of a local dance crew. Joining her crew might lead to epic dance-offs."),
   ]

    main_menu(player, npc)  # Pass the list of NPCs to the main_menu function
    
# Update main_menu function to include inventory options
def main_menu(player, npcs):
    while True:
        # Check for rent payment every 30 in-game days
        if player.days_since_last_rent_payment >= 30:
            rent_paid = player.pay_monthly_rent()
            if rent_paid:
                print("\nYou've paid your monthly rent.")
            else:
                print("\nYou couldn't pay your rent! Your fortune is negative, and you've lost the game.")
                quit_game()
                
        # Display the current city at the top
        print(f"\nCurrent City: {player.current_city}")
        print("\nMain Menu:")
        print("1. Write and record a new track")
        print("2. Perform at a local venue")
        print("3. Collaborate with other artists")
        print("4. Check your fame and fortune")
        print("5. Manage your inventory")
        print("6. Grow your fan base")
        print("7. Travel to a different city")
        print("8. Initiate a rap battle")
        print("9. Interact with NPCs")
        print("10. Quit the game")
        
        # Check for random events and NPC interactions
        if random.randint(1, 100) <= 30:  # Adjust the probability as needed
            random_event(player)  # Check for a random event
            random_npc_interaction(player, npcs)  # Interact with a random NPC
        
        choice = input("Enter your choice: ")
            
        if choice == "1":
            write_track(player)
        elif choice == "2":
            perform(player)
        elif choice == "3":
            collaborate(player)
        elif choice == "4":
            check_status(player)
            # Check if the player has won or lost
            if player.total_fame >= 1000000:
                print("Congratulations! You've achieved worldwide fame and won the game!")
                quit_game()
            elif player.total_fame <= 0 or player.money <= 0:
                print("Sorry, you've lost the game. Your fame or fortune dropped to zero.")
                quit_game()
        elif choice == "5":
                manage_inventory(player)
        elif choice == "6":
                grow_fan_base(player)
        elif choice == "7":
                travel(player)
        elif choice == "8":
                initiate_rap_battle(player)
        elif choice == "9":
                interact_with_npc(player)  # Pass the list of NPCs to the interaction function
        elif choice == "10":
                quit_game()
        else:
                print("Invalid choice. Please select a valid option.")




def add_to_inventory(player, item_name, quantity=1):
    if item_name in player.inventory:
        player.inventory[item_name] += quantity
    else:
        player.inventory[item_name] = quantity

def remove_from_inventory(player, item_name, quantity=1):
    if item_name in player.inventory:
        if player.inventory[item_name] >= quantity:
            player.inventory[item_name] -= quantity
            if player.inventory[item_name] == 0:
                del player.inventory[item_name]
        else:
            print("You don't have enough of that item.")
    else:
        print("Item not found in your inventory.")

def show_inventory(player):
    print("\nInventory:")
    for item, quantity in player.inventory.items():
        print(f"{item}: {quantity}")

def manage_inventory(player):
    while True:
        print("\nInventory Menu:")
        print("1. View inventory")
        print("2. Add item to inventory")
        print("3. Remove item from inventory")
        print("4. Back to main menu")
        inventory_choice = input("Enter your choice: ")

        if inventory_choice == "1":
            show_inventory(player)
        elif inventory_choice == "2":
            item_name = input("Enter the name of the item you want to add: ")
            add_to_inventory(player, item_name)
        elif inventory_choice == "3":
            item_name = input("Enter the name of the item you want to remove: ")
            remove_from_inventory(player, item_name)
        elif inventory_choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

def check_status(player):
    print("\nFame and Fortune Status:")
    print(f"Current Fame: {player.total_fame}")
    print(f"Current Fortune: {player.money}")

# Define a function to generate a random track prompt
def generate_track_prompt():
    track_prompts = [
        "Overcoming adversity",
        "Love and heartbreak",
        "Street life",
        "Social justice",
        "Personal growth",
        "Dreams and aspirations",
        "Friendship and loyalty",
        "Life in the city",
        "Political commentary",
        "Nostalgia for the past",
        "Exploring the unknown",
        "Inspirational stories",
        "Surreal experiences",
        "Epic battles",
        "Historical events",
        "Magical realms",
        "Science fiction adventures",
        "Time travel mysteries",
        "Fantasy worlds",
        "Mythological creatures",
    ]
    return random.choice(track_prompts)

# Define a function to calculate the quality of the track
def calculate_track_quality(lyrics):
    # Calculate the quality of the track based on the length and creativity of lyrics
    
    # Calculate the number of lines in the lyrics
    num_lines = len(lyrics)

    # Calculate creativity based on the presence of unique words
    unique_words = set(word.lower() for line in lyrics for word in line.split())
    creativity = len(unique_words)

    # Calculate track quality based on the number of lines and creativity
    track_quality = num_lines * 2 + creativity * 3

    return track_quality

rap_battle_responses = {
    "insult": ["Your rhymes are weak!", "You can't rap to save your life!", "Is that all you got?"],
    "compliment": ["You've got some skills!", "I respect your flow!", "Not bad, not bad at all!"]
}

# Define a function to initiate a rap battle
def initiate_rap_battle(player):
    print("\nInitiating Rap Battle:")
    
    # Calculate the cost based on player's fame
    cost = 200 + (player.total_fame // 10)
    
    # Check if the player has enough fortune to initiate a rap battle
    if player.money >= cost:
        print(f"You, {player.name}, are about to engage in a rap battle.")
        player.money -= cost  # Deduct the calculated cost
        # Simulate the rap battle
        rap_battle_result = simulate_rap_battle(player)

        # Update player's fame and fortune based on the battle result
        player.total_fame += rap_battle_result["fame_change"]
        player.money += rap_battle_result["money_earned"]
        
        # Increment the day
        player.day += 1

        # Display battle results
        print("\nRap Battle Results:")
        print(f"Fame Change: {rap_battle_result['fame_change']}")
        print(f"Money Earned: {rap_battle_result['money_earned']}")
        print(f"Current Fame: {player.total_fame}")
        print(f"Current Fortune: {player.money}")
    else:
        print(f"You need at least {cost} fortune to initiate a rap battle.")

# Simulate the rap battle and determine its outcome
def simulate_rap_battle(player):
    """
    Simulate a rap battle.

    Args:
        player (Player): The player object.

    Returns:
        dict: A dictionary containing fame_change and money_earned.
    """
    # Determine the opponent's response
    opponent_response = random.choice(["insult", "compliment"])
    opponent_phrase = random.choice(rap_battle_responses[opponent_response])

    # Calculate the player's rap skill factor based on fame and a bit of randomness
    player_rap_skill = player.total_fame + random.randint(-10, 10)

    # Calculate the opponent's rap skill factor with some randomness
    opponent_rap_skill = random.randint(0, 100) + random.randint(-20, 20)

    # Determine the outcome of the rap battle
    if player_rap_skill > opponent_rap_skill:
        # Player wins
        fame_change = random.randint(10, 30)
        money_earned = random.randint(100, 200)
        print(f"\nYou rap brilliantly! {opponent_phrase}")
    else:
        # Opponent wins
        fame_change = random.randint(-5, -25)
        money_earned = random.randint(50, 100)
        print(f"\nYour opponent outshines you! {opponent_phrase}")

    return {"fame_change": fame_change, "money_earned": money_earned}

def random_npc_interaction(player, npc):
    if random.random() < 0.5:  # Adjust the probability as needed
        npc = random.choice(npc)
        print("\nRandom NPC Encounter:")
        print(f"You bump into {npc.name}:")
        print(npc.description)

        # Call the interact_with_npcs function to handle the interaction
        interact_with_npc(player, npc)
    else:
        print("\nNo random NPC encounter this time.")
        
def simulate_collaboration(player):
    # Define the range for possible fame and money changes
    min_fame_change = 10
    max_fame_change = 30
    min_money_earned = 50
    max_money_earned = 200

    # Simulate a random fame change and money earned within the defined range
    fame_change = random.randint(min_fame_change, max_fame_change)
    money_earned = random.randint(min_money_earned, max_money_earned)

    # Determine whether the collaboration has a positive or negative impact on the player
    if random.random() < 0.5:
        # Positive collaboration, increase fame and money
        player.total_fame += fame_change
        player.money += money_earned
    else:
        # Negative collaboration, decrease fame and money
        fame_change = -fame_change
        money_earned = -money_earned
        player.total_fame += fame_change
        player.money += money_earned

    # Create a dictionary to represent the collaboration result
    collaboration_result = {
        "fame_change": fame_change,
        "money_earned": money_earned
    }

    return collaboration_result

def interact_with_npc(player, npc):
    print(f"\nYou approach {npc.name}:")
    print(npc.description)
    
    if npc.name == "DJ Scratch":
        print("\nDJ Scratch offers to teach you advanced scratching techniques.")
        choice = input("Do you want to learn from DJ Scratch? (yes/no): ")
        if choice.lower() == "yes":
            print("You spend time learning from the master, improving your DJ skills.")
            player.total_fame += 20
            print("Your fame increases by 20 points.")
        else:
            print("You decline the offer.")
    
    elif npc.name == "Lyricist Lila":
        print("\nLyricist Lila suggests a collaboration on a new track.")
        choice = input("Do you want to collaborate with Lyricist Lila? (yes/no): ")
        if choice.lower() == "yes":
            collaboration_result = simulate_collaboration(player)
            player.total_fame += collaboration_result["fame_change"]
            player.money += collaboration_result["money_earned"]
            print(f"You and Lyricist Lila create a fantastic track together.")
            print(f"Fame Change: {collaboration_result['fame_change']}")
            print(f"Money Earned: {collaboration_result['money_earned']}")
        else:
            print("You decline the collaboration offer.")
    
    elif npc.name == "Big Money Records Agent":
        print("\nThe agent from Big Money Records is interested in signing you.")
        choice = input("Do you want to negotiate a deal with the agent? (yes/no): ")
        if choice.lower() == "yes":
            print("You negotiate a deal, and your fortune increases significantly.")
            player.money += 1000
            print("Your fortune increases by 1000 points.")
        else:
            print("You decline the agent's offer.")
    
    elif npc.name == "B-Boy Benny":
        print("\nB-Boy Benny invites you to a breakdance battle.")
        choice = input("Do you want to battle Benny? (yes/no): ")
        if choice.lower() == "yes":
            dance_off_result = simulate_dance_off(player)
            if dance_off_result["win"]:
                print("You defeat Benny with your impressive breakdancing moves.")
                player.total_fame += 30
                print("Your fame increases by 30 points.")
            else:
                print("B-Boy Benny outperforms you in the battle.")
                player.total_fame += 10
                print("Your fame increases by 10 points.")
        else:
            print("You decline the battle invitation.")
            
    elif npc.name == "Graffiti Guru Gabby":
        print("\nGraffiti Guru Gabby offers you a mural project.")
        choice = input("Do you want to create a mural with Gabby? (yes/no): ")
        if choice.lower() == "yes":
            print("You collaborate with Gabby on an amazing mural project.")
            player.total_fame += 40
            print("Your fame increases by 40 points.")
        else:
            print("You decline the mural project.")
    
    elif npc.name == "Radio DJ Remy":
        print("\nRadio DJ Remy wants to play your tracks on the radio.")
        choice = input("Do you want Remy to play your tracks? (yes/no): ")
        if choice.lower() == "yes":
            print("Remy starts playing your tracks, boosting your fame.")
            player.total_fame += 30
            print("Your fame increases by 30 points.")
        else:
            print("You decline Remy's offer.")
    
    elif npc.name == "Beat Producer Max":
        print("\nBeat Producer Max is working on a new beat and notices you.")
        print("He offers to collaborate with you on a track and provide a beat for your lyrics.")
        
        choice = input("Do you want to collaborate with Beat Producer Max? (yes/no): ")
        
        if choice.lower() == "yes":
            # Simulate the collaboration with Beat Producer Max
            collaboration_result = collaborate_with_producer(player)
            
            # Update player's fame and fortune based on the collaboration result
            player.total_fame += collaboration_result["fame_change"]
            player.money += collaboration_result["money_earned"]
            
            print("You and Beat Producer Max create an amazing track together.")
            print(f"Fame Change: {collaboration_result['fame_change']}")
            print(f"Money Earned: {collaboration_result['money_earned']}")
        else:
            print("You decline Beat Producer Max's offer.")
        
    elif npc.name == "Street Poet Piper":
            print("\nStreet Poet Piper suggests a collaboration on a spoken word project.")
            choice = input("Do you want to collaborate with Piper? (yes/no): ")
            if choice.lower() == "yes":
                collaboration_result = simulate_collaboration(player)
                player.total_fame += collaboration_result["fame_change"]
                player.money += collaboration_result["money_earned"]
                print(f"You and Street Poet Piper create a unique spoken word piece.")
                print(f"Fame Change: {collaboration_result['fame_change']}")
                print(f"Money Earned: {collaboration_result['money_earned']}")
            else:
                print("You decline the collaboration offer.")
    
    elif npc.name == "Hip-Hop Historian Hank":
        print("\nHip-Hop Historian Hank shares some insights about hip-hop culture.")
        print("You gain knowledge about hip-hop history.")
    
    elif npc.name == "Cypher Champion Carlos":
        print("\nYou approach Cypher Champion Carlos, who is known for his incredible skills in freestyle rap battles.")
        print("Carlos challenges you to a rap battle right here and now.")
        
        choice = input("Do you accept Carlos's rap battle challenge? (yes/no): ")
        
        if choice.lower() == "yes":
            # Simulate the rap battle with Cypher Champion Carlos
            battle_result = rap_battle_with_carlos(player)
            
            # Update player's fame and fortune based on the battle result
            player.total_fame += battle_result["fame_change"]
            player.money += battle_result["money_earned"]
            
            print("You engage in an intense rap battle with Cypher Champion Carlos.")
            print(f"Fame Change: {battle_result['fame_change']}")
            print(f"Money Earned: {battle_result['money_earned']}")
        else:
            print("You decline Carlos's rap battle challenge.")

    
    elif npc.name == "Dance Crew Leader Destiny":
        print("\nYou find Destiny, the leader of a renowned dance crew, practicing some incredible dance moves.")
        print("Destiny invites you to join their crew and participate in an upcoming dance competition.")
        
        choice = input("Do you want to join Destiny's dance crew? (yes/no): ")
        
        if choice.lower() == "yes":
            # Simulate joining Destiny's dance crew and preparing for the competition
            crew_joining_result = join_destiny_crew(player)
            
            # Update player's fame and fortune based on the joining result
            player.total_fame += crew_joining_result["fame_change"]
            
            print("You become a member of Destiny's dance crew and start practicing for the competition.")
            print(f"Fame Change: {crew_joining_result['fame_change']}")
        else:
            print("You decline Destiny's invitation to join the dance crew.")
            
def collaborate_with_producer(player):
    print("\nYou decide to collaborate with Beat Producer Max.")
    
    # Simulate the collaboration process
    collaboration_result = {}
    
    # Simulate the creative process
    creativity = random.randint(1, 10)  # Simulate creativity in the collaboration
    player_fame_increase = creativity * 5  # Adjust as needed
    player_money_earned = creativity * 20  # Adjust as needed
    
    # Update player's fame and money based on the collaboration
    player.total_fame += player_fame_increase
    player.money += player_money_earned
    
    # Simulate the outcome and player's experience
    if creativity >= 7:
        print("Your collaboration with Beat Producer Max results in an incredibly creative track.")
        collaboration_result["success"] = True
    else:
        print("While the collaboration was fun, the track didn't turn out as expected.")
        collaboration_result["success"] = False
    
    # Provide feedback based on the outcome
    if collaboration_result["success"]:
        print(f"Your fame increases by {player_fame_increase} points.")
        print(f"You earn ${player_money_earned} from this collaboration.")
    else:
        print(f"Your fame increases by {player_fame_increase} points, but the track didn't perform well.")
        print(f"You earn ${player_money_earned} from this collaboration.")
    
    # Return the collaboration result as a dictionary
    collaboration_result["fame_change"] = player_fame_increase
    collaboration_result["money_earned"] = player_money_earned
    
    return collaboration_result
            
def rap_battle_with_carlos(player):
    # Define the range for possible fame change and money earned
    min_fame_change = 10
    max_fame_change = 30
    min_money_earned = 50
    max_money_earned = 200

    # Simulate a random fame change and money earned within the defined ranges
    fame_change = random.randint(min_fame_change, max_fame_change)
    money_earned = random.randint(min_money_earned, max_money_earned)

    # Determine whether the player wins the rap battle
    if random.random() < 0.5:
        # Player wins, increase fame and money
        player.total_fame += fame_change
        player.money += money_earned
        battle_result = {
            "fame_change": fame_change,
            "money_earned": money_earned,
            "win": True
        }
    else:
        # Player loses, decrease fame (no money earned)
        fame_change = -fame_change
        player.total_fame += fame_change
        battle_result = {
            "fame_change": fame_change,
            "money_earned": 0,
            "win": False
        }

    return battle_result

def join_destiny_crew(player):
    # Define the range for possible fame change
    min_fame_change = 20
    max_fame_change = 40

    # Simulate a random fame change within the defined range
    fame_change = random.randint(min_fame_change, max_fame_change)

    # Determine whether the crew membership has a positive or negative impact on the player
    if random.random() < 0.5:
        # Positive crew membership, increase fame and set membership status to "Active"
        player.total_fame += fame_change
        crew_membership_status = "Active"
    else:
        # Negative crew membership, decrease fame and set membership status to "Inactive"
        fame_change = -fame_change
        player.total_fame += fame_change
        crew_membership_status = "Inactive"

    # Create a dictionary to represent the crew membership result
    crew_joining_result = {
        "fame_change": fame_change,
        "crew_membership_status": crew_membership_status
    }

    return crew_joining_result
    
def simulate_dance_off(player):
    # Define dance-off difficulty and player's skill level
    dance_off_difficulty = random.randint(1, 10)
    player_skill_level = player.dance_skill

    # Determine the outcome of the dance-off
    if player_skill_level >= dance_off_difficulty:
        # Player wins the dance-off
        player.total_fame += 20
        return {
            "win": True,
            "fame_change": 20,
        }
    else:
        # Player loses the dance-off
        player.total_fame -= 10
        return {
            "win": False,
            "fame_change": -10,
        }

def write_track(player):
    print("\nWriting a New Track:")
    
    # Check if the player has already written a song
    if player.has_written_song:
        print(f"{player.name}, you've already written a song today. Try again tomorrow.")
        return
    
    print(f"You sit down to write a new track as {player.name}.")

    # Generate a random prompt or theme for the track
    track_prompt = generate_track_prompt()

    print(f"Your track's theme: {track_prompt}")
    print("Now, it's time to write the lyrics.")

    # Allow the player to input lyrics
    lyrics = input("Enter your lyrics (one line at a time, enter 'done' to finish):\n")
    track_lyrics = []

    while lyrics.lower() != 'done':
        track_lyrics.append(lyrics)
        lyrics = input()

    # Prompt the player to name the song
    song_name = input("Enter the name of the song: ")

    # Calculate the quality of the track based on the length and creativity of lyrics
    track_quality = calculate_track_quality(track_lyrics)

    # Update player's fame and fortune based on track quality
    player.total_fame += track_quality
    player.money += track_quality

    # Set the has_written_song flag to True
    player.has_written_song = True

    # Store the song name and lyrics in the player's songs dictionary
    player.songs[song_name] = track_lyrics

    # Increment the day
    player.day += 1

    print("\nYou've successfully written a track!")
    print(f"Track Quality: {track_quality}")
    print(f"Current Fame: {player.total_fame}")
    print(f"Current Fortune: {player.money}")

def display_songs(player):
    if player.songs:
        print("\nYour Written Songs:")
        for song_title in player.songs:
            print(f"Title: {song_title}")
            print("Lyrics:")
            for line in player.songs[song_title]:
                print(line)
            print()
    else:
        print("You haven't written any songs yet.")

def perform(player):
    print("\nPerforming at a Local Venue:")
    if not player.has_written_song:
        print("You can't perform until you have written a song.")
        return

    print(f"You, {player.name}, are about to perform at a local hip-hop venue.")

    # Display the list of your songs
    print("\nYour Songs:")
    song_titles = list(player.songs.keys())
    for i, song_title in enumerate(song_titles):
        print(f"{i + 1}. {song_title}")
    
    # Prompt the player to choose a song to perform
    choice = input("Enter the number of the song you want to perform: ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(song_titles):
            selected_song = song_titles[choice - 1]
            print(f"You are performing '{selected_song}'.")

            # Get the lyrics of the selected song
            song_lyrics = player.songs[selected_song]

            # Simulate the performance
            performance_result = simulate_performance(player, song_lyrics)

            # Update player's fame and fortune based on the performance result
            player.total_fame += performance_result["fame_change"]
            player.money += performance_result["money_earned"]

            # Display performance results
            print("\nPerformance Results:")
            print(f"Fame Change: {performance_result['fame_change']}")
            print(f"Money Earned: {performance_result['money_earned']}")
            print(f"Current Fame: {player.total_fame}")
            print(f"Current Fortune: {player.money}")
        else:
            print("Invalid choice. Please select a valid song.")
    else:
        print("Invalid input. Please enter a number.")

# Simulate the performance and determine its outcome
def simulate_performance(player, song_lyrics):
    print("Your performance begins...")

    # Simulate audience reaction (random value between 1 and 10)
    audience_reaction = random.randint(1, 10)

    # Simulate song quality (random value between 1 and 10)
    song_quality = random.randint(1, 10)

    # Calculate performance score based on audience reaction and song quality
    performance_score = (audience_reaction + song_quality) // 2

    # Determine performance outcome
    if performance_score >= 8:
        print("The crowd is ecstatic! Your performance was a huge success.")
        fame_change = random.randint(20, 40)
        money_earned = random.randint(200, 400)
    elif performance_score >= 5:
        print("The crowd enjoyed your performance.")
        fame_change = random.randint(10, 20)
        money_earned = random.randint(100, 200)
    else:
        print("The crowd seemed indifferent to your performance.")
        fame_change = random.randint(5, 10)
        money_earned = random.randint(50, 100)

    # Return performance results
    performance_result = {
        "fame_change": fame_change,
        "money_earned": money_earned
    }

    return performance_result

def collaborate(player):
    print("\nCollaborating with Other Artists:")
    print(f"You, {player.name}, have an opportunity to collaborate with another artist.")

    # Simulate the collaboration
    collaboration_result = simulate_collaboration(player)

    # Update player's fame and fortune based on the collaboration result
    player.total_fame += collaboration_result["fame_change"]
    player.money += collaboration_result["money_earned"]
    
    # Increment the day
    player.day += 1

    # Display collaboration results
    print("\nCollaboration Results:")
    print(f"Fame Change: {collaboration_result['fame_change']}")
    print(f"Money Earned: {collaboration_result['money_earned']}")
    print(f"Current Fame: {player.total_fame}")
    print(f"Current Fortune: {player.money}")

# Simulate the collaboration and determine its outcome
def simulate_collaboration(player):
    print("Your collaboration begins...")

    # Simulate collaboration quality (random value between 1 and 10)
    collaboration_quality = random.randint(1, 10)

    # Simulate compatibility with the other artist (random value between 1 and 10)
    compatibility = random.randint(1, 10)

    # Calculate collaboration score based on quality and compatibility
    collaboration_score = (collaboration_quality + compatibility) // 2

    # Update player's total fame and fortune based on the collaboration result
    player.total_fame += collaboration_score  # Use total_fame instead of fame
    player.money += collaboration_score  # Removed ["money_earned"] here

    # Set the has_written_song attribute to True after collaboration
    player.has_written_song = True

    # Determine collaboration outcome
    if collaboration_score >= 8:
        print("The collaboration was a masterpiece! Fans are loving it.")
        fame_change = random.randint(30, 50)
        money_earned = random.randint(300, 500)
    elif collaboration_score >= 5:
        print("The collaboration was decent, and it gained some attention.")
        fame_change = random.randint(15, 30)
        money_earned = random.randint(150, 300)
    else:
        print("The collaboration didn't turn out as expected.")
        fame_change = random.randint(5, 15)
        money_earned = random.randint(50, 150)

    # Return collaboration results
    collaboration_result = {
        "fame_change": fame_change,
        "money_earned": money_earned
    }

    return collaboration_result

def grow_fan_base(player):
    print("\nGrowing Your Fan Base:")
    
    # Simulate fan base growth based on various factors
    fan_growth = calculate_fan_growth(player)
    
    # Increment the day
    player.day += 1

    # Update the player's fame and fan base
    player.total_fame += fan_growth

    # Display fan base growth results
    print(f"Fan Base Growth: +{fan_growth}")
    print(f"Current Fame: {player.total_fame}")
    
def calculate_fan_growth(player):
    if player.total_fame >= 50:
        fan_growth = random.randint(50, 100)
    elif player.total_fame >= 30:
        fan_growth = random.randint(30, 60)
    elif player.total_fame >= 10:
        fan_growth = random.randint(10, 40)
    else:
        fan_growth = random.randint(1, 10)

    return fan_growth

def quit_game():
    print("Thanks for playing!")
    exit()

# Start the game
if __name__ == "__main__":
    start_game()
