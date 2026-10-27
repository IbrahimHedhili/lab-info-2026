import mystats
def main():
    file_name = str(input("Insert the name of the file containing the sample of events : "))
    mystats.disp_stats(file_name)

if __name__ == "__main__":
    main()