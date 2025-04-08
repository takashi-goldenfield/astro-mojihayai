import json

# List of unknown creature names
unknown_creatures = [
    "088.samurai_cat", "089.husky", "090.tentacule", "091.pepe", "092.pepe_samurai",
    "093.mammoth", "094.sabertooth", "095.terror_bird", "096.kakapo", "097.dodo",
    "098.tasmanian_devil", "099.platypus", "100.echidna", "101.quokka", "102.kiwi",
    "103.emu", "104.ostrich", "105.cassowary", "106.albatross", "107.frigatebird",
    "108.peregrine_falcon", "109.harpy_eagle", "110.vulture", "111.hyena", "112.jackal",
    "113.wolverine", "114.badger", "115.skunk", "116.weasel", "117.arctic_fox",
    "118.snow_leopard", "119.ibex", "120.markhor", "121.gryphon", "122.phoenix",
    "123.dragon", "124.unicorn", "125.kraken", "126.yeti", "127.chimera", "128.sphinx"
]

# Function to assign custom attributes based on creature name
def get_custom_attributes(name):
    if "samurai_cat" in name:
        return {
            "species": "Mythical Feline",
            "habitat": "Feudal Japan",
            "abilities": "Swordplay, Stealth, Agility",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "45 mph",
            "rarity": "Legendary"
        }
    elif "husky" in name:
        return {
            "species": "Dog",
            "habitat": "Arctic",
            "abilities": "Strength, Endurance, Loyalty",
            "diet": "Omnivore",
            "lifespan": "12 years",
            "speed": "20 mph",
            "rarity": "Rare"
        }
    elif "tentacule" in name:
        return {
            "species": "Deep-Sea Creature",
            "habitat": "Ocean Depths",
            "abilities": "Tentacle Manipulation, Camouflage",
            "diet": "Carnivore",
            "lifespan": "Unknown",
            "speed": "10 mph",
            "rarity": "Epic"
        }
    elif "pepe" in name:
        return {
            "species": "Meme Frog",
            "habitat": "Internet",
            "abilities": "Virality, Adaptability",
            "diet": "Omnivore",
            "lifespan": "Eternal",
            "speed": "5 mph",
            "rarity": "Legendary"
        }
    elif "mammoth" in name:
        return {
            "species": "Prehistoric Elephant",
            "habitat": "Tundra",
            "abilities": "Strength, Cold Resistance",
            "diet": "Herbivore",
            "lifespan": "60 years",
            "speed": "20 mph",
            "rarity": "Epic"
        }
    elif "sabertooth" in name:
        return {
            "species": "Prehistoric Feline",
            "habitat": "Ice Age",
            "abilities": "Strength, Stealth, Sharp Fangs",
            "diet": "Carnivore",
            "lifespan": "20 years",
            "speed": "40 mph",
            "rarity": "Legendary"
        }
    elif "terror_bird" in name:
        return {
            "species": "Prehistoric Bird",
            "habitat": "Grasslands",
            "abilities": "Speed, Predation",
            "diet": "Carnivore",
            "lifespan": "30 years",
            "speed": "50 mph",
            "rarity": "Epic"
        }
    elif "kakapo" in name:
        return {
            "species": "Parrot",
            "habitat": "New Zealand",
            "abilities": "Climbing, Camouflage",
            "diet": "Herbivore",
            "lifespan": "60 years",
            "speed": "5 mph",
            "rarity": "Rare"
        }
    elif "dodo" in name:
        return {
            "species": "Flightless Bird",
            "habitat": "Mauritius",
            "abilities": "Curiosity, Adaptability",
            "diet": "Herbivore",
            "lifespan": "20 years",
            "speed": "10 mph",
            "rarity": "Legendary"
        }
    elif "tasmanian_devil" in name:
        return {
            "species": "Marsupial",
            "habitat": "Tasmania",
            "abilities": "Strength, Ferocity",
            "diet": "Carnivore",
            "lifespan": "5 years",
            "speed": "15 mph",
            "rarity": "Rare"
        }
    elif "platypus" in name:
        return {
            "species": "Egg-Laying Mammal",
            "habitat": "Australia",
            "abilities": "Swimming, Electroreception",
            "diet": "Carnivore",
            "lifespan": "10 years",
            "speed": "5 mph",
            "rarity": "Rare"
        }
    elif "echidna" in name:
        return {
            "species": "Spiny Anteater",
            "habitat": "Australia",
            "abilities": "Burrowing, Defense",
            "diet": "Insectivore",
            "lifespan": "15 years",
            "speed": "5 mph",
            "rarity": "Rare"
        }
    elif "quokka" in name:
        return {
            "species": "Marsupial",
            "habitat": "Australia",
            "abilities": "Friendliness, Adaptability",
            "diet": "Herbivore",
            "lifespan": "10 years",
            "speed": "10 mph",
            "rarity": "Rare"
        }
    elif "kiwi" in name:
        return {
            "species": "Flightless Bird",
            "habitat": "New Zealand",
            "abilities": "Nocturnal, Foraging",
            "diet": "Omnivore",
            "lifespan": "30 years",
            "speed": "10 mph",
            "rarity": "Rare"
        }
    elif "emu" in name:
        return {
            "species": "Flightless Bird",
            "habitat": "Australia",
            "abilities": "Speed, Endurance",
            "diet": "Omnivore",
            "lifespan": "20 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "ostrich" in name:
        return {
            "species": "Flightless Bird",
            "habitat": "Savannah",
            "abilities": "Speed, Strength",
            "diet": "Omnivore",
            "lifespan": "40 years",
            "speed": "45 mph",
            "rarity": "Rare"
        }
    elif "cassowary" in name:
        return {
            "species": "Flightless Bird",
            "habitat": "Rainforest",
            "abilities": "Strength, Agility",
            "diet": "Omnivore",
            "lifespan": "40 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "albatross" in name:
        return {
            "species": "Seabird",
            "habitat": "Oceans",
            "abilities": "Flight, Endurance",
            "diet": "Carnivore",
            "lifespan": "50 years",
            "speed": "60 mph",
            "rarity": "Rare"
        }
    elif "frigatebird" in name:
        return {
            "species": "Seabird",
            "habitat": "Tropical Oceans",
            "abilities": "Flight, Speed",
            "diet": "Carnivore",
            "lifespan": "30 years",
            "speed": "50 mph",
            "rarity": "Rare"
        }
    elif "peregrine_falcon" in name:
        return {
            "species": "Bird of Prey",
            "habitat": "Worldwide",
            "abilities": "Speed, Precision",
            "diet": "Carnivore",
            "lifespan": "15 years",
            "speed": "240 mph",
            "rarity": "Epic"
        }
    elif "harpy_eagle" in name:
        return {
            "species": "Bird of Prey",
            "habitat": "Rainforest",
            "abilities": "Strength, Agility",
            "diet": "Carnivore",
            "lifespan": "30 years",
            "speed": "50 mph",
            "rarity": "Epic"
        }
    elif "vulture" in name:
        return {
            "species": "Scavenger Bird",
            "habitat": "Desert/Savannah",
            "abilities": "Scavenging, Flight",
            "diet": "Carnivore",
            "lifespan": "20 years",
            "speed": "30 mph",
            "rarity": "Common"
        }
    elif "hyena" in name:
        return {
            "species": "Mammal",
            "habitat": "Savannah",
            "abilities": "Scavenging, Strength",
            "diet": "Carnivore",
            "lifespan": "20 years",
            "speed": "40 mph",
            "rarity": "Rare"
        }
    elif "jackal" in name:
        return {
            "species": "Mammal",
            "habitat": "Savannah",
            "abilities": "Scavenging, Agility",
            "diet": "Carnivore",
            "lifespan": "10 years",
            "speed": "35 mph",
            "rarity": "Common"
        }
    elif "wolverine" in name:
        return {
            "species": "Mammal",
            "habitat": "Tundra",
            "abilities": "Strength, Ferocity",
            "diet": "Carnivore",
            "lifespan": "10 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "badger" in name:
        return {
            "species": "Mammal",
            "habitat": "Forest",
            "abilities": "Burrowing, Defense",
            "diet": "Omnivore",
            "lifespan": "10 years",
            "speed": "20 mph",
            "rarity": "Common"
        }
    elif "skunk" in name:
        return {
            "species": "Mammal",
            "habitat": "Forest",
            "abilities": "Defensive Spray, Foraging",
            "diet": "Omnivore",
            "lifespan": "5 years",
            "speed": "10 mph",
            "rarity": "Common"
        }
    elif "weasel" in name:
        return {
            "species": "Mammal",
            "habitat": "Forest",
            "abilities": "Agility, Stealth",
            "diet": "Carnivore",
            "lifespan": "5 years",
            "speed": "15 mph",
            "rarity": "Common"
        }
    elif "arctic_fox" in name:
        return {
            "species": "Mammal",
            "habitat": "Arctic",
            "abilities": "Camouflage, Adaptability",
            "diet": "Carnivore",
            "lifespan": "5 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "snow_leopard" in name:
        return {
            "species": "Feline",
            "habitat": "Mountains",
            "abilities": "Stealth, Agility",
            "diet": "Carnivore",
            "lifespan": "15 years",
            "speed": "40 mph",
            "rarity": "Epic"
        }
    elif "ibex" in name:
        return {
            "species": "Goat",
            "habitat": "Mountains",
            "abilities": "Climbing, Agility",
            "diet": "Herbivore",
            "lifespan": "15 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "markhor" in name:
        return {
            "species": "Goat",
            "habitat": "Mountains",
            "abilities": "Climbing, Strength",
            "diet": "Herbivore",
            "lifespan": "15 years",
            "speed": "30 mph",
            "rarity": "Rare"
        }
    elif "gryphon" in name:
        return {
            "species": "Mythical",
            "habitat": "Fantasy Realm",
            "abilities": "Flight, Strength",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "60 mph",
            "rarity": "Legendary"
        }
    elif "phoenix" in name:
        return {
            "species": "Mythical",
            "habitat": "Fantasy Realm",
            "abilities": "Rebirth, Fire Manipulation",
            "diet": "Unknown",
            "lifespan": "Eternal",
            "speed": "50 mph",
            "rarity": "Legendary"
        }
    elif "dragon" in name:
        return {
            "species": "Mythical",
            "habitat": "Fantasy Realm",
            "abilities": "Fire Breath, Flight, Immense Strength",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "200 mph",
            "rarity": "Legendary"
        }
    elif "unicorn" in name:
        return {
            "species": "Mythical",
            "habitat": "Fantasy Realm",
            "abilities": "Healing, Magic",
            "diet": "Herbivore",
            "lifespan": "Eternal",
            "speed": "50 mph",
            "rarity": "Legendary"
        }
    elif "kraken" in name:
        return {
            "species": "Mythical",
            "habitat": "Ocean Depths",
            "abilities": "Tentacle Manipulation, Destruction",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "30 mph",
            "rarity": "Legendary"
        }
    elif "yeti" in name:
        return {
            "species": "Mythical",
            "habitat": "Mountains",
            "abilities": "Strength, Stealth",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "40 mph",
            "rarity": "Legendary"
        }
    elif "chimera" in name:
        return {
            "species": "Mythical",
            "habitat": "Fantasy Realm",
            "abilities": "Multiple Abilities, Ferocity",
            "diet": "Carnivore",
            "lifespan": "Eternal",
            "speed": "50 mph",
            "rarity": "Legendary"
        }
    elif "sphinx" in name:
        return {
            "species": "Mythical",
            "habitat": "Desert",
            "abilities": "Wisdom, Riddles",
            "diet": "Unknown",
            "lifespan": "Eternal",
            "speed": "30 mph",
            "rarity": "Legendary"
        }
    else:
        return None

# Function to generate metadata
def generate_metadata(token_id, name):
    creature_name = name.split(".")[1].replace("_", " ").title()
    attributes = get_custom_attributes(name)
    
    if attributes is None:
        return None  # Skip if no attributes are found
    
    metadata = {
        "tokenId": token_id,
        "name": creature_name,
        "description": f"A futuristic {creature_name.lower()}, embodying the spirit of its species in a digital world.",
        "image": f"https://ipfs.io/ipfs/bafybeid4lexivwa6qb3cyt4cxirwsniwcfxzphnqczyuhq3ek5j7rvewxa/{name}.webp",
        "attributes": [
            { "trait_type": "species", "value": attributes["species"] },
            { "trait_type": "habitat", "value": attributes["habitat"] },
            { "trait_type": "abilities", "value": attributes["abilities"] },
            { "trait_type": "diet", "value": attributes["diet"] },
            { "trait_type": "lifespan", "value": attributes["lifespan"] },
            { "trait_type": "speed", "value": attributes["speed"] },
            { "trait_type": "rarity", "value": attributes["rarity"] }
        ],
        "external_url": "",
        "artist": "MythicCreator",
        "collection": "Mythical Beasts",
        "conservation_status": "Not Applicable"
    }
    return metadata

# Generate metadata for unknown creatures
metadata_list = []
for i, name in enumerate(unknown_creatures, start=88):
    metadata = generate_metadata(i, name)
    if metadata:  # Only include creatures with attributes
        metadata_list.append(metadata)

# Save metadata to a JSON file
with open("nft_metadata_unknown.json", "w") as f:
    json.dump(metadata_list, f, indent=4)

print("Metadata for unknown creatures generated successfully! Check 'nft_metadata_unknown.json'.")