import datetime


class Task:

    def __init__(self, title , estimate, state="in progress"):

        if type(title) != type(''):
            raise TypeError('Incorrect type of title. ')
        if type(estimate) != type(datetime.date.today()):
            raise TypeError('Incorrect type of estimate. ')
        if type(state) != type(''):
            raise TypeError('Incorrect type of state.')
        if (state != 'in_progress') and (state != 'ready'):
            raise ValueError('Incorrect state')

        self.title = title
        self.estimate = estimate
        self.state = state

    remaning = property()
    @remaning.getter
    def remaining(self):
        if self.state != 'in_progress':
            return 0
        else:
            return datetime.timedelta(self.estimate - datetime.date.today)

    is_failed = property()
    @is_failed.getter
    def is_failed(self):
        if (self.estimate < datetime.date.today()) and (self.state == 'in_progress '):
            return True
        else:
            return False


    def ready(self):
        self.state = "ready"





