========================
Working With Collections
========================

Better __*item__
=================

.. py:function:: get(obj, key[, default])

.. py:function:: assoc(obj, key1, value1[, key2, value2, ...])

.. py:function:: assoc_kw(obj, key1=value1[, key2=value2, ...])

.. py:function:: update(obj, key, callable, *args, **kwargs)

.. py:function:: dissoc(obj, key)


Nested __*item__
================

The `_in` functions provide nested ``__*item__`` access based on an iterable of ``__getitem__`` lookups.
Practically, this means that to access the ``eggs`` in:

.. code:: python
    
    x = {'foo': {'bar': {'spam': 'eggs'}}}


You could use ``get_in(x, ['foo', 'bar', 'spam'])``. The ``['foo', 'bar', 'spam']`` is the iterable of ``__getitem__`` lookups that is usable across this family of functions. It is much shorter, especially when you compare to the semantic equivalent:

.. code:: python

    get_in(x, ['foo', 'bar', 'spam'])

    # vs

    x.get('foo', {}).get('bar', {}).get('spam')

This is especially apparent when you need to programatically construct paths through nested structures, as constructing a list or iterable is very easy.

Note on `None`
--------------

In general, `_in` functions are safe with Nones, and act upon Nones encountered as though they are empty dictionaries. 

The `_in` functions
-------------------

These functions are inspired by similar functions that exist in Clojure and Clojurescript. They are handy for working with JSON and YAML apis.

.. py:function:: get_in(obj, lookup_iterable[, default=None])

    Walk a copy of `obj` using ``__getitem__`` calls for each element in `lookup_iterable`. Return the value
    found at `lookup_iterable`, or `default` (`None`) if any element of `lookup_iterable` cannot be found. 

    Examples:

    .. code:: python

        x = {'foo': {'bar': {'spam': 'eggs'}}}

        # lookup at a path
        'eggs' == get_in(x, ['foo', 'bar', 'spam'])

        # if something isn't found, return None
        None is get_in(x, ['foo', 'baz', 'spam'])

        # if something isn't found and a default is provided, return the default
        'adefault' == get_in(x, ['foo', 'baz', 'spam'], 'adefault')

.. py:function:: assoc_in(obj, lookup_iterable, value)

    Walk a copy of `obj` using ``__getitem__`` calls for each element in `lookup_iterable`. If an element is not found,
    create a dictionary at its place and continue. For the final element, call ``__setitem__`` with the element
    and `value`. Return the modified copy of `obj`.

    Examples:

    .. code:: python

        x = {'foo': {'bar': {'spam': 'eggs'}}}

        # assoc_in performs a nested write
        y = assoc_in(x, ['foo', 'bar', 'spam'], 1)
        1 == get_in(y, ['foo', 'bar', 'spam'])

        # assoc_in can nested write any value, and previous
        # assoc_ins did not mutate x
        z = assoc_in(x, ['foo', 'baz'], {'pika': 'chu'})
        'chu' == get_in(z, ['foo', 'baz', 'pika'])
        'eggs' == get_in(z, ['foo', 'bar', 'spam'])

.. py:function:: update_in(obj, lookup_iterable, callable, *args, **kwargs)

    Walk a copy of `obj` using ``__getitem__`` calls for each element in `lookup_iterable`. If an element is not found,
    create a dictionary at its place and continue. For the final element, call ``__setitem__`` with the element and
    the result of calling ``callable(current_value, *args, **kwargs)``. Return the modified copy of `obj`.

    Examples:

    .. code:: python

        x = {'foo': {'bar': {'spam': 'eggs'}}}

        # update_in applies a function at lookup_interable
        y = update_in(x, ['foo', 'bar', 'spam'], lambda x: x.upper())
        'EGGS' == get_in(y, ['foo', 'bar', 'spam'])

        # update_in can take arguments to the callable
        def add_n(x, n):
            return x + n
        w = assoc_in(x, ['foo', 'bar', 'baz'], 0)
        z = update_in(w, ['foo', 'bar', 'baz'], add_n, 10)
        10 == get_in(z, ['foo', 'bar', 'baz'])

