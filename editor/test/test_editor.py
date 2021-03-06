import pytest

from editor.__main__ import Buffer


def test_buffer_init_from_text():
    b = Buffer('hello\nworld')
    assert b.get_lines() == ['hello', 'world']


def test_buffer_init_empty():
    b = Buffer()
    assert b.get_lines() == ['']


def test_buffer_get_lines():
    b = Buffer()
    assert b.get_lines() == ['']

    b = Buffer('foo')
    assert b.get_lines() == ['foo']

    b = Buffer('foo\nbar')
    assert b.get_lines() == ['foo', 'bar']

    b = Buffer('foo\n\nbar')
    assert b.get_lines() == ['foo', '', 'bar']

    b = Buffer()
    b.get_lines().append('f')
    assert b.get_lines() == ['']


def test_buffer_set_text():
    b = Buffer('foo baz')
    b.set_text(0, 3, 0, 3, ' bar')
    assert b.get_lines() == ['foo bar baz']

    b = Buffer()
    b.set_text(0, 0, 0, 0, 'foo\nbar')
    assert b.get_lines() == ['foo', 'bar']

    b = Buffer('foo REPLACE baz')
    b.set_text(0, 4, 0, 11, 'bar')
    assert b.get_lines() == ['foo bar baz']

    b = Buffer('this is\na test')
    b.set_text(0, 5, 1, 1, 'was\nthe')
    assert b.get_lines() == ['this was', 'the test']

    b = Buffer('this foois\na test')
    b.set_text(0, 8, 0, 8, ' ')
    assert b.get_lines() == ['this foo is', 'a test']


def test_buffer_set_text_negative_row():
    b = Buffer('foo\nbar')
    with pytest.raises(ValueError):
        b.set_text(-1, 0, 0, 0, 'a')
    with pytest.raises(ValueError):
        b.set_text(0, 0, -1, 0, 'a')


def test_buffer_set_text_nonexistent_row():
    b = Buffer('foo\nbar')
    with pytest.raises(ValueError):
        b.set_text(2, 0, 0, 0, 'a')
    with pytest.raises(ValueError):
        b.set_text(0, 0, 2, 0, 'a')


def test_buffer_set_text_negative_col():
    b = Buffer('foo\nbar')
    with pytest.raises(ValueError):
        b.set_text(0, -1, 0, 0, 'a')
    with pytest.raises(ValueError):
        b.set_text(0, 0, 0, -1, 'a')


def test_buffer_set_text_nonexistent_col():
    b = Buffer('foo\nbar')
    with pytest.raises(ValueError):
        b.set_text(0, 4, 0, 0, 'a')
    with pytest.raises(ValueError):
        b.set_text(0, 0, 0, 4, 'a')
