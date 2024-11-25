import qrcode


def generate_qr_code():
    """Generate and save a QR code based on user input."""
    print("Welcome to the QR Code Generator!")
    data = input("Enter the text or URL to encode: ").strip()
    if not data:
        print("You must enter some text or a URL.")
        return

    filename = input("Enter a name for the QR code image file (without extension): ").strip()
    if not filename:
        print("Filename cannot be empty. Using default name 'qr_code'.")
        filename = "qr_code"

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{filename}.png")
    print(f"QR code saved as {filename}.png!")


def main():
    """Main program loop."""
    while True:
        generate_qr_code()
        retry = input("\nWould you like to generate another QR code? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Thanks for using the QR Code Generator! Goodbye!")
            break


if __name__ == "__main__":
    main()
