import json
import os

def generate_mystical_metadata(filenames, base_url, output_dir="metadata"):
    """
    Generates mystical and beautiful metadata for a list of creature filenames and saves each as a JSON file.

    Args:
        filenames (list): A list of filenames (e.g., ["001.lion.webp", "002.tiger.webp"]).
        base_url (str): The base URL for the IPFS gateway.
        output_dir (str): The directory to save the metadata files.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate metadata for each creature
    for filename in filenames:
        # Extract the image number and name
        image_number = filename.split(".")[0]
        name = filename.split(".")[1].replace("_", " ").title()

        # Format the image URL
        image_url = f"{base_url}/{filename}"

        # Generate mystical and beautiful metadata
        metadata = {
            "name": name,
            "description": get_description(name),
            "image": image_url,
            "external_url": "https://yourwebsite.com/collection",
            "artist": "Mystic Artist",
            "collection": "Mystic Creatures Collection",
            "conservation_status": get_conservation_status(name),
            "attributes": get_attributes(name)
        }

        # Save metadata to a JSON file
        metadata_file = os.path.join(output_dir, f"{image_number}.json")
        with open(metadata_file, "w") as file:
            json.dump(metadata, file, indent=4)

        print(f"Generated mystical metadata for {name} ({image_number}.json)")

def get_description(name):
    """
    Returns a mystical and beautiful description for the creature.
    """
    descriptions = {
        "Lion": "The Lion, a celestial guardian of the savanna, roars with the power of the sun and rules with the wisdom of the stars.",
        "Tiger": "The Tiger, a shadowy sovereign of the jungle, moves with the grace of moonlight and strikes with the fury of thunder.",
        "Jaguar": "The Jaguar, a spirit of the rainforest, embodies the mysteries of the night and the secrets of the earth.",
        "Leopard": "The Leopard, a phantom of the wilderness, wears the stars on its coat and moves like a whisper in the wind.",
        "Panda": "The Panda, a gentle sage of the bamboo forests, carries the balance of yin and yang in its serene gaze.",
        "Polar Bear": "The Polar Bear, a titan of the frozen realms, walks where the auroras dance and the ice sings.",
        "Brown Bear": "The Brown Bear, a keeper of the ancient woods, holds the strength of mountains and the warmth of the hearth.",
        "African Elephant": "The African Elephant, a colossus of the plains, carries the memory of the earth and the wisdom of the ages.",
        "Asian Elephant": "The Asian Elephant, a sacred guardian of the forests, walks with the grace of the moon and the power of the earth.",
        "White Rhino": "The White Rhino, a living fortress of the grasslands, stands as a testament to resilience and ancient power.",
        "Black Rhino": "The Black Rhino, a shadow of the savanna, moves with the silence of the night and the strength of the storm.",
        "Giraffe": "The Giraffe, a celestial sentinel of the plains, reaches for the heavens and touches the stars.",
        "Zebra": "The Zebra, a spirit of the savanna, wears the stripes of the sun and dances with the rhythm of the earth.",
        "Hippopotamus": "The Hippopotamus, a river deity of the wetlands, commands the waters and guards the secrets of the deep.",
        "Seal": "The Seal, a child of the ocean, swims with the currents and sings with the waves.",
        "Sea Lion": "The Sea Lion, a guardian of the shores, basks in the sun and dances with the tides.",
        "Dolphin": "The Dolphin, a messenger of the sea, leaps with joy and carries the songs of the ocean.",
        "Blue Whale": "The Blue Whale, a leviathan of the deep, holds the mysteries of the abyss and the songs of the stars.",
        "Humpback Whale": "The Humpback Whale, a bard of the ocean, sings the ancient hymns of the sea.",
        "Great White Shark": "The Great White Shark, a phantom of the depths, moves with the silence of the abyss and the power of the storm.",
        "Whale Shark": "The Whale Shark, a gentle giant of the ocean, glides through the waters with the grace of a cloud.",
        "Penguin": "The Penguin, a wanderer of the ice, dances on the frozen stage and swims in the cold embrace of the sea.",
        "Eagle": "The Eagle, a sovereign of the skies, soars with the winds and sees the world with the eyes of the sun.",
        "Owl": "The Owl, a sage of the night, holds the secrets of the moon and the wisdom of the stars.",
        "Peacock": "The Peacock, a jewel of the earth, wears the colors of the rainbow and dances with the light of the sun.",
        "Flamingo": "The Flamingo, a spirit of the waters, stands on one leg and dreams with the colors of the sunset.",
        "Parrot": "The Parrot, a bard of the forests, speaks the language of the earth and sings the songs of the sky.",
        "Hummingbird": "The Hummingbird, a spark of life, flutters with the speed of light and drinks the nectar of the stars.",
        "Kangaroo": "The Kangaroo, a traveler of the outback, leaps with the rhythm of the earth and carries the future in its pouch.",
        "Koala": "The Koala, a dreamer of the eucalyptus, sleeps with the stars and wakes with the sun.",
        "Wallaby": "The Wallaby, a shadow of the bush, hops with the silence of the night and the grace of the moon.",
        "Wombat": "The Wombat, a burrower of the earth, digs deep into the heart of the land and guards its secrets.",
        "King Cobra": "The King Cobra, a ruler of the shadows, moves with the silence of the night and the power of the storm.",
        "Python": "The Python, a spirit of the earth, coils with the patience of time and strikes with the speed of lightning.",
        "Komodo": "The Komodo, a dragon of the islands, walks with the strength of the earth and the fire of the sun.",
        "Crocodile": "The Crocodile, a guardian of the rivers, waits with the patience of stone and strikes with the fury of the storm.",
        "Nile Crocodile": "The Nile Crocodile, a titan of the waters, holds the power of the river and the secrets of the deep.",
        "Alligator": "The Alligator, a shadow of the swamps, moves with the silence of the night and the strength of the earth.",
        "Turtle": "The Turtle, a wanderer of the waters, carries the wisdom of the ages and the patience of the stars.",
        "Tortoise": "The Tortoise, a sage of the land, walks with the slowness of time and the wisdom of the earth.",
        "Dart Frog": "The Dart Frog, a jewel of the rainforest, wears the colors of the sun and carries the poison of the stars.",
        "Green Frog": "The Green Frog, a spirit of the waters, sings with the voice of the rain and dances with the rhythm of the earth.",
        "Butterfly": "The Butterfly, a dream of the sky, flutters with the colors of the rainbow and the light of the sun.",
        "Honeybee": "The Honeybee, a worker of the earth, dances with the rhythm of the flowers and carries the sweetness of the sun.",
        "Ant": "The Ant, a builder of the earth, carries the weight of the world and the strength of the stars.",
        "Tarantula": "The Tarantula, a weaver of the night, spins the threads of the moon and guards the secrets of the earth.",
        "Beetle": "The Beetle, a jewel of the earth, wears the armor of the sun and carries the strength of the stars.",
        "Octopus": "The Octopus, a phantom of the deep, moves with the silence of the abyss and the intelligence of the stars.",
        "Squid": "The Squid, a shadow of the ocean, swims with the speed of light and the mystery of the night.",
        "Starfish": "The Starfish, a child of the sea, wears the shape of the stars and dreams with the colors of the ocean.",
        "Crab": "The Crab, a wanderer of the shores, walks with the patience of the earth and the strength of the tides.",
        "Lobster": "The Lobster, a guardian of the deep, carries the armor of the sun and the secrets of the ocean.",
        "Seahorse": "The Seahorse, a spirit of the waters, dances with the rhythm of the waves and the grace of the stars.",
        "Clownfish": "The Clownfish, a jewel of the reef, wears the colors of the sun and dances with the anemones.",
        "Hammerhead Shark": "The Hammerhead Shark, a phantom of the deep, swims with the silence of the abyss and the power of the storm.",
        "Manta Ray": "The Manta Ray, a shadow of the ocean, glides with the grace of the stars and the mystery of the night.",
        "Wild Boar": "The Wild Boar, a warrior of the forest, charges with the strength of the earth and the fury of the storm.",
        "Antelope": "The Antelope, a spirit of the plains, runs with the speed of the wind and the grace of the stars.",
        "Bison": "The Bison, a titan of the grasslands, walks with the strength of the earth and the power of the sun.",
        "Mountain Goat": "The Mountain Goat, a climber of the heights, scales the peaks with the grace of the stars and the strength of the earth.",
        "Sheep": "The Sheep, a dreamer of the fields, grazes with the patience of the earth and the peace of the stars.",
        "Goat": "The Goat, a wanderer of the hills, climbs with the strength of the earth and the curiosity of the stars.",
        "Camel": "The Camel, a traveler of the deserts, walks with the patience of the earth and the endurance of the stars.",
        "Dromedary": "The Dromedary, a spirit of the sands, carries the weight of the sun and the secrets of the desert.",
        "Wolf": "The Wolf, a shadow of the forest, howls with the voice of the moon and runs with the speed of the wind.",
        "Fox": "The Fox, a trickster of the night, moves with the silence of the stars and the cunning of the earth.",
        "Raccoon": "The Raccoon, a thief of the night, wears the mask of the moon and carries the secrets of the earth.",
        "Ferret": "The Ferret, a spirit of the burrows, moves with the speed of the wind and the curiosity of the stars.",
        "Otter": "The Otter, a child of the waters, plays with the joy of the sun and the grace of the stars.",
        "Beaver": "The Beaver, a builder of the rivers, shapes the earth with the patience of the stars and the strength of the sun.",
        "Mole": "The Mole, a digger of the earth, moves with the silence of the night and the strength of the stars.",
        "Porcupine": "The Porcupine, a guardian of the forest, wears the armor of the stars and carries the strength of the earth.",
        "Rabbit": "The Rabbit, a dreamer of the fields, hops with the speed of the wind and the grace of the stars.",
        "Squirrel": "The Squirrel, a gatherer of the forests, moves with the speed of the wind and the curiosity of the stars.",
        "Gorilla": "The Gorilla, a king of the jungle, walks with the strength of the earth and the wisdom of the stars.",
        "Chimpanzee": "The Chimpanzee, a spirit of the forest, moves with the intelligence of the stars and the curiosity of the earth.",
        "Orangutan": "The Orangutan, a dreamer of the trees, swings with the grace of the stars and the patience of the earth.",
        "Baboon": "The Baboon, a warrior of the plains, walks with the strength of the earth and the cunning of the stars.",
        "Gibbon": "The Gibbon, a singer of the forests, swings with the grace of the stars and the joy of the sun.",
        "Bat": "The Bat, a phantom of the night, flies with the silence of the stars and the mystery of the moon.",
        "Amazon Dolphin": "The Amazon Dolphin, a spirit of the rivers, swims with the grace of the stars and the joy of the sun.",
        "Walrus": "The Walrus, a titan of the ice, basks in the sun and guards the secrets of the frozen seas.",
        "Narwhal": "The Narwhal, a unicorn of the ocean, swims with the grace of the stars and the mystery of the moon.",
        "Orca": "The Orca, a phantom of the deep, moves with the silence of the abyss and the power of the storm.",
        "Maui Dolphin": "The Maui Dolphin, a jewel of the ocean, swims with the grace of the stars and the joy of the sun.",
        "Monarch Butterfly": "The Monarch Butterfly, a dream of the sky, flutters with the colors of the rainbow and the light of the sun.",
        "Samurai Cat": "The Samurai Cat, a warrior of the night, wears the armor of the stars and wields the katana of the moon.",
        "Husky": "The Husky, a spirit of the snow, runs with the speed of the wind and the strength of the stars.",
        "Tentacule": "The Tentacule, a phantom of the deep, moves with the silence of the abyss and the mystery of the night.",
        "Pigeon": "The Pigeon, a messenger of the sky, flies with the grace of the stars and the peace of the sun.",
        "Lotus Cat": "The Lotus Cat, a spirit of the waters, wears the flower of the sun and dreams with the colors of the stars.",
        "Pig": "The Pig, a dreamer of the fields, grazes with the patience of the earth and the peace of the stars.",
        "Pepe Samurai": "The Pepe Samurai, a warrior of the night, wears the armor of the stars and wields the katana of the moon.",
        "Shiba Inu": "The Shiba Inu, a spirit of the earth, runs with the speed of the wind and the strength of the stars.",
        "Qilin": "The Qilin, a celestial guardian, walks with the grace of the stars and the power of the sun.",
        "Magentaur": "The Magentaur, a phantom of the earth, moves with the silence of the night and the strength of the stars.",
        "Koi": "The Koi, a spirit of the waters, swims with the grace of the stars and the colors of the sun.",
        "Tengu": "The Tengu, a guardian of the skies, flies with the grace of the stars and the power of the sun.",
        "Maneki Neko": "The Maneki Neko, a spirit of fortune, waves with the grace of the stars and the joy of the sun.",
        "Tyrannosaurus": "The Tyrannosaurus, a king of the ancient world, roars with the power of the stars and the fury of the storm.",
        "Triceratops": "The Triceratops, a guardian of the earth, walks with the strength of the stars and the wisdom of the sun.",
        "Brachiosaurus": "The Brachiosaurus, a titan of the skies, reaches for the stars and touches the sun.",
        "Velociraptor": "The Velociraptor, a phantom of the night, moves with the speed of the stars and the cunning of the moon.",
        "Spinosaurus": "The Spinosaurus, a ruler of the waters, swims with the grace of the stars and the power of the sun.",
        "Mammoth": "The Mammoth, a titan of the ice, walks with the strength of the stars and the wisdom of the sun.",
        "Gozilla": "The Gozilla, a phantom of the deep, moves with the silence of the abyss and the power of the storm.",
        "Bearus": "The Bearus, a titan of the earth, walks with the strength of the stars and the wisdom of the sun.",
        "Unicorn": "The Unicorn, a dream of the sky, gallops with the grace of the stars and the light of the sun.",
        "Phoenix": "The Phoenix, a spirit of the sun, rises from the ashes with the power of the stars and the light of the sun.",
        "Megalodon": "The Megalodon, a phantom of the deep, swims with the silence of the abyss and the power of the storm.",
        "Markhor": "The Markhor, a spirit of the mountains, climbs with the grace of the stars and the strength of the sun.",
        "Anthrop Dragon": "The Anthrop Dragon, a ruler of the skies, flies with the grace of the stars and the power of the sun.",
        "Kitsune": "The Kitsune, a spirit of the night, moves with the cunning of the stars and the mystery of the moon.",
        "Ninja Turtle": "The Ninja Turtle, a warrior of the night, wears the armor of the stars and wields the katana of the moon.",
        "Terror Bird": "The Terror Bird, a phantom of the night, moves with the speed of the stars and the fury of the storm.",
        "Saiga Antelope": "The Saiga Antelope, a spirit of the plains, runs with the speed of the wind and the grace of the stars.",
        "Okapi": "The Okapi, a dreamer of the forests, walks with the grace of the stars and the mystery of the moon.",
        "Platypus": "The Platypus, a spirit of the waters, swims with the grace of the stars and the curiosity of the sun.",
        "Kakapo": "The Kakapo, a dreamer of the night, flies with the silence of the stars and the mystery of the moon.",
        "Manticore": "The Manticore, a phantom of the night, moves with the speed of the stars and the fury of the storm.",
        "Minotaur": "The Minotaur, a titan of the earth, walks with the strength of the stars and the wisdom of the sun.",
        "Chamaleon": "The Chamaleon, a spirit of the earth, changes with the colors of the stars and the mystery of the moon.",
        "Archaeopteryx": "The Archaeopteryx, a dream of the sky, flies with the grace of the stars and the light of the sun.",
        "Llama": "The Llama, a spirit of the mountains, walks with the grace of the stars and the strength of the sun.",
        "Anaconda": "The Anaconda, a phantom of the night, moves with the silence of the stars and the power of the storm.",
        "Alien Monster": "The Alien Monster, a phantom of the night, moves with the speed of the stars and the fury of the storm.",
        "Baphomet": "The Baphomet, a titan of the earth, walks with the strength of the stars and the wisdom of the sun."
    }
    return descriptions.get(name, f"A {name}, a mystical creature of the earth, carries the secrets of the stars.")

def get_conservation_status(name):
    """
    Returns a conservation status for the creature.
    """
    statuses = {
        "Lion": "Vulnerable",
        "Tiger": "Endangered",
        "Jaguar": "Near Threatened",
        "Leopard": "Vulnerable",
        "Panda": "Vulnerable",
        "Polar Bear": "Vulnerable",
        "Brown Bear": "Least Concern",
        "African Elephant": "Vulnerable",
        "Asian Elephant": "Endangered",
        "White Rhino": "Near Threatened",
        "Black Rhino": "Critically Endangered",
        "Giraffe": "Vulnerable",
        "Zebra": "Least Concern",
        "Hippopotamus": "Vulnerable",
        "Seal": "Least Concern",
        "Sea Lion": "Least Concern",
        "Dolphin": "Least Concern",
        "Blue Whale": "Endangered",
        "Humpback Whale": "Least Concern",
        "Great White Shark": "Vulnerable",
        "Whale Shark": "Endangered",
        "Penguin": "Vulnerable",
        "Eagle": "Least Concern",
        "Owl": "Least Concern",
        "Peacock": "Least Concern",
        "Flamingo": "Least Concern",
        "Parrot": "Least Concern",
        "Hummingbird": "Least Concern",
        "Kangaroo": "Least Concern",
        "Koala": "Vulnerable",
        "Wallaby": "Least Concern",
        "Wombat": "Least Concern",
        "King Cobra": "Vulnerable",
        "Python": "Least Concern",
        "Komodo": "Vulnerable",
        "Crocodile": "Least Concern",
        "Nile Crocodile": "Least Concern",
        "Alligator": "Least Concern",
        "Turtle": "Vulnerable",
        "Tortoise": "Vulnerable",
        "Dart Frog": "Least Concern",
        "Green Frog": "Least Concern",
        "Butterfly": "Least Concern",
        "Honeybee": "Least Concern",
        "Ant": "Least Concern",
        "Tarantula": "Least Concern",
        "Beetle": "Least Concern",
        "Octopus": "Least Concern",
        "Squid": "Least Concern",
        "Starfish": "Least Concern",
        "Crab": "Least Concern",
        "Lobster": "Least Concern",
        "Seahorse": "Vulnerable",
        "Clownfish": "Least Concern",
        "Hammerhead Shark": "Endangered",
        "Manta Ray": "Vulnerable",
        "Wild Boar": "Least Concern",
        "Antelope": "Least Concern",
        "Bison": "Near Threatened",
        "Mountain Goat": "Least Concern",
        "Sheep": "Least Concern",
        "Goat": "Least Concern",
        "Camel": "Least Concern",
        "Dromedary": "Least Concern",
        "Wolf": "Least Concern",
        "Fox": "Least Concern",
        "Raccoon": "Least Concern",
        "Ferret": "Least Concern",
        "Otter": "Least Concern",
        "Beaver": "Least Concern",
        "Mole": "Least Concern",
        "Porcupine": "Least Concern",
        "Rabbit": "Least Concern",
        "Squirrel": "Least Concern",
        "Gorilla": "Critically Endangered",
        "Chimpanzee": "Endangered",
        "Orangutan": "Critically Endangered",
        "Baboon": "Least Concern",
        "Gibbon": "Endangered",
        "Bat": "Least Concern",
        "Amazon Dolphin": "Endangered",
        "Walrus": "Vulnerable",
        "Narwhal": "Near Threatened",
        "Orca": "Data Deficient",
        "Maui Dolphin": "Critically Endangered",
        "Monarch Butterfly": "Endangered",
        "Samurai Cat": "Mythical",
        "Husky": "Domesticated",
        "Tentacule": "Mythical",
        "Pigeon": "Least Concern",
        "Lotus Cat": "Mythical",
        "Pig": "Domesticated",
        "Pepe Samurai": "Mythical",
        "Shiba Inu": "Domesticated",
        "Qilin": "Mythical",
        "Magentaur": "Mythical",
        "Koi": "Domesticated",
        "Tengu": "Mythical",
        "Maneki Neko": "Mythical",
        "Tyrannosaurus": "Extinct",
        "Triceratops": "Extinct",
        "Brachiosaurus": "Extinct",
        "Velociraptor": "Extinct",
        "Spinosaurus": "Extinct",
        "Mammoth": "Extinct",
        "Gozilla": "Mythical",
        "Bearus": "Mythical",
        "Unicorn": "Mythical",
        "Phoenix": "Mythical",
        "Megalodon": "Extinct",
        "Markhor": "Near Threatened",
        "Anthrop Dragon": "Mythical",
        "Kitsune": "Mythical",
        "Ninja Turtle": "Mythical",
        "Terror Bird": "Extinct",
        "Saiga Antelope": "Critically Endangered",
        "Okapi": "Endangered",
        "Platypus": "Near Threatened",
        "Kakapo": "Critically Endangered",
        "Manticore": "Mythical",
        "Minotaur": "Mythical",
        "Chamaleon": "Least Concern",
        "Archaeopteryx": "Extinct",
        "Llama": "Domesticated",
        "Anaconda": "Least Concern",
        "Alien Monster": "Mythical",
        "Baphomet": "Mythical"
    }
    return statuses.get(name, "Unknown")

def get_attributes(name):
    """
    Returns a list of attributes for the creature.
    """
    attributes = {
        "Lion": [
            {"trait_type": "Species", "value": "Panthera leo"},
            {"trait_type": "Habitat", "value": "Savanna, Grasslands"},
            {"trait_type": "Rarity", "value": "Common"},
            {"trait_type": "Abilities", "value": "Strength, Roar, Hunting in Prides"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-14 years"},
            {"trait_type": "Speed", "value": "50 mph"}
        ],
        "Tiger": [
            {"trait_type": "Species", "value": "Panthera tigris"},
            {"trait_type": "Habitat", "value": "Forests, Mangroves"},
            {"trait_type": "Rarity", "value": "Rare"},
            {"trait_type": "Abilities", "value": "Stealth, Strength, Swimming"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Jaguar": [
            {"trait_type": "Species", "value": "Panthera onca"},
            {"trait_type": "Habitat", "value": "Rainforests, Swamps"},
            {"trait_type": "Rarity", "value": "Uncommon"},
            {"trait_type": "Abilities", "value": "Stealth, Climbing, Strong Bite"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "12-15 years"},
            {"trait_type": "Speed", "value": "50 mph"}
        ],
        "Leopard": [
            {"trait_type": "Species", "value": "Panthera pardus"},
            {"trait_type": "Habitat", "value": "Savanna, Forests"},
            {"trait_type": "Rarity", "value": "Uncommon"},
            {"trait_type": "Abilities", "value": "Stealth, Climbing, Agility"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "12-17 years"},
            {"trait_type": "Speed", "value": "58 mph"}
        ],
        "Panda": [
            {"trait_type": "Species", "value": "Ailuropoda melanoleuca"},
            {"trait_type": "Habitat", "value": "Bamboo Forests"},
            {"trait_type": "Rarity", "value": "Rare"},
            {"trait_type": "Abilities", "value": "Strength, Climbing, Bamboo Diet"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "20 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Polar Bear": [
            {"trait_type": "Species", "value": "Ursus maritimus"},
            {"trait_type": "Habitat", "value": "Arctic"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Strength, Cold Resistance"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-25 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Brown Bear": [
            {"trait_type": "Species", "value": "Ursus arctos"},
            {"trait_type": "Habitat", "value": "Forests, Mountains"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Strength, Climbing, Fishing"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "African Elephant": [
            {"trait_type": "Species", "value": "Loxodonta africana"},
            {"trait_type": "Habitat", "value": "Savanna, Forests"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Strength, Intelligence, Memory"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "60-70 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Asian Elephant": [
            {"trait_type": "Species", "value": "Elephas maximus"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Strength, Intelligence, Memory"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "60 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "White Rhino": [
            {"trait_type": "Species", "value": "Ceratotherium simum"},
            {"trait_type": "Habitat", "value": "Savanna, Grasslands"},
            {"trait_type": "Rarity", "value": "Near Threatened"},
            {"trait_type": "Abilities", "value": "Strength, Thick Skin, Horn"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "40-50 years"},
            {"trait_type": "Speed", "value": "30 mph"}
        ],
        "Black Rhino": [
            {"trait_type": "Species", "value": "Diceros bicornis"},
            {"trait_type": "Habitat", "value": "Savanna, Grasslands"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Strength, Thick Skin, Horn"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "35-50 years"},
            {"trait_type": "Speed", "value": "34 mph"}
        ],
        "Giraffe": [
            {"trait_type": "Species", "value": "Giraffa camelopardalis"},
            {"trait_type": "Habitat", "value": "Savanna, Grasslands"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Height, Long Neck, Speed"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "25 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Zebra": [
            {"trait_type": "Species", "value": "Equus quagga"},
            {"trait_type": "Habitat", "value": "Savanna, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Speed, Stripes, Herd Behavior"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "25 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Hippopotamus": [
            {"trait_type": "Species", "value": "Hippopotamus amphibius"},
            {"trait_type": "Habitat", "value": "Rivers, Lakes"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Strength, Swimming, Aggression"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "40-50 years"},
            {"trait_type": "Speed", "value": "19 mph"}
        ],
        "Seal": [
            {"trait_type": "Species", "value": "Pinnipedia"},
            {"trait_type": "Habitat", "value": "Oceans, Coasts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Thick Blubber"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Sea Lion": [
            {"trait_type": "Species", "value": "Otariidae"},
            {"trait_type": "Habitat", "value": "Oceans, Coasts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Social Behavior"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Dolphin": [
            {"trait_type": "Species", "value": "Delphinidae"},
            {"trait_type": "Habitat", "value": "Oceans, Coasts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Echolocation, Intelligence"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "40-60 years"},
            {"trait_type": "Speed", "value": "37 mph"}
        ],
        "Blue Whale": [
            {"trait_type": "Species", "value": "Balaenoptera musculus"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Filter Feeding"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "80-90 years"},
            {"trait_type": "Speed", "value": "31 mph"}
        ],
        "Humpback Whale": [
            {"trait_type": "Species", "value": "Megaptera novaeangliae"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Singing, Breaching"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "45-50 years"},
            {"trait_type": "Speed", "value": "16 mph"}
        ],
        "Great White Shark": [
            {"trait_type": "Species", "value": "Carcharodon carcharias"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Hunting, Strong Bite"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "70 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Whale Shark": [
            {"trait_type": "Species", "value": "Rhincodon typus"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Swimming, Filter Feeding, Gentle Nature"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "70-100 years"},
            {"trait_type": "Speed", "value": "3 mph"}
        ],
        "Penguin": [
            {"trait_type": "Species", "value": "Spheniscidae"},
            {"trait_type": "Habitat", "value": "Antarctica, Coasts"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Social Behavior"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "6 mph"}
        ],
        "Eagle": [
            {"trait_type": "Species", "value": "Accipitridae"},
            {"trait_type": "Habitat", "value": "Mountains, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Sharp Vision, Hunting"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "99 mph"}
        ],
        "Owl": [
            {"trait_type": "Species", "value": "Strigiformes"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Night Vision, Silent Flight"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Peacock": [
            {"trait_type": "Species", "value": "Pavo cristatus"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Displaying Feathers, Mating Calls"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Flamingo": [
            {"trait_type": "Species", "value": "Phoenicopteridae"},
            {"trait_type": "Habitat", "value": "Wetlands, Lakes"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Standing on One Leg, Filter Feeding"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Parrot": [
            {"trait_type": "Species", "value": "Psittaciformes"},
            {"trait_type": "Habitat", "value": "Forests, Jungles"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Mimicry, Flying, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "50-80 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Hummingbird": [
            {"trait_type": "Species", "value": "Trochilidae"},
            {"trait_type": "Habitat", "value": "Forests, Gardens"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hovering, Fast Flight, Nectar Feeding"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "3-5 years"},
            {"trait_type": "Speed", "value": "34 mph"}
        ],
        "Kangaroo": [
            {"trait_type": "Species", "value": "Macropodidae"},
            {"trait_type": "Habitat", "value": "Grasslands, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hopping, Carrying Young in Pouch"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "8-12 years"},
            {"trait_type": "Speed", "value": "44 mph"}
        ],
        "Koala": [
            {"trait_type": "Species", "value": "Phascolarctos cinereus"},
            {"trait_type": "Habitat", "value": "Eucalyptus Forests"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Climbing, Sleeping, Eucalyptus Diet"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "13-18 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Wallaby": [
            {"trait_type": "Species", "value": "Macropodidae"},
            {"trait_type": "Habitat", "value": "Grasslands, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hopping, Carrying Young in Pouch"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "9-15 years"},
            {"trait_type": "Speed", "value": "30 mph"}
        ],
        "Wombat": [
            {"trait_type": "Species", "value": "Vombatidae"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Digging, Nocturnal, Strong Jaw"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "King Cobra": [
            {"trait_type": "Species", "value": "Ophiophagus hannah"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Venom, Hood Display, Climbing"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20 years"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Python": [
            {"trait_type": "Species", "value": "Pythonidae"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Constriction, Camouflage, Swimming"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "1 mph"}
        ],
        "Komodo": [
            {"trait_type": "Species", "value": "Varanus komodoensis"},
            {"trait_type": "Habitat", "value": "Islands, Forests"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Venom, Strong Bite, Climbing"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "30 years"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Crocodile": [
            {"trait_type": "Species", "value": "Crocodylidae"},
            {"trait_type": "Habitat", "value": "Rivers, Swamps"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Strong Bite, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "70-100 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Nile Crocodile": [
            {"trait_type": "Species", "value": "Crocodylus niloticus"},
            {"trait_type": "Habitat", "value": "Rivers, Swamps"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Strong Bite, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "70-100 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Alligator": [
            {"trait_type": "Species", "value": "Alligatoridae"},
            {"trait_type": "Habitat", "value": "Rivers, Swamps"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Strong Bite, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "30-50 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Turtle": [
            {"trait_type": "Species", "value": "Testudines"},
            {"trait_type": "Habitat", "value": "Oceans, Rivers"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Long Lifespan, Shell Protection"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "80-150 years"},
            {"trait_type": "Speed", "value": "1 mph"}
        ],
        "Tortoise": [
            {"trait_type": "Species", "value": "Testudinidae"},
            {"trait_type": "Habitat", "value": "Deserts, Grasslands"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Long Lifespan, Shell Protection, Slow Movement"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "80-150 years"},
            {"trait_type": "Speed", "value": "0.2 mph"}
        ],
        "Dart Frog": [
            {"trait_type": "Species", "value": "Dendrobatidae"},
            {"trait_type": "Habitat", "value": "Rainforests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Bright Colors, Poison, Climbing"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Green Frog": [
            {"trait_type": "Species", "value": "Lithobates clamitans"},
            {"trait_type": "Habitat", "value": "Ponds, Lakes"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Jumping, Swimming, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "5-10 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Butterfly": [
            {"trait_type": "Species", "value": "Lepidoptera"},
            {"trait_type": "Habitat", "value": "Forests, Gardens"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Pollination, Camouflage"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "2-4 weeks"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Honeybee": [
            {"trait_type": "Species", "value": "Apis mellifera"},
            {"trait_type": "Habitat", "value": "Forests, Gardens"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Pollination, Honey Production"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "6 weeks"},
            {"trait_type": "Speed", "value": "15 mph"}
        ],
        "Ant": [
            {"trait_type": "Species", "value": "Formicidae"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Strength, Colony Building, Communication"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "1-3 years"},
            {"trait_type": "Speed", "value": "0.03 mph"}
        ],
        "Tarantula": [
            {"trait_type": "Species", "value": "Theraphosidae"},
            {"trait_type": "Habitat", "value": "Forests, Deserts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Venom, Silk Production, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-25 years"},
            {"trait_type": "Speed", "value": "1 mph"}
        ],
        "Beetle": [
            {"trait_type": "Species", "value": "Coleoptera"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Camouflage, Strength"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "1-3 years"},
            {"trait_type": "Speed", "value": "5 mph"}
        ],
        "Octopus": [
            {"trait_type": "Species", "value": "Octopoda"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Camouflage, Intelligence, Ink Defense"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "1-2 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Squid": [
            {"trait_type": "Species", "value": "Teuthida"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Ink Defense, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "1-2 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Starfish": [
            {"trait_type": "Species", "value": "Asteroidea"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Regeneration, Camouflage, Filter Feeding"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "35 years"},
            {"trait_type": "Speed", "value": "0.02 mph"}
        ],
        "Crab": [
            {"trait_type": "Species", "value": "Brachyura"},
            {"trait_type": "Habitat", "value": "Oceans, Coasts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Climbing, Camouflage"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "3-4 years"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Lobster": [
            {"trait_type": "Species", "value": "Nephropidae"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Claw Strength, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "50-100 years"},
            {"trait_type": "Speed", "value": "11 mph"}
        ],
        "Seahorse": [
            {"trait_type": "Species", "value": "Hippocampus"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Camouflage, Male Pregnancy"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "1-5 years"},
            {"trait_type": "Speed", "value": "0.01 mph"}
        ],
        "Clownfish": [
            {"trait_type": "Species", "value": "Amphiprioninae"},
            {"trait_type": "Habitat", "value": "Coral Reefs"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Symbiosis with Anemones"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "6-10 years"},
            {"trait_type": "Speed", "value": "1 mph"}
        ],
        "Hammerhead Shark": [
            {"trait_type": "Species", "value": "Sphyrnidae"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Swimming, Hunting, Wide Vision"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Manta Ray": [
            {"trait_type": "Species", "value": "Mobulidae"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Filter Feeding, Graceful Movement"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "40 years"},
            {"trait_type": "Speed", "value": "22 mph"}
        ],
        "Wild Boar": [
            {"trait_type": "Species", "value": "Sus scrofa"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Strength, Foraging, Aggression"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "10-14 years"},
            {"trait_type": "Speed", "value": "30 mph"}
        ],
        "Antelope": [
            {"trait_type": "Species", "value": "Bovidae"},
            {"trait_type": "Habitat", "value": "Grasslands, Savannas"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Speed, Agility, Herd Behavior"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Bison": [
            {"trait_type": "Species", "value": "Bison bison"},
            {"trait_type": "Habitat", "value": "Grasslands, Forests"},
            {"trait_type": "Rarity", "value": "Near Threatened"},
            {"trait_type": "Abilities", "value": "Strength, Herd Behavior, Foraging"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Mountain Goat": [
            {"trait_type": "Species", "value": "Oreamnos americanus"},
            {"trait_type": "Habitat", "value": "Mountains"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Climbing, Agility, Thick Coat"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "12-15 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Sheep": [
            {"trait_type": "Species", "value": "Ovis aries"},
            {"trait_type": "Habitat", "value": "Grasslands, Farms"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Grazing, Herd Behavior, Wool Production"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "10-12 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Goat": [
            {"trait_type": "Species", "value": "Capra aegagrus hircus"},
            {"trait_type": "Habitat", "value": "Mountains, Farms"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Climbing, Grazing, Milk Production"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "15-18 years"},
            {"trait_type": "Speed", "value": "15 mph"}
        ],
        "Camel": [
            {"trait_type": "Species", "value": "Camelus"},
            {"trait_type": "Habitat", "value": "Deserts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Water Storage, Endurance, Thick Coat"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "40-50 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Dromedary": [
            {"trait_type": "Species", "value": "Camelus dromedarius"},
            {"trait_type": "Habitat", "value": "Deserts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Water Storage, Endurance, Thick Coat"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "40-50 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Wolf": [
            {"trait_type": "Species", "value": "Canis lupus"},
            {"trait_type": "Habitat", "value": "Forests, Tundras"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hunting, Pack Behavior, Howling"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "6-8 years"},
            {"trait_type": "Speed", "value": "37 mph"}
        ],
        "Fox": [
            {"trait_type": "Species", "value": "Vulpes vulpes"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hunting, Camouflage, Cunning"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "3-4 years"},
            {"trait_type": "Speed", "value": "31 mph"}
        ],
        "Raccoon": [
            {"trait_type": "Species", "value": "Procyon lotor"},
            {"trait_type": "Habitat", "value": "Forests, Urban Areas"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Climbing, Foraging, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "2-3 years"},
            {"trait_type": "Speed", "value": "15 mph"}
        ],
        "Ferret": [
            {"trait_type": "Species", "value": "Mustela putorius furo"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hunting, Climbing, Curiosity"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "6-10 years"},
            {"trait_type": "Speed", "value": "15 mph"}
        ],
        "Otter": [
            {"trait_type": "Species", "value": "Lutrinae"},
            {"trait_type": "Habitat", "value": "Rivers, Lakes"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Playfulness"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "7 mph"}
        ],
        "Beaver": [
            {"trait_type": "Species", "value": "Castor"},
            {"trait_type": "Habitat", "value": "Rivers, Lakes"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Dam Building, Swimming, Gnawing"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "5 mph"}
        ],
        "Mole": [
            {"trait_type": "Species", "value": "Talpidae"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Digging, Camouflage, Foraging"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "3-6 years"},
            {"trait_type": "Speed", "value": "4 mph"}
        ],
        "Porcupine": [
            {"trait_type": "Species", "value": "Erethizontidae"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Quill Defense, Climbing, Foraging"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "5-7 years"},
            {"trait_type": "Speed", "value": "2 mph"}
        ],
        "Rabbit": [
            {"trait_type": "Species", "value": "Oryctolagus cuniculus"},
            {"trait_type": "Habitat", "value": "Forests, Grasslands"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Hopping, Digging, Foraging"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "9-12 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Squirrel": [
            {"trait_type": "Species", "value": "Sciuridae"},
            {"trait_type": "Habitat", "value": "Forests, Urban Areas"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Climbing, Foraging, Hoarding"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "5-10 years"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Gorilla": [
            {"trait_type": "Species", "value": "Gorilla"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Strength, Intelligence, Social Behavior"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "35-40 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Chimpanzee": [
            {"trait_type": "Species", "value": "Pan troglodytes"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Intelligence, Tool Use, Social Behavior"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "40-50 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Orangutan": [
            {"trait_type": "Species", "value": "Pongo"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Intelligence, Climbing, Tool Use"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "35-45 years"},
            {"trait_type": "Speed", "value": "6 mph"}
        ],
        "Baboon": [
            {"trait_type": "Species", "value": "Papio"},
            {"trait_type": "Habitat", "value": "Savannas, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Strength, Social Behavior, Foraging"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "30 mph"}
        ],
        "Gibbon": [
            {"trait_type": "Species", "value": "Hylobatidae"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Swinging, Vocalization, Social Behavior"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "25-30 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Bat": [
            {"trait_type": "Species", "value": "Chiroptera"},
            {"trait_type": "Habitat", "value": "Caves, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Echolocation, Nocturnal"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Amazon Dolphin": [
            {"trait_type": "Species", "value": "Inia geoffrensis"},
            {"trait_type": "Habitat", "value": "Rivers"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Swimming, Echolocation, Intelligence"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "30 years"},
            {"trait_type": "Speed", "value": "18 mph"}
        ],
        "Walrus": [
            {"trait_type": "Species", "value": "Odobenus rosmarus"},
            {"trait_type": "Habitat", "value": "Arctic"},
            {"trait_type": "Rarity", "value": "Vulnerable"},
            {"trait_type": "Abilities", "value": "Swimming, Diving, Tusk Defense"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "40 years"},
            {"trait_type": "Speed", "value": "21 mph"}
        ],
        "Narwhal": [
            {"trait_type": "Species", "value": "Monodon monoceros"},
            {"trait_type": "Habitat", "value": "Arctic"},
            {"trait_type": "Rarity", "value": "Near Threatened"},
            {"trait_type": "Abilities", "value": "Swimming, Tusk Defense, Echolocation"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "50 years"},
            {"trait_type": "Speed", "value": "17 mph"}
        ],
        "Orca": [
            {"trait_type": "Species", "value": "Orcinus orca"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Data Deficient"},
            {"trait_type": "Abilities", "value": "Swimming, Hunting, Intelligence"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "50-80 years"},
            {"trait_type": "Speed", "value": "34 mph"}
        ],
        "Maui Dolphin": [
            {"trait_type": "Species", "value": "Cephalorhynchus hectori maui"},
            {"trait_type": "Habitat", "value": "Oceans"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Swimming, Echolocation, Intelligence"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20 years"},
            {"trait_type": "Speed", "value": "18 mph"}
        ],
        "Monarch Butterfly": [
            {"trait_type": "Species", "value": "Danaus plexippus"},
            {"trait_type": "Habitat", "value": "Forests, Gardens"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Migration, Pollination, Camouflage"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "2-6 weeks"},
            {"trait_type": "Speed", "value": "12 mph"}
        ],
        "Samurai Cat": [
            {"trait_type": "Species", "value": "Felis catus"},
            {"trait_type": "Habitat", "value": "Feudal Japan"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Swordsmanship, Stealth, Agility"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "12-15 years"},
            {"trait_type": "Speed", "value": "30 mph"}
        ],
        "Husky": [
            {"trait_type": "Species", "value": "Canis lupus familiaris"},
            {"trait_type": "Habitat", "value": "Arctic"},
            {"trait_type": "Rarity", "value": "Domesticated"},
            {"trait_type": "Abilities", "value": "Strength, Endurance, Loyalty"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "12-15 years"},
            {"trait_type": "Speed", "value": "28 mph"}
        ],
        "Tentacule": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Deep Ocean"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Tentacle Manipulation, Camouflage, Intelligence"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Pigeon": [
            {"trait_type": "Species", "value": "Columba livia"},
            {"trait_type": "Habitat", "value": "Urban Areas, Forests"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Flying, Navigation, Communication"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "6 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Lotus Cat": [
            {"trait_type": "Species", "value": "Felis catus"},
            {"trait_type": "Habitat", "value": "Temples, Gardens"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Calm Aura, Healing, Meditation"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Pig": [
            {"trait_type": "Species", "value": "Sus scrofa domesticus"},
            {"trait_type": "Habitat", "value": "Farms, Forests"},
            {"trait_type": "Rarity", "value": "Domesticated"},
            {"trait_type": "Abilities", "value": "Foraging, Intelligence, Social Behavior"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "11 mph"}
        ],
        "Pepe Samurai": [
            {"trait_type": "Species", "value": "Anura"},
            {"trait_type": "Habitat", "value": "Feudal Japan"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Swordsmanship, Jumping, Camouflage"},
            {"trait_type": "Diet", "value": "Insectivore"},
            {"trait_type": "Lifespan", "value": "10-12 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Shiba Inu": [
            {"trait_type": "Species", "value": "Canis lupus familiaris"},
            {"trait_type": "Habitat", "value": "Urban Areas, Farms"},
            {"trait_type": "Rarity", "value": "Domesticated"},
            {"trait_type": "Abilities", "value": "Loyalty, Agility, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "12-15 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Qilin": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Ancient China"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Divine Protection, Fire Breathing, Flight"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "1000 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Magentaur": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Mythical Realms"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Magnetic Manipulation, Strength, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Koi": [
            {"trait_type": "Species", "value": "Cyprinus rubrofuscus"},
            {"trait_type": "Habitat", "value": "Ponds, Gardens"},
            {"trait_type": "Rarity", "value": "Domesticated"},
            {"trait_type": "Abilities", "value": "Swimming, Graceful Movement, Longevity"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "25-35 years"},
            {"trait_type": "Speed", "value": "5 mph"}
        ],
        "Tengu": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Mountains, Forests"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Flight, Martial Arts, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Maneki Neko": [
            {"trait_type": "Species", "value": "Felis catus"},
            {"trait_type": "Habitat", "value": "Temples, Homes"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Good Luck, Wealth Attraction, Healing"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Tyrannosaurus": [
            {"trait_type": "Species", "value": "Tyrannosaurus rex"},
            {"trait_type": "Habitat", "value": "Ancient Forests"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Strength, Hunting, Roaring"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "28-30 years"},
            {"trait_type": "Speed", "value": "25 mph"}
        ],
        "Triceratops": [
            {"trait_type": "Species", "value": "Triceratops horridus"},
            {"trait_type": "Habitat", "value": "Ancient Forests"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Horn Defense, Herd Behavior, Grazing"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "30 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Brachiosaurus": [
            {"trait_type": "Species", "value": "Brachiosaurus altithorax"},
            {"trait_type": "Habitat", "value": "Ancient Forests"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Height, Long Neck, Grazing"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "100 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Velociraptor": [
            {"trait_type": "Species", "value": "Velociraptor mongoliensis"},
            {"trait_type": "Habitat", "value": "Ancient Deserts"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Speed, Hunting, Pack Behavior"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Spinosaurus": [
            {"trait_type": "Species", "value": "Spinosaurus aegyptiacus"},
            {"trait_type": "Habitat", "value": "Ancient Rivers"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Swimming, Hunting, Sail Defense"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "25 years"},
            {"trait_type": "Speed", "value": "18 mph"}
        ],
        "Mammoth": [
            {"trait_type": "Species", "value": "Mammuthus primigenius"},
            {"trait_type": "Habitat", "value": "Tundras"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Strength, Tusk Defense, Herd Behavior"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "60 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Gozilla": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Oceans, Cities"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Strength, Atomic Breath, Regeneration"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Bearus": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Mythical Forests"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Strength, Roar, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Unicorn": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Enchanted Forests"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Healing, Flight, Magic"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "1000 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Phoenix": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Volcanoes, Skies"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Rebirth, Fire Manipulation, Flight"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "1000 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Megalodon": [
            {"trait_type": "Species", "value": "Carcharocles megalodon"},
            {"trait_type": "Habitat", "value": "Ancient Oceans"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Strength, Hunting, Speed"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "20-40 years"},
            {"trait_type": "Speed", "value": "20 mph"}
        ],
        "Markhor": [
            {"trait_type": "Species", "value": "Capra falconeri"},
            {"trait_type": "Habitat", "value": "Mountains"},
            {"trait_type": "Rarity", "value": "Near Threatened"},
            {"trait_type": "Abilities", "value": "Climbing, Horn Defense, Grazing"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "12-13 years"},
            {"trait_type": "Speed", "value": "10 mph"}
        ],
        "Anthrop Dragon": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Mythical Realms"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Flight, Fire Breathing, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Kitsune": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Forests, Temples"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Shape-shifting, Intelligence, Magic"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "1000 years"},
            {"trait_type": "Speed", "value": "60 mph"}
        ],
        "Ninja Turtle": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Urban Areas, Sewers"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Martial Arts, Stealth, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Terror Bird": [
            {"trait_type": "Species", "value": "Phorusrhacidae"},
            {"trait_type": "Habitat", "value": "Ancient Grasslands"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Speed, Hunting, Beak Strength"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-15 years"},
            {"trait_type": "Speed", "value": "40 mph"}
        ],
        "Saiga Antelope": [
            {"trait_type": "Species", "value": "Saiga tatarica"},
            {"trait_type": "Habitat", "value": "Grasslands, Deserts"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Speed, Herd Behavior, Grazing"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "6-10 years"},
            {"trait_type": "Speed", "value": "50 mph"}
        ],
        "Okapi": [
            {"trait_type": "Species", "value": "Okapia johnstoni"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Endangered"},
            {"trait_type": "Abilities", "value": "Camouflage, Grazing, Speed"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "20-30 years"},
            {"trait_type": "Speed", "value": "37 mph"}
        ],
        "Platypus": [
            {"trait_type": "Species", "value": "Ornithorhynchus anatinus"},
            {"trait_type": "Habitat", "value": "Rivers, Lakes"},
            {"trait_type": "Rarity", "value": "Near Threatened"},
            {"trait_type": "Abilities", "value": "Swimming, Venom, Egg-laying"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-17 years"},
            {"trait_type": "Speed", "value": "6 mph"}
        ],
        "Kakapo": [
            {"trait_type": "Species", "value": "Strigops habroptilus"},
            {"trait_type": "Habitat", "value": "Forests"},
            {"trait_type": "Rarity", "value": "Critically Endangered"},
            {"trait_type": "Abilities", "value": "Flightless, Nocturnal, Camouflage"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "60 years"},
            {"trait_type": "Speed", "value": "2 mph"}
        ],
        "Manticore": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Deserts, Forests"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Venomous Tail, Strength, Flight"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Minotaur": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Labyrinths"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Strength, Horns, Intelligence"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Chamaleon": [
            {"trait_type": "Species", "value": "Chamaeleonidae"},
            {"trait_type": "Habitat", "value": "Forests, Deserts"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Camouflage, Long Tongue, Climbing"},
            {"trait_type": "Diet", "value": "Insectivore"},
            {"trait_type": "Lifespan", "value": "5-10 years"},
            {"trait_type": "Speed", "value": "0.5 mph"}
        ],
        "Archaeopteryx": [
            {"trait_type": "Species", "value": "Archaeopteryx lithographica"},
            {"trait_type": "Habitat", "value": "Ancient Forests"},
            {"trait_type": "Rarity", "value": "Extinct"},
            {"trait_type": "Abilities", "value": "Flight, Feathers, Climbing"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Llama": [
            {"trait_type": "Species", "value": "Lama glama"},
            {"trait_type": "Habitat", "value": "Mountains, Farms"},
            {"trait_type": "Rarity", "value": "Domesticated"},
            {"trait_type": "Abilities", "value": "Strength, Grazing, Wool Production"},
            {"trait_type": "Diet", "value": "Herbivore"},
            {"trait_type": "Lifespan", "value": "15-20 years"},
            {"trait_type": "Speed", "value": "35 mph"}
        ],
        "Anaconda": [
            {"trait_type": "Species", "value": "Eunectes murinus"},
            {"trait_type": "Habitat", "value": "Rivers, Swamps"},
            {"trait_type": "Rarity", "value": "Least Concern"},
            {"trait_type": "Abilities", "value": "Constriction, Swimming, Camouflage"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "10-12 years"},
            {"trait_type": "Speed", "value": "5 mph"}
        ],
        "Alien Monster": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Space, Planets"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Strength, Intelligence, Flight"},
            {"trait_type": "Diet", "value": "Carnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ],
        "Baphomet": [
            {"trait_type": "Species", "value": "Mythical"},
            {"trait_type": "Habitat", "value": "Mythical Realms"},
            {"trait_type": "Rarity", "value": "Mythical"},
            {"trait_type": "Abilities", "value": "Magic, Intelligence, Strength"},
            {"trait_type": "Diet", "value": "Omnivore"},
            {"trait_type": "Lifespan", "value": "Unknown"},
            {"trait_type": "Speed", "value": "Unknown"}
        ]
    }
    return attributes.get(name, [
        {"trait_type": "Species", "value": "Unknown"},
        {"trait_type": "Habitat", "value": "Unknown"},
        {"trait_type": "Rarity", "value": "Unknown"},
        {"trait_type": "Abilities", "value": "Unknown"},
        {"trait_type": "Diet", "value": "Unknown"},
        {"trait_type": "Lifespan", "value": "Unknown"},
        {"trait_type": "Speed", "value": "Unknown"}
    ])

# Example usage
if __name__ == "__main__":
    # Base URL for the IPFS gateway
    base_url = "https://ipfs.io/ipfs/bafybeid4lexivwa6qb3cyt4cxirwsniwcfxzphnqczyuhq3ek5j7rvewxa"

    # List of filenames
    filenames = [
        "001.lion.webp",
        "002.tiger.webp",
        "003.jaguar.webp",
        "004.leopard.webp",
        "005.panda.webp",
        "006.polar_bear.webp",
        "007.brown_bear.webp",
        "008.african_elephant.webp",
        "009.asian_elephant.webp",
        "010.white_rhino.webp",
        "011.black_rhino.webp",
        "012.giraffe.webp",
        "013.zebra.webp",
        "014.hippopotamus.webp",
        "015.seal.webp",
        "016.sea_lion.webp",
        "017.dolphin.webp",
        "018.blue_whale.webp",
        "019.humpback_whale.webp",
        "020.great_white_shark.webp",
        "021.whale_shark.webp",
        "022.penguin.webp",
        "023.eagle.webp",
        "024.owl.webp",
        "025.peacock.webp",
        "026.flamingo.webp",
        "027.parrot.webp",
        "028.hummingbird.webp",
        "029.kangaroo.webp",
        "030.koala.webp",
        "031.wallaby.webp",
        "032.wombat.webp",
        "033.king_cobra.webp",
        "034.python.webp",
        "035.komodo.webp",
        "036.crocodile.webp",
        "037.nile_crocodile.webp",
        "038.alligator.webp",
        "039.turtle.webp",
        "040.tortoise.webp",
        "041.dart_frog.webp",
        "042.green_frog.webp",
        "043.butterfly.webp",
        "044.honeybee.webp",
        "045.ant.webp",
        "046.tarantula.webp",
        "047.beetle.webp",
        "048.octopus.webp",
        "049.squid.webp",
        "050.starfish.webp",
        "051.crab.webp",
        "052.lobster.webp",
        "053.seahorse.webp",
        "054.clownfish.webp",
        "055.hammerhead_shark.webp",
        "056.manta_ray.webp",
        "057.wild_boar.webp",
        "058.antelope.webp",
        "059.bison.webp",
        "060.mountain_goat.webp",
        "061.sheep.webp",
        "062.goat.webp",
        "063.camel.webp",
        "064.dromedary.webp",
        "065.wolf.webp",
        "066.fox.webp",
        "067.raccoon.webp",
        "068.ferret.webp",
        "069.otter.webp",
        "070.beaver.webp",
        "071.mole.webp",
        "072.porcupine.webp",
        "073.rabbit.webp",
        "074.squirrel.webp",
        "075.gorilla.webp",
        "076.chimpanzee.webp",
        "077.orangutan.webp",
        "078.baboon.webp",
        "079.gibbon.webp",
        "080.bat.webp",
        "081.amazon_dolphin.webp",
        "082.dolphin.webp",
        "083.walrus.webp",
        "084.narwhal.webp",
        "085.orca.webp",
        "086.maui_dolphin.webp",
        "087.monarch_butterfly.webp",
        "088.samurai_cat.webp",
        "089.husky.webp",
        "090.tentacule.webp",
        "091.pigeon.webp",
        "092.lotus_cat.webp",
        "093.pig.webp",
        "094.pepe_samurai.webp",
        "095.shiba_inu.webp",
        "096.qilin.webp",
        "097.magentaur.webp",
        "098.koi.webp",
        "099.tengu.webp",
        "100.maneki_neko.webp",
        "101.tyrannosaurus.webp",
        "102.triceratops.webp",
        "103.brachiosaurus.webp",
        "104.velociraptor.webp",
        "105.spinosaurus.webp",
        "106.mammoth.webp",
        "107.gozilla.webp",
        "108.bearus.webp",
        "109.unicorn.webp",
        "110.phoenix.webp",
        "111.megalodon.webp",
        "112.markhor.webp",
        "113.anthrop_dragon.webp",
        "114.kitsune.webp",
        "115.ninja_turtle.webp",
        "116.terror_bird.webp",
        "117.saiga_antelope.webp",
        "118.okapi.webp",
        "119.platypus.webp",
        "120.kakapo.webp",
        "121.manticore.webp",
        "122.minotaur.webp",
        "123.chamaleon.webp",
        "124.archaeopteryx.webp",
        "125.llama.webp",
        "126.anaconda.webp",
        "127.alien_monster.webp",
        "128.baphomet.webp"
    ]

    # Generate metadata
    generate_mystical_metadata(filenames, base_url)