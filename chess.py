def main():
    try:
        print("enter your file path \n")
        file_path = input()
        with open(file_path) as dot:
            contents = dot.read()
            print(contents)
    except Exception as e:
        print("cannot read file: " + file_path)
        print(e)

main()
