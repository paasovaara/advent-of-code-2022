from enum import Enum 

class Shape(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'


def parse_shape(input_string):
    input_string = input_string.upper()
    if input_string in ['A', 'X']:
        return Shape.ROCK
    elif input_string in ['B', 'Y']:
        return Shape.PAPER
    elif input_string in ['C', 'Z']:
        return Shape.SCISSORS
    else:
        raise ValueError("Invalid input: {}".format(input_string))

#def determine_score(opponent_shape: Shape, )

class Main:
    def run(self):
        battle_input = self.read_values()
        print(battle_input)
    
    def read_values(self) -> list[tuple[Shape]]:
        shapes = []
        with open("input.txt", 'r') as file:
            for line in file:
                try:        
                    splitted = line.strip().split(" ")
                    if len(splitted) == 2:
                        input_shape = tuple(map(parse_shape, splitted))
                        shapes.append(input_shape)
                        #opponent = parse_input(splitted[0])
                        #me = parse_input(splitted[1])
                except Exception as e:
                    print('Error occurred', e)
        return shapes

    
if __name__=='__main__':
    main = Main()
    main.run()