from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class DiamondAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    '''def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')'''

    @intent_file_handler('machine.status.intent')
    def handle_machine_status_intent(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        machine_number = message.data.get('number')
        self.speak_dialog('machine.status',{'number': machine_number})

    @intent_handler(IntentBuilder('ThankYouIntent').require('ThankYouKeyword'))
    def handle_thank_you_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.speak_dialog("welcome")

    def stop(self):
        pass

def create_skill():
    return DiamondAssistant()

