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


def test_list_combinations():
    prio = {
        'value': 'this should stay',
        'listhere': ['from prio']
    }
    not_prio = {
        'value': 'to be removed',
        'listhere': ['from not prio']
    }
    expected = {
        'value': 'this should stay',
        'listhere': ['from not prio', 'from prio']
    }
    result = prio_merge(prio, not_prio)
    assert result == expected


def test_nested_fields():
    prio = {
        'value': {
            'index1': 'value here',
            'index2': 'should stay'
        }
    }
    not_prio = {
        'value': {
            'index2': 'remove this!',
            'index3': 'index here'
        }
    }
    expected = {
        'value': {
            'index1': 'value here',
            'index2': 'should stay',
            'index3': 'index here'
        }
    }
    result = prio_merge(prio, not_prio)
    assert result == expected


def test_nested_lists():
    prio = {
        'value': {
            'index1': 'value here',
            'index2': 'should stay',
            'list_key': ['list item one']
        }
    }
    not_prio = {
        'value': {
            'index2': 'remove this!',
            'index3': 'index here',
            'list_key': ['list item two']
        }
    }
    expected = {
        'value': {
            'index1': 'value here',
            'index2': 'should stay',
            'index3': 'index here',
            'list_key': ['list item one', 'list item two']
        }
    }
    result = prio_merge(prio, not_prio)
    assert result == expected
