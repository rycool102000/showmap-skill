import re
import sys
import json
from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler, intent_file_handler
from mycroft.messagebus.message import Message
from mycroft.skills.core import resting_screen_handler


class Showmap(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('showmap.intent')
    def handle_showmap(self, message):
        self.speak_dialog('showmap')
        self.gui.clear()
        self.enclosure.display_manager.remove_active()
        self.gui.show_image("https://www.binghamton.edu/clt/utc/img/new_bartle_map_small.jpg", "School Map", "School Map")

def create_skill():
    return Showmap()

