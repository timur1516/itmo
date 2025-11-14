from abc import abstractmethod


class Reader:
    @abstractmethod
    def read(self, text=None):
        pass


class ConsoleReader(Reader):
    def read(self, text=None):
        return input() if text is None else input(text)


class FileReader(Reader):
    def __init__(self, path):
        self.file = open(path, 'r')

    def read(self, text=None):
        return self.file.readline()

    def close(self):
        self.file.close()


class Writer:
    @abstractmethod
    def write(self, data):
        pass
