import qrcode


class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        # user_input: str = input("Enter text: ")
        user_input: str = "www.website.com"

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save("excercises/" + file_name)
            print(f"QR code successfully saved as {file_name}")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr("qr_sample.png", "black", "white")


if __name__ == "__main__":
    main()
