from mycroft import MycroftSkill, intent_file_handler


class DiamondAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.diamond.intent')
    def handle_assistant_diamond(self, message):
        self.speak_dialog('assistant.diamond')


def create_skill():
    return DiamondAssistant()

