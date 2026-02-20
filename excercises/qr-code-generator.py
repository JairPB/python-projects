# Import the qrcode library for generating QR codes
import qrcode


# Define a custom QR code generator class
class MyQR:
    def __init__(self, size: int, padding: int):
        """
        Initialize the MyQR object with QR code configuration.

        Args:
            size (int): The size of each box in the QR code (in pixels)
            padding (int): The border/padding around the QR code (in boxes)
        """
        # Create a QRCode instance with the specified box size and border padding
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        """
        Create and save a QR code image to a file.

        Args:
            file_name (str): The name of the output file (e.g., "qr_sample.png")
            fg (str): Foreground color - the color of the QR code pattern (e.g., "black")
            bg (str): Background color - the color behind the QR code (e.g., "white")
        """
        # Get the text input from the user (this will be encoded in the QR code)
        # Note: This is currently hardcoded for testing purposes
        user_input: str = "www.website.com"
        # Uncomment the line below to enable interactive user input:
        # user_input: str = input("Enter text: ")

        try:
            # Add the user input data to the QR code
            self.qr.add_data(user_input)

            # Generate the QR code image with the specified colors
            # fill_color is the foreground (the pattern), back_color is the background
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)

            # Save the generated QR code image to the specified file path
            qr_image.save("excercises/" + file_name)

            # Display a success message to the user
            print(f"QR code successfully saved as {file_name}")

        except Exception as e:
            # Catch any errors that occur during QR code generation or file saving
            # and display an error message to the user
            print(f"An error occurred: {e}")


def main():
    """
    Main function that orchestrates the QR code generation process.
    """
    # Create an instance of MyQR with:
    # - size=30: each QR code box will be 30 pixels
    # - padding=2: there will be a 2-box border around the QR code
    myqr = MyQR(size=30, padding=2)

    # Generate and save the QR code with:
    # - file name: "qr_sample.png"
    # - foreground color: black (the QR code pattern)
    # - background color: white (the background)
    myqr.create_qr("qr_sample.png", "black", "white")


# Entry point check: only run main() if this file is executed directly
# (not if it's imported as a module in another script)
if __name__ == "__main__":
    main()
