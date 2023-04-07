class Main:

    def run(self):
        filename = "input.txt"
        lists = [[]] 

        with open(filename, "r") as file:
            for line in file:
                line = line.strip() 
                
                if line == "":
                    # if the line is empty, create a new empty list
                    lists.append([])
                else:
                    # if the line is not empty, convert it to an integer and append to the last list
                    lists[-1].append(int(line))

        # sum the sublists
        sums = [sum(sublist) for sublist in lists]
        print("Part 1: Max calories for one elf was", max(sums))

        # Calculate the sum of top three items
        sorted_list = sorted(sums, reverse=True)
        top_three = sorted_list[:3]
        sum_for_three = sum(top_three)
        print("Part 2: Three elves carrying ", sum_for_three, " calories")
        

if __name__ == '__main__':
    main = Main()
    main.run()