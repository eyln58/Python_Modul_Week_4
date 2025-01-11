

def screen(file_path = 'Membership'):
    
    with open('Library_system/'+file_path+'.txt', 'r') as file:
        while True:
            char = file.read(1)  # Read one character at a time
            if not char:  # Break loop if end of file
                break
            print(char, end='')

if __name__ == '__main__':
    screen()