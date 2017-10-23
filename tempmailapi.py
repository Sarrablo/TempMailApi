import hashlib
import requests

class TempMailApi:

    def __init__(self, token_api):
        self.token_api = token_api

    def make_request(self, url):
        response = requests.get(url,
                headers={
                    "X-Mashape-Key": self.token_api,
                    "Accept": "application/json"
                    }
                )
        return response

    def get_domains(self):
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/domains/"
        return self.make_request(url)

    def get_emails(self, email):
        md5 = hashlib.md5(email.encode('utf-8')).hexdigest()
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/mail/id/%s/"%(md5)
        return self.make_request(url)

    def get_message_attachments(self, message_id):
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/attachments/id/%s/"%(message_id)
        return self.make_request(url)

    def get_one_message(self, message_id):
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/one_mail/id/%s/"%(message_id)
        return self.make_request(url)

    def get_source_message(self, message_id):
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/source/id/%s/"%(message_id)
        return self.make_request(url)

    def delete_message(self, message_id):
        url = "https://privatix-temp-mail-v1.p.mashape.com/request/delete/id/%s/"%(message_id)
        return self.make_request(url)

