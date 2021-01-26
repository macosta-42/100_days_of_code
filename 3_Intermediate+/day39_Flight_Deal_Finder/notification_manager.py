import re
import fbchat
from fbchat import Client
from fbchat.models import *

EMAIL = # YOUR FB MESSENGER EMAIL HERE
PASS = # YOUR FB MESSENGER PASSWORD HERE
GROUP_ID = # THE THREAD ID OF THE GROUP HERE

fbchat._util.USER_AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')


class NotificationManager:

    def __init__(self):
        self.client = Client(EMAIL, PASS)

    def send_notification(self, msg):
        sent = self.client.send(Message(text=msg), thread_id=GROUP_ID, thread_type=ThreadType.USER)
        if sent:
            print("Message sent successfully")
