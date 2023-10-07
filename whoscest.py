import random
import time
import requests

# Function to get IP information from a free API
def get_ip_info(ip_address):
    url = f"https://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to generate a random event
def generate_random_event():
    events = [
        ("Double Points", "Your score is doubled for this scan!"),
        ("Half Points", "Your score is halved for this scan!"),
        ("Time Warp", "Time slows down for this scan!"),
        ("Network Attack", "You have to defend against a network attack!"),
        # Add more events as desired
    ]
    return random.choice(events)

# Function to generate a random power-up
def generate_power_up():
    power_ups = [
        ("Double Points", "Doubles your score for the next scan."),
        ("Time Freeze", "Freezes time for the next scan."),
        ("Shield", "Protects against network attacks for the next scan."),
        ("Double XP", "Earns double XP for the next scan."),
        ("Immunity", "Grants immunity to one trivia question."),
        # Add more power-ups as desired
    ]
    return random.choice(power_ups)

# Function to generate a random network vulnerability
def generate_network_vulnerability():
    vulnerabilities = [
        ("Firewall Weakness", "Scans may incorrectly report open ports."),
        ("DDoS Vulnerability", "Scans may take longer to complete."),
        ("Intrusion Detection System", "Scans may trigger alerts."),
        # Add more vulnerabilities as desired
    ]
    return random.choice(vulnerabilities)

# Function to generate a random enemy hacker
def generate_enemy_hacker():
    hackers = [
        ("DarkByte", 100),  # Hacker name and XP required to defeat
        ("CyberPhantom", 150),
        ("ShadowSlicer", 200),
        ("GhostWraith", 250),
        ("NinjaHacker", 300),
        # Add more hackers as desired
    ]
    return random.choice(hackers)

# Function to generate a quest hacker
def generate_quest_hacker():
    quest_hackers = [
        ("QuestHacker1", 120),  # Quest hacker name and XP required to defeat
        ("QuestHacker2", 180),
        ("QuestHacker3", 220),
        # Add more quest hackers as desired
    ]
    return random.choice(quest_hackers)

# Function to generate the final boss
def generate_final_boss():
    return ("FinalBoss", 1000)

# Function to generate a random skill challenge
def generate_skill_challenge():
    challenges = [
        ("Hacking Challenge", "You must successfully complete a hacking challenge to earn extra points."),
        # Add more skill challenges as desired
    ]
    return random.choice(challenges)

