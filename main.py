from preprocessor import preprocessor
from csv_parser import csv_parser

def main():
    csvParser_1 = csv_parser("./messages/messages_1.csv")
    bodies_1 = csvParser_1.get_bodies()

    csvParser_2 = csv_parser("./messages/messages_2.csv")
    bodies_2 = csvParser_2.get_bodies()

    csvParser_3 = csv_parser("./messages/messages_3.csv")
    bodies_3 = csvParser_3.get_bodies()

    csvParser_4 = csv_parser("./messages/messages_4.csv")
    bodies_4 = csvParser_4.get_bodies()

    bodies = bodies_1 + bodies_2 + bodies_3 + bodies_4
    lines = []

    preproc = preprocessor()
    for body in bodies:
        proclines = preproc.proc_body(body, name = "john", email = "JohnDoe@gmail.com")
        for line in proclines:
            lines.append(line)

    print(">> line length " + str(len(lines)))

    empty_file("proctemp.txt")
    write_to_file("proctemp.txt", lines)

def write_to_file(file, lines):
    print(">> writing lines to " + file)
    #cp437
    with open(file, 'a', encoding='utf-8') as file:
        for line in lines:
            #print("- " + line)
            file.write(line + '\n')

def empty_file(file):
    print(">> emptied " + file)
    with open(file, 'w', encoding='utf-8') as file:
        file.write('')

if __name__ == "__main__":
    main()
