import pickle

class saveloadsystem():
    def __init__(self, file_extension, folder):
        self.file_extension = file_extension
        self.folder = folder
    
    def save(self, name_file, data):
        data_file = open(self.folder + '/' + name_file + self.file_extension, 'wb')
        pickle.dump(data, data_file)
    def load(self, name_file):
        data_file = open(self.folder + '/' + name_file + self.file_extension, 'rb')
        data = pickle.load(data_file)
        return data
        