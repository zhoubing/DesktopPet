import os
import random


class Config:
    ROOT_DIR = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'resources')
    ACTION_DISTRIBUTION = [
        ['1', '2', '3'],
        ['4', '5', '6', '7', '8', '9', '10', '11'],
        ['12', '13', '14'],
        ['15', '16', '17'],
        ['18', '19'],
        ['20', '21'],
        ['22'],
        ['23', '24', '25'],
        ['26',  '27', '28', '29'],
        ['30', '31', '32', '33'],
        ['34', '35', '36', '37'],
        ['38', '39', '40', '41'],
        ['42', '43', '44', '45', '46']
    ]
    PET_ACTIONS_MAP = dict()
    for name in ['pikachu', 'blackcat', 'whitecat', 'fox']:
        PET_ACTIONS_MAP[name] = ACTION_DISTRIBUTION
    PET_ACTIONS_MAP['bingdwendwen'] = [
        [str(i) for i in range(1, 41, 8)],
        [str(i) for i in range(41, 56)],
        [str(i) for i in range(56, 91)],
    ]
    BAIDU_KEYS = random.choice([
        ['25419425', 'fct6UMiQMLsp53MqXzp7AbKQ', 'p3wU9nPnfR7iBz2kM25sikN2ms0y84T3'],
        ['24941009', '2c5AnnNaQKOIcTrLDTuY41vv', 'HOYo7BunbFtt88Z0ALFZcFSQ4ZVyIgiZ'],
        ['11403041', 'swB03t9EbokK03htGsg0PKYe', 'XX20l47se2tSGmet8NihkHQLIjTIHUyy'],
    ])
