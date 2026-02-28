from PIL import Image
import random

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Simple encryption using key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save("encrypted_image.png")
    print("Image Encrypted Successfully!")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse encryption
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save("decrypted_image.png")
    print("Image Decrypted Successfully!")

# ---- Main Program ----
image_path = input("Enter image path: ")
key = int(input("Enter encryption key (number): "))

choice = input("Type 'e' to encrypt or 'd' to decrypt: ")

if choice == 'e':
    encrypt_image(image_path, key)
elif choice == 'd':
    decrypt_image(image_path, key)
else:
    print("Invalid Choice!")