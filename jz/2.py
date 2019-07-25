def convert_blank(str):
    return str.replace(' ', '%20')

if __name__ == '__main__':
    print(convert_blank('We Are Happy!'))