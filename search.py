def file_read():
    try:
        print("To open files in mazes/ with '.lay.txt' extension, just type the file name itself.")
        file_input = input('mazes/')
        file_name = 'mazes/' + file_input + '.lay.txt'
        l = [line.rstrip('\n') for line in open(file_name, 'r')]
        pattern = []

        for item in l:
            tmp = []
            for character in item:
                tmp.append(character)
            pattern.append(tmp)

        return pattern
    except FileNotFoundError:
        print("{} does not exist.".format(file_name))
        ptrn = file_read()
        return ptrn


def main():
    maze_pattern = file_read()
    print(maze_pattern)


if __name__ == "__main__":
    main()
