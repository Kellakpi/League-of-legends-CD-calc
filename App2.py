# Dictionary containing character information with ability cooldowns
champion_info = {
    "aatrox": {
        "ability_cooldowns": {"Q1": 14,"Q2": 12,"Q3": 10,"Q4": 8,"Q5": 6,
                              "W1": 20, "W2": 18, "W3": 16, "W4": 14, "W5": 12,
                              "E1": 9, "E2": 8, "E3": 7, "E4": 6, "E5": 5,
                              "R1": 120, "R2": 100, "R3": 80}
    },
  "ahri": {
        "ability_cooldowns": {"Q1": 7,"Q2": 7,"Q3": 7,"Q4": 7,"Q5": 7,
                              "W1": 9, "W2": 8, "W3": 7, "W4": 6, "W5": 5,
                              "E1": 14, "E2": 14, "E3": 14, "E4": 14, "E5": 14,
                              "R1": 130, "R2": 105, "R3": 80}
    },

    }
    # Add more champion information as needed


# Get input from the user
champion_name = input("Enter the champion name: ").lower()
ability_haste = float(input("Enter the ability haste value: "))

# Check if the champion exists in the dictionary
if champion_name in champion_info:
    champion = champion_info[champion_name]
    ability_cooldowns = champion["ability_cooldowns"]

    # Apply ability haste to the cooldowns
    for ability, cooldown in ability_cooldowns.items():
        new_cooldown = cooldown * (1 - min(0.8, ability_haste / 100))
        ability_cooldowns[ability] = round(new_cooldown, 2)

    # Display the updated cooldowns
    print(f"Updated cooldowns for {champion_name.title()} with {ability_haste}% ability haste:")
    for ability, cooldown in ability_cooldowns.items():
        print(f"{ability}: {cooldown} seconds")
else:
    print("Who is that?")
