import textwrap

def wrap(string, max_width):
    wrapped = ''
    
    for index, letter in enumerate(string):
        # Add the newline character if the index is divisible by the max_width
        if index % max_width == 0 and wrapped:
            wrapped += '\n'
        
        wrapped += letter
            
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
