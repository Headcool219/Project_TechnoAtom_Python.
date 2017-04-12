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


from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

def get_dataset():
    with open("dataset.yml", 'rt', encoding='utf-8') as input:
        package = load(input, Loader=Loader)
        dataset = package.get('dataset')
        if not isinstance(dataset, list):
            raise ValueError('wrong format')
        yield from dataset
dataset = get_dataset()
Test = list()
for i in dataset:
    val = Task(i[0], i[2], i[1])
    Test.append(val)
Xeh = Roadmap(Test)
for i in Xeh.filter('in_progress'):
  print(i)


class WSGIApplication:

    def __init__(self, environment, start_response):
        print('Get request')
        self.environment = environment
        self.start_response = start_response
        self.headers = [
            ('Content-type', 'text/plain; charset=utf-8')
        ]

    def __iter__(self):
        List_of_Tasks = list()
        print('Wait for response')
        for data in dataset:
            task = Task(data[0], data[2], data[1])
            if task.remaining < datetime.timedelta(days=3) and task.state == 'in_progress':
                List_of_Tasks += task.title + '\n'
        yield List_of_Tasks.encode('utf-8')