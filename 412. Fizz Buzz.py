def fizzBuzz(n: int) -> [str]:
    ans = []
    for i in range(1, n+1):
        temp = ""
        if i % 3 == 0:
            temp += "Fizz"
        if i % 5 == 0:
            temp += "Buzz"
        if temp == "":
            temp = str(i)
        ans.append(temp)
    return ans


if __name__ == '__main__':
    print(fizzBuzz(15))
