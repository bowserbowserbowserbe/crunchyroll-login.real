# Stub semplificato. Per funzionamento reale, serve sostituire con la vera libreria crunchyroll.py
# dal repo: https://github.com/crunchy-labs/crunchyroll.py

import asyncio

class User:
    def __init__(self, name):
        self.name = name

class Session:
    def __init__(self, user):
        self.user = user

class Crunchyroll:
    @staticmethod
    async def login(email, password):
        # Simulazione accesso reale: inserire qui chiamate alle API vere
        if email and password:
            return Session(User(email.split("@")[0]))
        raise Exception("Login fallito")
