def number_to_words(num):
    words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    for digit in str(num):
        print(words[int(digit)], end=" ")


if __name__ == "__main__":
    num = int(input("Enter number: "))
    number_to_words(num)
