import os
import shutil
import json
import yaml  # Install with `pip install pyyaml`

def build_nft_structure(metadata_dir, creatures_dir, output_dir="src/content/nft"):
    """
    Builds the NFT folder structure with images and metadata markdown files (with frontmatter).

    Args:
        metadata_dir (str): Path to the folder containing JSON metadata files.
        creatures_dir (str): Path to the folder containing creature images.
        output_dir (str): Path to the output folder (default: "src/content/nft").
    """
    # Create the parent folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all metadata files
    for filename in os.listdir(metadata_dir):
        if filename.endswith(".json"):
            # Extract the serial number (e.g., "001" from "001.json")
            serial_number = filename.split(".")[0]

            # Create the subfolder for this creature
            subfolder = os.path.join(output_dir, serial_number)
            os.makedirs(subfolder, exist_ok=True)

            # Find the main image file that starts with the serial number
            image_filename = None
            for img_file in os.listdir(creatures_dir):
                if img_file.startswith(serial_number) and img_file.endswith(".webp") and '-' not in img_file:
                    image_filename = img_file
                    break

            # Find the art image file that starts with the serial number and has a hyphen
            art_filename = None
            for img_file in os.listdir(creatures_dir):
                if img_file.startswith(serial_number) and img_file.endswith(".webp") and '-' in img_file:
                    art_filename = img_file
                    break

            if image_filename:
                # Copy the main image file to the subfolder
                image_src = os.path.join(creatures_dir, image_filename)
                image_dest = os.path.join(subfolder, image_filename)
                shutil.copy(image_src, image_dest)
            else:
                print(f"Warning: Main image file for {serial_number} not found. Skipping.")

            if art_filename:
                # Copy the art image file to the subfolder
                art_src = os.path.join(creatures_dir, art_filename)
                art_dest = os.path.join(subfolder, art_filename)
                shutil.copy(art_src, art_dest)
            else:
                print(f"Warning: Art image file for {serial_number} not found. Skipping.")

            # Load the metadata from the JSON file
            metadata_path = os.path.join(metadata_dir, filename)
            with open(metadata_path, "r") as file:
                metadata = json.load(file)

            # Prepare the frontmatter in YAML format
            frontmatter = {
                "name": metadata["name"],
                "description": metadata["description"],
                "image": image_filename if image_filename else "N/A",
                "art": art_filename if art_filename else "N/A",
                "external_url": metadata["image"],
                "artist": metadata["artist"],
                "collection": metadata["collection"],
                "conservation_status": metadata["conservation_status"],
                "attributes": metadata["attributes"]
            }

            # Generate the markdown content with frontmatter
            markdown_content = f"""---
{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}
---

# {metadata['name']}

**Description**: {metadata['description']}

**Image**: [{image_filename}](./{image_filename}) if image_filename else "N/A"

**Art**: [{art_filename}](./{art_filename}) if art_filename else "N/A"

**External URL**: [{metadata['image']}]({metadata['image']})

**Artist**: {metadata['artist']}

**Collection**: {metadata['collection']}

**Conservation Status**: {metadata['conservation_status']}

## Attributes
- **Species**: {metadata['attributes'][0]['value']}
- **Habitat**: {metadata['attributes'][1]['value']}
- **Rarity**: {metadata['attributes'][2]['value']}
- **Abilities**: {metadata['attributes'][3]['value']}
- **Diet**: {metadata['attributes'][4]['value']}
- **Lifespan**: {metadata['attributes'][5]['value']}
- **Speed**: {metadata['attributes'][6]['value']}
"""

            # Save the markdown file
            markdown_path = os.path.join(subfolder, "metadata.md")
            with open(markdown_path, "w") as file:
                file.write(markdown_content)

            print(f"Created folder for {metadata['name']} ({serial_number})")

# Example usage
if __name__ == "__main__":
    # Paths to the metadata and creatures folders
    metadata_dir = "metadata"
    creatures_dir = "creatures"

    # Build the NFT folder structure
    build_nft_structure(metadata_dir, creatures_dir)