.. py:function:: dissoc_in(obj, lookup_iterable)

    Walk a copy of `obj` using ``__getitem__`` asserting that the final element in `lookup_iterable` does not exist apparent
    the specified path. Return the modified copy of `obj`.

    Examples:

    .. code:: python

        x = {'foo': {'bar': {'spam': 'eggs'}}}

        # dissoc_in asserts a path doesn't exist
        y = dissoc_in(x, ['foo', 'bar'])
        None is get_in(y, ['foo', 'bar'])

        # dissoc_in doesn't mutate the original obj
        {'spam': 'eggs'} == get_in(x, ['foo', 'bar'])

Merging Dictionaries
====================

.. py:function:: merge_with(callable, *dictionaries)

.. py:function:: merge(*dictionaries)

.. py:function:: deep_merge_with(callable, *dictionaries)

.. py:function:: deep_merge(*dictionaries)

Named Access to Places of an Iterable
=====================================

.. py:function:: first(iterable)
.. py:function:: second(iterable)
.. py:function:: third(iterable)
.. py:function:: fourth(iterable)
.. py:function:: fifth(iterable)
.. py:function:: sixth(iterable)
.. py:function:: seventh(iterable)
.. py:function:: eighth(iterable)
.. py:function:: ninth(iterable)

.. py:function:: last(iterable)

Utilities
=========
.. py:function:: select_keys(keys_iterable, dictionary[, default=None])
.. py:function:: select_vals(keys_iterable, dictionary[, default=None])
.. py:function:: select_keys_flat(keys_iterable, dictionary[, default=None)

    Deprecated. Alias for ``select_vals``.

.. py:function:: prepend(value, iterable)

    Prepend a `value` to `iterable`. If `iterable` is a ``list``, mutate the list.

.. py:function:: append(value, iterable)

    Append a `value` to `iterable`. If `iterable` is a ``list``, mutate the list.

.. py:function:: cons(value, iterable):
    
    Deprecated. Alias for ``prepend``.

.. py:function:: conj(value, iterable):
    
    Deprecated. Alias for ``append``.

.. py:function:: concat(*items)

    Concatenates `items` which may be values or iterables into a single iterable. Nested
    iterables are not walked. ``basestring`` and ``bytes`` are **NOT** considerable iterables for the
    purposes of ``concat``.

.. py:function:: flatten1(*items)

    Concatenates `items` which may be values or iterables into a single list. Nested 
    iterables are not walked.  ``basestring`` and ``bytes`` are **NOT** considered iterables for the
    purposes of ``flatten1``.

.. py:function:: flatten(iterable)

    Recursively flatten `iterable` into a single iterable. ``basestring`` and ``bytes`` are **NOT**
    considered iterables for the purposes of ``flatten``.

.. py:function:: group_by(grouper_callable, iterable)
.. py:function:: group_by_and_transform(grouper_callable, transformer_callable, iterable)

.. py:function:: dedup(iterable)
    
    Returns a list of the iterable with duplicates removed. Order is non-deterministic.

.. py:function:: transform_tree(transformer_callable, tree)
    
    Walks `tree` (a dict of dicts), depth-first, calling ``transformer_callable(k, v)`` to transform.

    The `transformer_callable` should take two arguments, the key and the value, and return a
    2-tuple with the new key and the new value. For example, an identity transformer_callable would
    be:

    .. code:: python

         def identity_transformer(k, v):
             return (k, v)

    Examples:

    .. code:: python

        t = {'a': {'b': {'c': 'd'}, 'e': {'f': 'g'}}, 'h': 'i'}
        
        def uppercase_keys_transformer(k, v):
            return (k.upper(), v)
        
        z = transform_tree(uppercase_keys_transformer, t)
        z == {'A': {'B': {'C': 'd'}, 'E': {'F': 'g'}}, 'H': 'i'}
