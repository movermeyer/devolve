import pytest

from devolve.registry import Registry


def test_single_key_registration():
    registry = Registry()

    @registry.register('foo')
    def test_fn(*args, **kwargs):
        pass

    assert registry.functions['foo'] == test_fn


def test_multi_key_registration():
    registry = Registry()

    @registry.register('foo', 'bar')
    def test_fn(*args, **kwargs):
        pass

    assert registry.functions['foo'] == test_fn
    assert registry.functions['bar'] == test_fn


def test_key_collision():
    registry = Registry()

    @registry.register('foo', 'baz')
    def test_fn(*args, **kwargs):
        pass

    def other_test_fn(*args, **kwargs):
        pass

    with pytest.raises(ValueError):
        registry.register('bar', 'baz')(other_test_fn)


def test_duplicate_registration():
    registry = Registry()

    @registry.register('foo', 'baz')
    def test_fn(*args, **kwargs):
        pass

    with pytest.raises(ValueError):
        registry.register('baz')(test_fn)


def test_function_with_single_return_value():
    registry = Registry()

    @registry.register('foo')
    def test_fn():
        return 3

    data = registry()

    assert data == {'foo': 3}


def test_function_with_mapping_return_value():
    registry = Registry()

    expected = {
        'foo': 3,
        'bar': 4,
    }

    @registry.register('foo', 'bar')
    def test_fn():
        return expected

    data = registry()

    assert data == expected


def test_handles_failing_functions():
    registry = Registry()

    @registry.register('foo', 'bar')
    def test_fn():
        return {
            'foo': 2,
            'bar': 3,
        }

    @registry.register('baz')
    def other_test_fn():
        return 1

    @registry.register('bang')
    def bad_fn():
        assert False

    data = registry()

    assert data == {
        'foo': 2,
        'bar': 3,
        'baz': 1,
    }
