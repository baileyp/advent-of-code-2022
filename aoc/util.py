class FileReader:
    def __init__(self, f):
        self._file = f

    def __iter__(self):
        return map(lambda x: x.strip(), iter(self._file))

    def single_line(self):
        return next(iter(self))

    def raw(self):
        return iter(self._file)


class defaultlist(list):
    def __init__(self, fx):
        self._fx = fx

    def _fill(self, index):
        while len(self) <= index:
            self.append(self._fx())

    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)
