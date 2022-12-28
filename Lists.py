if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for index in range(N):
        command = list(input().split())
        
        # checks if the stated method takes two arguments
        if len(command) == 3:
            eval('arr.' + command[0] + '(' + command[1] + ',' + command[2] + ')')
        
        # checks if the stated method or command takes one arguments
        elif len(command) == 2:
            eval('arr.' + command[0] + '(' + command[1] +  ')')
        
        # checks if the command is a print command 
        elif command[0] == 'print':
            print(arr)
        
        # checks if the command takes no arguments
        else:
            eval('arr.' + command[0] + '()')
