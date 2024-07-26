import requests
import time, random, string
from bs4 import BeautifulSoup

save = lambda src: open('/sdcard/src.htm', 'w').write(str(src))
randomize = lambda length=20: ''.join(random.choices(string.ascii_letters+str(string.digits), k=int(length)))

class TMail:
    session = requests.session()
    host = 'https://generator.email/'

    def __init__(self):
        source = BeautifulSoup(self.session.get(self.host).text, 'html.parser')
        self.mail = source.find('span', {'id': 'email_ch_text'}).get_text()
        self.db = []

    def messages(self, mail: str=None):
        get = self.session.get('https://generator.email/'+ self.mail if mail is None else mail)
        source = BeautifulSoup(get.text, 'html.parser')
        table = source.find('div', {'id': 'email-table'})
        
        try: 
            inbox_url = [url['href'] for url in table.find_all('a', href=lambda href: self.mail.split('@')[0] in href)]
            if len(inbox_url) == 0:
                inbox = self.inbox_details(source.find('div', {'id': 'email-table'}))

                if inbox is not None:
                    if self.check_db(inbox) is True: pass
                    else: self.db.append({randomize(): inbox})
                else:
                    pass
            else:
                for url in inbox_url:
                    source = BeautifulSoup(self.session.get(self.host + url).text, 'html.parser')
                    inbox = self.inbox_details(source.find('div', {'id': 'email-table'}))

                    if inbox is not None: 
                        if self.check_db(inbox) is True: pass
                        else: self.db.append({randomize(): inbox})
                    else:
                        pass

            #inbox_id = [[key for key, v in dc.items()][0] for dc in self.db]
        except AttributeError: # attribute
            inbox = self.inbox_details(source.find('div', {'id': 'email-table'}))

            if inbox is not None:
                if self.check_db(inbox) is True: pass
                else: self.db.append({randomize(): inbox})
            else:
                pass

        inbox_id = [[key for key, v in dc.items()][0] for dc in self.db]
        return inbox_id

    def inbox_details(self, source):
        try:
            info = source.find('div', {'class': True}).find_all('div')
            # inbox details
            sender_mail = info[0].get_text()
            subject = info[1].get_text()
            time = info[2].get_text()
            messages = source.find('div', {'dir': 'auto'}).get_text()
        except (IndexError, AttributeError): # index
            try:
                info = source.find('div', {'id': 'message'})
                # inbox details
                sender_mail = info.find_all('span')[3].get_text().split(' ')[0]
                subject = info.find('h1').get_text()
                time = info.find_all('span')[7].get_text().split('\n')[0]
                messages = source.find('div', {'dir': 'auto'}).get_text()
            except AttributeError:
                return None

        return {'subject': subject, 'from': sender_mail, 'received': time, 'messages': messages}

    def inbox(self, keys: str):
        for msg in self.db:
            if keys in msg: return msg[keys]
        
        return {}

    def check_db(self, target):
        for d in self.db:
            for value in d.values():
                if value == target:
                    return True
        return False

