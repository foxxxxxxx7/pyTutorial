from PIL import Image


def image_to_ascii(image_path, output_width=100):
    """Convert an image to ASCII art."""
    # ASCII characters used to represent pixel brightness levels
    ascii_chars = "@%#*+=-:. "
    # Open and resize the image
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    width, height = img.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio * 0.55)  # Adjust for terminal aspect ratio
    img = img.resize((output_width, new_height))

    # Convert image to grayscale
    img = img.convert("L")

    # Convert pixels to ASCII
    pixels = img.getdata()
    ascii_str = "".join([ascii_chars[pixel // 25] for pixel in pixels])

    # Format ASCII string into lines
    ascii_art = "\n".join(
        [ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)]
    )
    return ascii_art


def main():
    """Main function for the ASCII Art Generator."""
    print("Welcome to the ASCII Art Generator!")
    image_path = input("Enter the path to the image file: ").strip()
    try:
        output_width = int(input("Enter the desired output width (default 100): ").strip() or 100)
    except ValueError:
        print("Invalid width, using default of 100.")
        output_width = 100

    ascii_art = image_to_ascii(image_path, output_width)
    if ascii_art:
        print("\nYour ASCII Art:\n")
        print(ascii_art)
        save = input("\nWould you like to save this art to a text file? (yes/no): ").strip().lower()
        if save == "yes":
            with open("ascii_art.txt", "w") as file:
                file.write(ascii_art)
            print("ASCII art saved to 'ascii_art.txt'.")


if __name__ == "__main__":
    main()
