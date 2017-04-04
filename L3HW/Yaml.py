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
