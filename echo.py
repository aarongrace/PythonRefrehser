#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo"""
    res = ""
    for i in range (repetitions, 0, -1):
        ending = text[-i:] + '\n'
        res += ending
    res += '.'
    return res


if __name__ == "__main__":
    text = input("Yell something at at a mountain: ")
    print(echo(text))