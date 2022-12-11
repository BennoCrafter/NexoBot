import configs
from NexoActions import engine_speak
from datetime import datetime
import languageSaver

module = __import__("NexoActions")


class Intend:
    now = datetime.now()
    pattern = []
    action_def = None
    action_param = ''

    def __init__(self, pattern, action_def):
        self.action_def = action_def
        self.pattern = pattern.split('|')

    def __str__(self):
        return str(self.pattern) + ":::" + self.action_def

    def match(self, voice):
        for p in self.pattern:
            if p in voice:
                return True
        return False

    def execute(self, voice):
        if configs.developer_mode:
            current_time = self.now.strftime("%H:%M:%S")
            if self.action_def == "speak":
                print(self.action_def + " - " + self.action_param + " - ", current_time)
            else:
                print(self.action_def + " -", current_time)
        if self.action_def == 'speak':
            engine_speak(self.action_param)
        else:
            func = getattr(module, self.action_def)
            func(voice)

# MADE BY BENNO #
