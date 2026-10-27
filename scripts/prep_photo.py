import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
if len(sys.argv) < 2:
    raise SystemExit("Usage: python scripts/prep_photo.py path/to/photo.jpg")
source = Path(sys.argv[1])
if not source.exists():
    raise SystemExit(f"Photo not found: {source}")
im = Image.open(source).convert("RGB")
im.thumbnail((900, 900))
im = ImageOps.grayscale(im)
im = ImageOps.autocontrast(im, cutoff=2)
im = ImageEnhance.Contrast(im).enhance(1.35)
im = im.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
im.save("source-prepped.png")
print("Created source-prepped.png")
