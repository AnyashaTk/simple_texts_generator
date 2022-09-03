import argparse
import os
import pickle

parser = argparse.ArgumentParser()

parser.add_argument('--input-dir',
                    default='stdin',
                    help='Путь к директории с датой. (default: stdin)')
parser.add_argument('--model',
                    default='./',
                    help='Путь сохраняения модели. (default: ./)')

args = parser.parse_args()


class TextModel:
    def __init__(self):
        w2v = 'w2v obj'

    def load_weights(self, weights):
        pass

    def fit(self, train_data):
        pass

    def generate(self, length=10, prefix=''):
        pass


model = TextModel()

# Train process


# Saving model
with open(os.path.join(args.model, 'model.pkl'), 'wb') as save_path:
    pickle.dump(model, save_path)
