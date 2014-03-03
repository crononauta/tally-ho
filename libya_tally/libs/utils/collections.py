from itertools import chain


def flatten(l):
    return list(chain.from_iterable(l))


def keys_if_value(d):
    return [k for k, v in d.iteritems() if v]


def listify(maybe_list):
    """Make maybe list a list if it is not.

    :param maybe_list: A variable that may be a list.

    :returns: A list."""
    return [maybe_list] if not isinstance(maybe_list, list) else maybe_list
