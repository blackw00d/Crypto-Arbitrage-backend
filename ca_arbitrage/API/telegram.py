from requests import get, post


class Telegram:
    base = 'https://api.telegram.org/bot'

    def __init__(self, token):
        self.url = "{0}{1}".format(self.base, token)

    def send_message_to_user(self, user, text):
        response = get('{0}/sendMessage?chat_id={1}&text={2}&parse_mode=HTML'.format(self.url, user, text))
        return response.json()

    def send_photo_to_user(self, user, text, img):
        files = {'photo': open(img, 'rb')}
        response = post('{0}/sendPhoto?chat_id={1}&caption={2}&parse_mode=HTML'.format(self.url, user, text),
                        files=files)
        return response.json()
