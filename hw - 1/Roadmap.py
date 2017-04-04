import datetime
class Roadmap:

    def __init__(self, tasks=list()):
        self.tasks = tasks

    today = property()
    @today.getter
    def today(self):
        return [value for value in self.tasks if value.estimate == datetime.date.today()]

    def filter(self, state):
        if type(state) != type(''):
            raise TypeError('Incorrect type of state.')
        if (state != 'in_progress') and (state != 'ready'):
            raise ValueError('Incorrect state')
        return [value for value in self.tasks if value.state == state]
    


