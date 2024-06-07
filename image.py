from PIL import Image

def encrypt_decrypt(image_path, key, mode):
  """Encrypts or decrypts an image using pixel-wise XOR with a key."""
  image = Image.open(image_path)
  pixels = image.load()
  width, height = image.size

  new_image = Image.new(image.mode, image.size)
  new_pixels = new_image.load()

  for i in range(width):
    for j in range(height):
      red, green, blue = pixels[i, j]
      if mode == 'encrypt':
        new_red = red ^ key
        new_green = green ^ key
        new_blue = blue ^ key
      else:
        new_red = red ^ key
        new_green = green ^ key
        new_blue = blue ^ key
      new_pixels[i, j] = (new_red, new_green, new_blue)

  new_image.save(f"{image_path[:-4]}_{mode}.png")

def main():
  while True:
    mode = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
    if mode == 'q':
      break
    elif mode not in ('e', 'd'):
      print("Invalid input. Please enter 'e', 'd', or 'q'.")
      continue

    image_path = input("Enter the image path: ")
    try:
      key = int(input("Enter the encryption/decryption key (integer): "))
    except ValueError:
      print("Invalid key. Please enter an integer.")
      continue

    encrypt_decrypt(image_path, key, mode)
    print(f"Image {mode}crypted successfully!")

if __name__ == "__main__":
  main()
