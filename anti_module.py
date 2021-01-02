from python3_anticaptcha import ImageToTextTask


class Anticaptcha:
    def __init__(self):
        pass

    def run(self):
        # Enter the key to the AntiCaptcha service from your account. Anticaptcha service key.
        ANTICAPTCHA_KEY = ""
        # Link to captcha image.
        image_link = "http://58.215.18.81:32314/dwz_springmvc/passport/getVerifyCode"
        # Get string for solve captcha, and some other info.
        print("a")
        user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY). \
            captcha_handler(captcha_link=image_link)

        print(user_answer)


def test():
    demo = Anticaptcha()
    demo.run()


if __name__ == '__main__':
    test()
