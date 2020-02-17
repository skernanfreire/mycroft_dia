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
        self.log.info("padatious status intent was triggered")
        machine_number = message.data.get('number')
        self.speak_dialog('machine.status',{'number': machine_number})
        self.set_context('number', machine_number)

    @intent_file_handler('machine.maintenance.intent')
    def handle_machine_maintenance_intent(self, message):
        """ This is a Padatious intent handler.
        It is triggered using a list of sample phrases."""
        self.log.info("padatious maintenance intent was triggered")
        machine_number = message.data.get('number')
        self.speak_dialog('machine.maintenance',{'number': machine_number})
        self.set_context('number', machine_number)
        

    '''@intent_handler(IntentBuilder('MaintenanceIntent').optionally('MachineKeyword').require('MaintenanceKeyword').require('number'))
    def handle_maintenance_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.log.info("adapt maintenance intent was triggered")
        machine_number = message.data.get('number')
        self.log.info(machine_number)
        self.speak_dialog("machine.maintenance",{'number': machine_number})
        self.set_context('number', machine_number)

    @intent_handler(IntentBuilder('AdaptStatusIntent').optionally('MachineKeyword').require('MachineStatusKeyword').require('number'))
    def handle_adapt_status_intent(self, message):
        """ This is an Adapt intent handler, it is triggered by a keyword."""
        self.log.info("adapt status intent was triggered")
        machine_number = message.data.get('number')
        self.log.info(machine_number)
        self.speak_dialog("machine.status",{'number': machine_number})
        self.set_context('number', machine_number)'''
      
        

    def stop(self):
        pass

def create_skill():
    return DiamondAssistant()

