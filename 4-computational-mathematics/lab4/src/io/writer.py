from abc import abstractmethod


class Writer:
    @abstractmethod
    def write(self, data):
        pass


class ConsoleWriter(Writer):
    def write(self, text):
        print(text)


class FileWriter(Writer):
    def __init__(self, path):
        self.file = open(path, 'w')

    def write(self, text):
        self.file.write(text + '\n')

    def close(self):
        self.file.close()
