"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

# Cedric Anover, 4/08/2023
file_name = 'mbox-short.txt'

def get_line(line_number):
    global file_name

    counter = 0

    with open(file_name, 'r') as file:
        for line in file.readlines():
            try:
                if counter + 1 == line_number:
                    return line
                counter += 1
            except:
                return None

# while True:
#     try:
#         line_number = int(input("Enter a Line Number: "))
#         if line_number < 1:
#             print("Line Number can only be a Positive Integer! Please try again ...")
#             continue
#         else:
#             result = get_line(line_number)
#             if result is None:
#                 print("Line Number is Out of Range! Please try again ...")
#                 continue
#             else:
#                 print(result)
#                 break
#     except:
#         print("Invlid Input! Please try again ...")
#         continue

def main():
    global file_name

    emails = []

    with open(file_name, 'r') as file:

        # Use this instead
        # for line in file:
        #     print(line)

        while True:
            line = file.readline()
            
            if "From " in line:
                line.rstrip()
                line = line[:-1]

                line_word_ls = line.split()
                email = line_word_ls[1]

                emails.append(email)

            if not line:
                break
    
    # for email in emails:
    #     print(email)

if __name__ == "__main__":
    main()