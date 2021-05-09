from mycroft import MycroftSkill, intent_file_handler


class Showmap(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('showmap.intent')
    def handle_showmap(self, message):
        self.speak_dialog('showmap')


def create_skill():
    return Showmap()

