import unittest
from src.task import check_gas_supply

class TestGasSupply(unittest.TestCase):
    def test_full_connectivity(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [
            ['Львів', 'Стрий'],
            ['Долина', 'Львів'],
            ['Сховище_1', 'Сховище_2'],
            ['Сховище_2', 'Долина']
        ]
        self.assertEqual(check_gas_supply(cities, storages, pipelines), [])

    def test_partial_connectivity(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1']
        pipelines = [
            ['Сховище_1', 'Львів'],
            ['Львів', 'Стрий']
        ]
        self.assertEqual(check_gas_supply(cities, storages, pipelines), [['Сховище_1', ['Долина']]])

    def test_no_connectivity(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = []
        self.assertEqual(check_gas_supply(cities, storages, pipelines), [['Сховище_1', ['Львів', 'Стрий']]])

