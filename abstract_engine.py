class abstract_engine:

    # chess.color where white = True, black = False
    def __init__(self, color):
        self.color = color

    # returns chess.move
    def get_move(self, current_board):
        print("ERROR: Function not overriden in child class")

# Example implementation
# class test_engine(abstract_engine):
#     def __init__(self):
#         pass
