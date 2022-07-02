from re import A


def load_text():
    # Get the text from the story file
    with open('Texts\Text.txt') as f:
        the_text = f.read()
        return the_text

def convert_text(given_text, _counter):
    # Convert the text from the file to gameplay
    exit_counter = 0
    inner_counter = 0
    inner_counter2 = 0
    print_string = []
    for i in given_text:
        if(i == _counter):
            # if i could be what we're looking for, check to make sure it is:
            return_string = []
            
            if given_text[inner_counter+1] == "\"":
                # if the text is followed " <---     "
                for h in given_text:
                    if (inner_counter > given_text.index(i)):
                        if inner_counter2 > inner_counter:
                            if h != "\"" and h != "|" and h != "#":
                                print_string.append(h)
                            elif h == "|":
                                return_string.append(''.join(print_string))
                                print_string.clear()
                            elif h == "#":
                                return_string.append(''.join(print_string))
                                return return_string
                            elif h == "\"":
                                print(''.join(print_string))
                                print_string.clear()
                        inner_counter2+=1
        inner_counter+=1


def get_user_input():
    # Gets the user's input
    response=input()
    return response

def main():
    playing = True
    the_text = load_text()
    counter = 'b'

    while playing == True:
        options = convert_text(the_text, counter)
        input = get_user_input()
        if input.upper() == "A":
            counter = options[0]
            pass
        elif input.upper() =="B":
            counter = options[1]
            pass
        else:
            print("AYO, your input was not recognized (a or b)")




    pass

if __name__ == "__main__":
   main()