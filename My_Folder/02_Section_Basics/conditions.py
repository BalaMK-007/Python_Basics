# Conditionals

def main():
    x,y = 1000,1000

    #Conditional flow statements if, elseif(elif), else
    # if x < y:
    #     result = "x is less than y"
    # elif x == y:
    #     result = "x is same as y"    
    # else:
    #     result = "x is greater than Y"

    # print(result)

    # Conditional statements let you use "a if c else b"
    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "-87"

    match value:
        case "one":
            answer = 1
        case "two":
            answer = 2
        case "three" | "four":
            answer = (3,4)
        case _:
            answer = -1

    print(answer)

# Calling the function
if __name__ == "__main__":
    main()