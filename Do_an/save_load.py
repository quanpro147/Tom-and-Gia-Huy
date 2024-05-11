import pickle

class saveloadsystem():
    def __init__(self, file_extension, folder):
        self.file_extension = file_extension
        self.folder = folder
    
    def save_maze(self, name_file, maze):
        """ Ham luu maze voi ten file vao maze_manager """
        self.add_file_name(name_file)
        data = self.process_maze_to_save(name_file, maze)
        with open(self.folder + self.file_extension, 'wb+') as f:          
            pickle.dump(data, f)

    def process_maze_to_save(self,name_file, maze):
        """ Ham nay dung de them maze muon luu vao maze_manager quan ly cac maze khac """
        try:
            maze_manager = self.load_data()
            maze_manager[name_file] = maze
            return maze_manager
        except EOFError:
            return {name_file: maze}
        
    def load_data(self):
        """ Ham phu tro de lay maze_manager """
        with open(self.folder + self.file_extension, 'rb') as f:
            data = pickle.load(f)
        return data
        
    def load_maze(self, name_file):
        """ Ham nay dung de load maze tu ten file da luu """
        if self.check_file_name(name_file):
            maze_manager = self.load_data()
            for key, val in maze_manager.items():
                if key == name_file:
                    return val
        else:
            # raise error
            return False
        
    def add_file_name(self, name_file):
        with open('Do_an/SaveLoad/saveload.txt', 'a') as f:
            f.write(name_file + '\n')
    
    def check_file_name(self, name_file):
        with open('Do_an/SaveLoad/saveload.txt', 'r') as f:
            name_files = f.readlines()
            for _name_file in name_files:
                _name_file = _name_file[:-1]
                if name_file == _name_file:
                    return True
        return False