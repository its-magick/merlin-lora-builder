import os
import subprocess
import sys


def download_file(url, dest):
    """
    Downloads a file from the given URL if it doesn't already exist.
    """
    if not os.path.exists(dest):
        print(f"Downloading {url} to {dest}...")
        subprocess.run(["wget", url, "-O", dest], check=True, timeout=None)
    else:
        print(f"File {dest} already exists. Skipping download.")

def setup_weight_files():
    """
    Download necessary weight files.
    """
    print("Setting up weight files...")
    # Define file URLs and destinations
    files = {
        #"add-details.safetensors": "https://huggingface.co/Shakker-Labs/FLUX.1-dev-LoRA-add-details/resolve/main/FLUX-dev-lora-add_details.safetensors",
        #"scripts/Canopus-LoRA-Flux-FaceRealism.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/Canopus-LoRA-Flux-FaceRealism.safetensors",
        #"scripts/Canopus-LoRA-Flux-UltraRealism.safetensors": "https://huggingface.co/its-magick/merlin-flux-ultra-realism-v2/resolve/main/Canopus-LoRA-Flux-UltraRealism.safetensors",
        #"scripts/merlin-logos.safetensors": "https://huggingface.co/its-magick/merlin-logos/resolve/main/merlin-logos.safetensors",
        #"scripts/merlin-mobile-app.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/mobile-ui.safetensors",
        #"scripts/merlin-food.safetensors": "https://huggingface.co/its-magick/merlin-food/resolve/main/lora.safetensors",
        #"scripts/merlin-cake.safetensors": "https://huggingface.co/its-magick/merlin-cake/resolve/main/lora.safetensors",
        #"scripts/merlin-snlogo.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/sn-logo.safetensors",
        #"scripts/merlin-headshots.safetensors": "https://huggingface.co/its-magick/merlin-headshots/resolve/main/lora.safetensors",
        #"scripts/merlin-office.safetensors": "https://huggingface.co/its-magick/merlin-office/resolve/main/lora.safetensors",
        #"scripts/merlin-ironman.safetensors": "https://huggingface.co/miike-ai/merlin-ironman/resolve/main/lora.safetensors",
        #"scripts/merlin-aquariums.safetensors": "https://huggingface.co/its-magick/merlin-aquariums/resolve/main/lora.safetensors",
        #"scripts/merlin-upgrader.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/aidmaHyperrealism-FLUX-v0.3.safetensors",
        #"scripts/merlin-turbo-detailer.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/Flux.1_Turbo_Detailer.safetensors",
        "scripts/shards/merlin-hands.safetensors": "https://huggingface.co/its-magick/merlin-test-loras/resolve/main/Detailed_Hands-000001.safetensors",
    }

    for filename, url in files.items():
        download_file(url, filename)

if __name__ == "__main__":
    print("Starting setup process...")
    setup_weight_files()
