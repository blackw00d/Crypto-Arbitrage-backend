from requests import get


class Telegram:

    base = 'https://api.telegram.org/bot'

    def __init__(self, token):
        self.url = "{0}{1}".format(self.base, token)

    def send_message_to_user(self, user, text):
        response = get('{0}/sendMessage?chat_id={1}&text={2}&parse_mode=HTML'.format(self.url, user, text))
        return response.json()
