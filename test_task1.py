import io
import sys
from tasks_software_engineer import CountShares
import pytest

test_cases_task1 = [
    {
        'input': [4, 1.5, 3, 6, 1.5],
        'output': [0.125, 0.250, 0.500, 0.125]
    },
    {
        'input': [5, 1.5, 3, 6, 1.5, 1],
        'output': [0.115, 0.231, 0.462, 0.115, 0.077]
    },
    {
        'input': [0],
        'output': []
    },
    {
        'input': [20, 634.1, 672.4, 2.3, 51.3, 640.2, 790.3, 738.6, 663.9, 462.4, 916.1, 239.2, 45.5, 797.1, 221.1, 207.1, 651.2, 245, 493.2, 970.7, 377.29],
        'output': [0.065, 0.068, 0.0, 0.005, 0.065, 0.08, 0.075, 0.068, 0.047, 0.093, 0.024, 0.005, 0.081, 0.023, 0.021, 0.066, 0.025, 0.05, 0.099, 0.038]
    },
]

@pytest.fixture(params=test_cases_task1)
def shares(request):
    return request.param

def test_task_example(shares, capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('\n'.join([str(num) for num in shares['input']])))

    count_shares = CountShares()
    count_shares()

    out, err = capsys.readouterr()
    assert err == '', 'not empty errors'

    assert [float(num) for num in out.split('\n')[:-1]] == shares['output'], f"test case {shares['input']}"
