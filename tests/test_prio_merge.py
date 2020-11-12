"""
Tests for prio merge
"""

from prio_merge import prio_merge


def test_empty_dicts():
    prio = {}
    not_prio = {}
    result = prio_merge(prio, not_prio)
    assert result == {}


def test_one_equal_entry():
    prio = {
        'value': 'this should stay',
        'not in other': 'not in other'
    }
    not_prio = {
        'value': 'to be removed',
        'not in prio': 'nowhere'
    }
    expected = {
        'value': 'this should stay',
        'not in other': 'not in other',
        'not in prio': 'nowhere'
    }
    result = prio_merge(prio, not_prio)
    assert result == expected

