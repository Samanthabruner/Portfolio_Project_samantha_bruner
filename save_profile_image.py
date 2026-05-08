#!/usr/bin/env python
"""
Helper script to save profile image to static/images/profile.jpg
Converts image to JPEG if needed.
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Project paths
PROJECT_ROOT = Path(__file__).parent
IMAGES_DIR = PROJECT_ROOT / "static" / "images"
OUTPUT_FILE = IMAGES_DIR / "profile.jpg"

# Create images directory if it doesn't exist
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def save_profile_image(input_path):
    """Convert and save image to profile.jpg."""
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        return False
    
    try:
        # Open and convert image
        img = Image.open(input_path)
        
        # Convert to RGB if needed (for PNG with alpha, etc.)
        if img.mode in ("RGBA", "LA", "P"):
            rgb_img = Image.new("RGB", img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = rgb_img
        
        # Save as JPEG
        img.save(OUTPUT_FILE, "JPEG", quality=85, optimize=True)
        print(f"✓ Profile image saved: {OUTPUT_FILE}")
        print(f"  Size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
        return True
    
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Use provided path
        input_file = sys.argv[1]
    else:
        # Try default Download location
        default_path = Path.home() / "Downloads" / "profile.jpg"
        if default_path.exists():
            input_file = default_path
            print(f"Using: {input_file}")
        else:
            print("Usage: python save_profile_image.py <image_file_path>")
            print(f"\nSearching for profile.jpg in {Path.home() / 'Downloads'}...")
            sys.exit(1)
    
    success = save_profile_image(input_file)
    sys.exit(0 if success else 1)
