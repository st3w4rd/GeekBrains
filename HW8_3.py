class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")

        if user_input == "stop":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' has not numerical format")

            my_list.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_list)
