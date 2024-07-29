# work in progress

import sqlite3
import os


class MessageStorage:
    # It will be a history of messages
    def __init__(self):
        os.makedirs("data/", exist_ok=True)
        self.storage = sqlite3.connect("data/messages.db")
