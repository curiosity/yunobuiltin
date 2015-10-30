import functools
from yunobuiltin import compose, thread, pipeline, rpartial, partial

def test_partial_available():
    assert partial is functools.partial

def test_rpartial():
    assert rpartial(lambda x, y: x ** y, 4)(2) == 16

def _append_str(s, x):
    x +=  s
    return x

_append_foo = partial(_append_str, ' foo ')
_append_bar = partial(_append_str, ' bar ')
_append_spam = partial(_append_str, ' spam ')

def test_pipeline():
    f = pipeline(_append_foo, _append_bar, _append_spam)
    assert f('') == ' foo  bar  spam '

def test_thread():
    assert (thread('', _append_foo, _append_bar, _append_spam)
            == ' foo  bar  spam ')

def test_compose():
    f = compose(_append_foo, _append_bar, _append_spam)
    assert f('') == ' spam  bar  foo '
