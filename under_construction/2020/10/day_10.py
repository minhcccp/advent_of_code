if __name__ == "__main__":
    with open("input_10.txt") as source, open("output_10.txt", "w") as output:
        num_list = [0] + sorted(int(value) for value in source.read()[:-1].split("\n"))
        previous = 0
        for num in num_list:
            output.write(("\n" if num - previous > 2 else "") + f"{num}\n")
            previous = num
