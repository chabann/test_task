import io
import sys
from tasks_software_engineer import Megatrader
import pytest


test_cases_task2 = [
    {
        'input': ['2 2 8000', '1 alfa-05 100.2 2', '2 alfa-05 101.5 5', '2 gazprom-17 100.0 2', '\n'],
        'output': [135, '2 alfa-05 101.5 5', '2 gazprom-17 100.0 2']
    },
    {
        'input': ['0 100 1000', '\n'],
        'output': [0]
    },
    {
        'input': ['10 100 0', '1 alfa-05 100.2 10', '\n'],
        'output': [0]
    },
    {
        'input': ['10 100 1000', '\n'],
        'output': [0]
    },
    {
        'input': ['10 100 1000', '1 alfa-05 100.2 10', '\n'],
        'output': [0]
    },
    {
        'input': ['10 100 10000', '1 alfa-05 98.2 10', '\n'],
        'output': [570, '1 alfa-05 98.2 10']
    },
    {
        'input': [
            '10 2 2000000', '1 name-1-0 116.6 3', '2 name-2-0 95.6 4', '2 name-2-1 95.8 20', '3 name-3-0 115.8 17', 
            '4 name-4-0 120.0 1', '5 name-5-0 116.8 6', '5 name-5-1 98.3 15', '6 name-6-0 106.5 1', '7 name-7-0 111.2 12', 
            '7 name-7-1 101.9 13', '8 name-8-0 93.3 17', '9 name-9-0 106.1 10', '9 name-9-1 113.0 6', '10 name-10-0 111.6 5', '\n'
        ],
        'output': [
            4573.0, '2 name-2-0 95.6 4', '2 name-2-1 95.8 20', '5 name-5-1 98.3 15', '7 name-7-1 101.9 13', '8 name-8-0 93.3 17'
        ]
    }
]


@pytest.fixture(params=test_cases_task2)
def bonds(request):
    return request.param


def test_task_example(bonds, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('\n'.join([bond for bond in bonds['input']])))

    megatrader = Megatrader()
    megatrader()

    out, err = capsys.readouterr()
    assert err == '', 'not empty errors'

    result = []
    out_list = out.split('\n')[:-1]
    for i in range(len(out_list)):
        if i == 0:
            result.append(float(out_list[i]))
        else:
            result.append(out_list[i])

    assert result == bonds['output'], f"test case {bonds['input']}"

    