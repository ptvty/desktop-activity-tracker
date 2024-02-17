class Activity:
    def __init__(self, project_name):
        self.keyboard = 0
        self.mouse = 0
        self.history = []
        self.project_name = project_name

    def tick(self):
        record = [self.keyboard, self.mouse]
        self.history.append(record)
        self.keyboard = 0
        self.mouse = 0
        if len(self.history) > 10:
            self.history.pop(0)

    def activity(self, timeframe = 10):
        active = 0
        for record in self.history:
            if record[0] + record[1] > 2 and timeframe > 0:
                active += 1
            timeframe -= 1
        return active

