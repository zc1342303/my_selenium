from PIL import Image
import pytesseract


class Cap():
    def __init__(self):
        pass

    def run(self):
        captcha = Image.open("C:/Users/YDBJ0440/Desktop/pict")
        result = pytesseract.image_to_string(captcha)
        print(result)


def run():
    cap = Cap()
    cap.run()


if __name__ == '__main__':
    run()
