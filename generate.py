import argparse
from train import TextModel
import pickle
import os

parser = argparse.ArgumentParser()

parser.add_argument('--model',
                    default='./model.pkl',
                    help='Путь к весам модели. (default: ./model.pkl)')
parser.add_argument('--prefix',
                    default='',
                    help='Начало последовательности. (optional, default: "")')
parser.add_argument('--length',
                    default=10,
                    help='Длина генерируемой последовательности. '
                         '(default: 10)')

args = parser.parse_args()

with open(os.path.join(args.model), 'rb') as load_path:
    model = TextModel()
    model.load_weights(pickle.load(load_path))

print(model.generate(args.length, args.prefix))
