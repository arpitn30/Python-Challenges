def reverse_string(input_string):
    return input_string[::-1]


if __name__ == '__main__':
    my_string = "Hello Python"
    output_string = reverse_string(my_string)
    print("Your reverse string is: \n{}".format(output_string))
