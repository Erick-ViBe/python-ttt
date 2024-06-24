def normal_f():

    def get_animal():
        return 'horse'

    return f"There is a {get_animal()}"

x = normal_f()
print(x)


# def process_file(filename):

    # def compute_new_data(some_data):
        # return some_data.replace('#', '<hashtag>')

    # with open(filename, 'r') as f:
        # data = filename.read()
        # result = compute_new_data(data)

    # return result
