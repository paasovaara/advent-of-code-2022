from enum import Enum 

POINTS_FOR_LOSING = 0
POINTS_FOR_DRAW = 3
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

class ExpectedOutcome(Enum):
    LOSE = 'lose'
    WIN = 'win'
    DRAW = 'draw'

def parse_expected_outcome(input_string):
    input_string = input_string.upper()
    if input_string == 'X':
        return ExpectedOutcome.LOSE
    elif input_string == 'Y':
        return ExpectedOutcome.DRAW
    elif input_string == 'Z':
        return ExpectedOutcome.WIN
    else:
        raise ValueError("Invalid input: {}".format(input_string))

def determine_score(opponent: Shape, me: Shape) -> int: 
    score = shape_value(me)
    if opponent == me:
        return score + POINTS_FOR_DRAW
    else:
        if (opponent == Shape.PAPER and me == Shape.SCISSORS) or \
            (opponent == Shape.SCISSORS and me == Shape.ROCK) or \
            (opponent == Shape.ROCK and me == Shape.PAPER):
            return score + POINTS_FOR_WIN
        else:
            return score + POINTS_FOR_LOSING

def determine_my_shape(opponent: Shape, outcome: ExpectedOutcome) -> Shape: 
    if outcome == ExpectedOutcome.DRAW:
        return opponent
    else:
        if outcome == ExpectedOutcome.WIN:
            if opponent == Shape.SCISSORS:
                return Shape.ROCK
            elif opponent == Shape.ROCK:
                return Shape.PAPER
            elif opponent == Shape.PAPER:
                return Shape.SCISSORS
        else:
            if opponent == Shape.ROCK:
                return Shape.SCISSORS
            elif opponent == Shape.SCISSORS:
                return Shape.PAPER
            elif opponent == Shape.PAPER:
                return Shape.ROCK

def resolve_battle(opponent: Shape, outcome: ExpectedOutcome) -> int:
    my_shape = determine_my_shape(opponent, outcome)
    return determine_score(opponent, my_shape)

class Main:
    def run(self):
        battle_input = self.read_values()
        print(battle_input)

        # Note to self: is it better to use this for-syntax or map? 
        battle_scores = [resolve_battle(input[0], input[1]) for input in battle_input]
        print(battle_scores)
        
        total_score = sum(battle_scores)
        print(total_score)
    
    def read_values(self) -> list[tuple[Shape, ExpectedOutcome]]:
        input = []
        with open("input.txt", 'r') as file:
            for line in file:
                try:        
                    splitted = line.strip().split(" ")
                    if len(splitted) == 2:
                        input_shape = parse_shape(splitted[0])
                        outcome = parse_expected_outcome(splitted[1])
                        
                        input.append((input_shape, outcome))
                except Exception as e:
                    print('Error occurred', e)
        return input

    

    
if __name__=='__main__':
    main = Main()
    main.run()