# Function to calculate IP address class
def calculate_ip_class(ip_address):
    first_octet = int(ip_address.split(".")[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Reserved)"
    else:
        return "Invalid"

# Basic game setup
player_name = input("Enter your player name: ")
score = 0
level = 1
inventory = []  # Player's inventory for power-ups
leaderboard = []  # List to track high scores
xp = 0  # Player's experience points
skill_points = 0  # Skill points for player
hacking_skill_level = 1  # Hacking skill level

# Define available hacking skills and their effects
hacking_skills = {
    "Skillful Hacker": {"description": "Increases hacking success rate.", "success_rate_increase": 0.1},
    "Speedy Hacker": {"description": "Reduces hacking challenge time.", "time_reduction": 2},
    "Stealth Hacker": {"description": "Decreases enemy hacker XP requirements.", "xp_reduction": 20},
    # Add more hacking skills as desired
}

# Initialize quest giver state
quest_giver_appeared = False
quest_completed = False

# Initialize final boss state
final_boss_encountered = False

# Game loop
while True:
    print(f"\nLevel {level}")

    # Generate a list of random IP addresses to scan
    num_ip_addresses_per_level = 5  # Adjust the number of IP addresses as desired
    ip_addresses = [f"192.168.1.{random.randint(1, 255)}" for _ in range(num_ip_addresses_per_level)]

    print(f"IP Addresses to Scan: {', '.join(ip_addresses)}")

    for target_ip in ip_addresses:
        print(f"\nScanning {target_ip}...")

        # Generate a random event
        event_name, event_description = generate_random_event()
        print(f"Event: {event_name} - {event_description}")

        # Apply event effects on the scan
        event_multiplier = 1
        if event_name == "Double Points":
            event_multiplier = 2
        elif event_name == "Half Points":
            event_multiplier = 0.5

        # Check if the player has a "Time Freeze" power-up
        time_frozen = "Time Freeze" in inventory

        # Simulate scanning with potential time freeze
        if not time_frozen:
            time.sleep(2)  # Simulate a 2-second scan (adjust as needed)

        # Simulate network vulnerabilities
        network_vulnerability_name, network_vulnerability_description = generate_network_vulnerability()
        print(f"Network Vulnerability: {network_vulnerability_name} - {network_vulnerability_description}")

        is_open_ports = [random.choice([True, False]) for _ in range(1, 101)]

        open_ports = [i + 1 for i, is_open in enumerate(is_open_ports) if is_open]

        print(f"Open ports: {open_ports}")

        # Apply event and power-up effects on the score
        score_gain = event_multiplier * len(open_ports)

        # Check if the player has a "Double Points" power-up
        if "Double Points" in inventory:
            score_gain *= 2

        score += score_gain

    print(f"\nYour current score: {score}")

    # Update XP based on the player's score
    xp += score // 10  # Adjust this value as needed

    print(f"Your XP: {xp}")

    # Check if the player can attack an enemy hacker
    if xp >= 100:
        enemy_hacker, xp_required = generate_enemy_hacker()
        print(f"\nYou've encountered an enemy hacker: {enemy_hacker} (XP Required: {xp_required})")
        attack_choice = input("Do you want to attack the hacker? (yes/no): ").lower()

        if attack_choice == "yes":
            if xp >= xp_required:
                print(f"You've successfully defeated {enemy_hacker}!")
                xp -= xp_required
            else:
                print(f"You need {xp_required} XP to defeat {enemy_hacker}. Continue scanning to build XP.")

    # Check if the player can attempt a skill challenge
    if skill_points >= 10:
        skill_challenge, skill_description = generate_skill_challenge()
        print(f"\nYou've encountered a skill challenge: {skill_challenge} - {skill_description}")
        challenge_choice = input("Do you want to attempt the skill challenge? (yes/no): ").lower()

        if challenge_choice == "yes":
            skill_points -= 10  # Deduct skill points for the challenge

            # Simulate a hacking challenge (customize as needed)
            print("Hacking Challenge: Crack the password within 30 seconds.")
            target_password = "password123"
            attempts = 3  # Number of attempts allowed

            for _ in range(attempts):
                user_guess = input(f"Attempt {attempts - _}. Enter password guess: ")

                if user_guess == target_password:
                    print("Congratulations! You successfully hacked the system.")
                    score += 50  # Award extra points for the challenge
                    break
                else:
                    print("Incorrect guess. Keep trying!")

    # Check if the player has defeated DarkByte and the quest giver has not appeared yet
    if xp >= 100 and not quest_giver_appeared:
        print("\nYou've defeated DarkByte!")
        print("A mysterious quest giver appears.")
        print("Quest Giver: Hello, brave hacker! I have a quest for you.")
        print("Quest Giver: There's a dangerous hacker called 'QuestHacker' on the loose.")
        print("Quest Giver: I need you to defeat 'QuestHacker' and bring justice to the network.")
        quest_choice = input("Quest Giver: Will you accept this quest? (yes/no): ").lower()

        if quest_choice == "yes":
            quest_giver_appeared = True
            quest_hacker, quest_xp_required = generate_quest_hacker()
            print(f"\nYou've accepted the quest to defeat '{quest_hacker}' (XP Required: {quest_xp_required}).")
        else:
            print("Quest Giver: Very well. If you change your mind, I'll be here.")

    # Check if the player has completed the quest by defeating the quest hacker
    if quest_giver_appeared and not quest_completed:
        if xp >= quest_xp_required:
            print(f"\nYou've successfully defeated '{quest_hacker}' and completed the quest!")
            xp -= quest_xp_required
            quest_completed = True
            print("Quest Giver: Thank you, brave hacker! Here's your reward of 50 XP.")
            xp += 50

    # Check if the player has reached the level for the final boss encounter
    if level >= 10 and not final_boss_encountered:
        print("\nYou've reached level 10! The final boss, 'FinalBoss,' appears.")
        print("Prepare for the ultimate showdown!")
        final_boss_encountered = True
        final_boss, final_boss_xp_required = generate_final_boss()
        print(f"\nYou've encountered the final boss: '{final_boss}' (XP Required: {final_boss_xp_required}).")
        attack_choice = input("Do you want to attack the final boss? (yes/no): ").lower()

        if attack_choice == "yes":
            if xp >= final_boss_xp_required:
                print(f"You've successfully defeated '{final_boss}' and completed the game!")
                xp -= final_boss_xp_required
                print(f"Congratulations, {player_name}! You've completed the game.")
                print(f"Your final score: {score}")
                break
            else:
                print(f"You need {final_boss_xp_required} XP to defeat '{final_boss}'. Continue scanning to build XP.")

# End of the game loop
