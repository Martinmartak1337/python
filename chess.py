def main():
    print("enter your file path \n")
    file_path = input()
    try:
        with open(file_path) as dot:
            contents = dot.read()
            print(contents)
            dot.close()
    except Exception as e:
        print("cannot read file: " + file_path)
        print(e)

main()
