import logging
import os
import base64
import dearpygui.dearpygui as dpg
import hashlib

from chat_client import ChatClient
from generic_callback import GenericCallback
from ciphered_gui import CipheredGUI
from cryptography.fernet import Fernet




class FernetGUI(CipheredGUI):

    #GUI pour un chat client sécurisé non altéré.

    def run_chat(self, sender, app_data)->None:
        # callback used by the connection windows to start a chat session
        host = dpg.get_value("connection_host")
        port = int(dpg.get_value("connection_port"))
        name = dpg.get_value("connection_name")
        #Récupation du password
        password=dpg.get_value("connection_password")
        self._log.info(f"Connecting {name}@{host}:{port}")

        self._callback = GenericCallback()

        self._client = ChatClient(host, port)
        self._client.start(self._callback)
        self._client.register(name)

        dpg.hide_item("connection_windows")
        dpg.show_item("chat_windows")
        dpg.set_value("screen", "Connecting")

        #dérivation de la clé
        self.key = hashlib.sha256(password.endoce()).digest()
        self.key = base64.b64encode(self.key)

    def encrypt(self, message):
        #chiffrement du message envoyé
        f = Fernet(self.key)
        return f.encrypt(bytes(message,'utf-8'))
    
    def decrypt(self, message):
        #dechiffrage du message envoyé
        message=base64.b64decode(message['data'])
        f = Fernet(self.key)
        #retourne le message en clair
        return f.decrypt(message).decode()

 

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # instanciate the class, create context and related stuff, run the main loop
    client = FernetGUI()
    client.create()
    client.loop()