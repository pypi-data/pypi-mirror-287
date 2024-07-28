import os
from collections.abc import Callable
from typing import Union
import fnmatch
import re

Predicate = Callable[[str, str], bool]

Callback = Callable[[str, str], None]

class Collector:
    def __init__(self):
        self._collection = []

    def __call__(self, name, path):
        self._collection.append(path)

class NamePredicate:
    def __init__(self, patterns):
        self._patterns = patterns
    def __call__(self, name, path):
        for pattern in self._patterns:
            if isinstance(pattern, re.Pattern):
                if pattern.match(name):
                    return True
            elif isinstance(pattern, str):
                if fnmatch.fnmatch(name, pattern):
                    return True
            else:
                raise ValueError("expected str or re.Pattern as pattern, got {}".format(type(pattern)))
        return False

class SizePredicate:
    def __init__(self, low, high):
        if low is None and high is None:
            raise ValueError("both low and high is None, predicate is useless")
        self._low = low
        self._high = high
    def __call__(self, name, path):
        if not os.path.isfile(path):
            return False
        size = os.path.getsize(path)
        low = self._low
        high = self._high
        return (low is None or size > low) and (high is None or size < high)

def size_kb(v: int):
    return v * 1024

def size_mb(v: int):
    return v * 1024 * 1024

def size_gb(v: int):
    return v * 1024 * 1024 * 1024

def size_tb(v: int):
    return v * 1024 * 1024 * 1024 * 1024

def with_dot(ext):
    if not ext.startswith('.'):
        return '.' + ext
    return ext

class ExtPredicate:
    def __init__(self, patterns):
        self._patterns = patterns
    def __call__(self, name: str, path: str):
        ext = os.path.splitext(name)[1].lower()
        for pattern in self._patterns:
            if isinstance(pattern, re.Pattern):
                if pattern.match(name):
                    return True
            elif isinstance(pattern, str):
                if with_dot(pattern.lower()) == ext.lower():
                    return True
            else:
                raise ValueError("expected str or re.Pattern as pattern, got {}".format(type(pattern)))
        return False

def matches(name, path, predicates: list[Predicate]):
    for predicate in predicates:
        if not predicate(name, path):
            return False
    return True

def path_depth(path: str, base: str) -> int:
    rel = os.path.relpath(path, base)
    if rel == '.':
        return 0
    return len(re.split('[/\\\\]', rel))

class Find:
    def __init__(self, paths):
        paths = list(paths)
        if len(paths) == 0:
            paths.append(os.getcwd())
        self._paths = paths
        self._predicates: list[Predicate] = []
        self._do_files = False
        self._do_dirs = False
        self._maxdepth = 0

    def files(self):
        self._do_files = True
        return self

    def dirs(self):
        self._do_dirs = True
        return self
    
    def ext(self, *patterns: Union[str, re.Pattern]):
        self._predicates.append(ExtPredicate(patterns))
        return self

    def name(self, *patterns: Union[str, re.Pattern]):
        self._predicates.append(NamePredicate(patterns))
        return self

    def size(self, low = None, high = None):
        self._predicates.append(SizePredicate(low, high))
        return self

    def filter(self, predicate: Predicate):
        self._predicates.append(predicate)
        return self
    
    def maxdepth(self, n : int):
        self._maxdepth = n
        return self

    def for_each(self, callback: Callback):
        do_dirs = self._do_dirs
        do_files = self._do_files
        if not do_dirs and not do_files:
            do_dirs = True
            do_files = True
        for path in self._paths:
            for root, dirs, files in os.walk(path):
                if self._maxdepth > 0 and path_depth(root, path) == self._maxdepth:
                    while len(dirs) > 0:
                        dirs.pop()
                    continue
                if do_files:
                    for f in files:
                        p = os.path.join(root, f)
                        if matches(f, p, self._predicates):
                            callback(f, p)
                if do_dirs:
                    for f in dirs:
                        p = os.path.join(root, f)
                        if matches(f, p, self._predicates):
                            callback(f, p)

    def collect(self) -> list[str]:
        collector = Collector()
        self.for_each(collector)
        return collector._collection

def find(*paths):
    return Find(paths)