input_type = input()
input_data = input()


def action(data_type, data):
    if data_type == "int":
        data = int(data)
        print(data*2)
    elif data_type == "real":
        data = float(data)
        print(f'{data*1.5:.2f}')
    else:
        print('$' + data + '$')


action(input_type, input_data)

