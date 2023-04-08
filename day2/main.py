from enum import Enum 

POINTS_FOR_LOSING = 0
POINTS_FOR_TIE = 3
POINTS_FOR_WIN = 6

class Shape(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSORS = 'scissors'

def shape_value(shape: Shape) -> int:
    if shape == Shape.ROCK:
        return 1
    elif shape == Shape.PAPER:
        return 2
    elif shape == Shape.SCISSORS:
        return 3

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


class Main:
    def run(self):
        battle_input = self.read_values()
        print(battle_input)

        # Note to self: is it better to use this for-syntax or map?
        battle_scores = [self.determine_score(input[0], input[1]) for input in battle_input]
        print(battle_scores)
        
        total_score = sum(battle_scores)
        print(total_score)
    
    def read_values(self) -> list[tuple[Shape]]:
        shapes = []
        with open("input.txt", 'r') as file:
            for line in file:
                try:        
                    splitted = line.strip().split(" ")
                    if len(splitted) == 2:
                        # Note to self: is it better to use this for-syntax or map?
                        input_shape = tuple(map(parse_shape, splitted))
                        shapes.append(input_shape)
                except Exception as e:
                    print('Error occurred', e)
        return shapes

    def determine_score(self, opponent: Shape, me: Shape) -> int: 
        score = shape_value(me)
        if opponent == me:
            return score + POINTS_FOR_TIE
        else:
            if (opponent == Shape.PAPER and me == Shape.SCISSORS) or \
                (opponent == Shape.SCISSORS and me == Shape.ROCK) or \
                (opponent == Shape.ROCK and me == Shape.PAPER):
                return score + POINTS_FOR_WIN
            else:
                return score + POINTS_FOR_LOSING

    
if __name__=='__main__':
    main = Main()
    main.run()