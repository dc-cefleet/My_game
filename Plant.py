class Plant():
    def __init__(self):
        self.day_actions = []
    
    def run_day(self):
        for i in self.day_actions:
            i()