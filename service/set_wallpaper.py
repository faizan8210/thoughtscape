import ctypes
import os
from pathlib import Path

def set_wallpaper(image_path):
    if os.name != "nt":
        raise RuntimeError("This works only on Windows.")

    path = Path(image_path).resolve()

    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {path}")

    result = ctypes.windll.user32.SystemParametersInfoW(
        20,              # SPI_SETDESKWALLPAPER
        0,
        str(path),
        0x01 | 0x02      # Update settings + notify Windows
    )

    if not result:
        raise RuntimeError("Failed to set wallpaper.")

       