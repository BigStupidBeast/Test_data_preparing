from itertools import product, permutations, combinations, combinations_with_replacement, pairwise


def give_me_all_combinations(cooked_array, length_of_tuples_in_result=2):
    """
    create all combinations
    for example: ['A', 'B', 'C', 'D'] and 2
    will return AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    :param cooked_array: origin array for combination creating
    :param length_of_tuples_in_result: int. default=2
    :return: list of tuples
    """
    return list(product(cooked_array, repeat=length_of_tuples_in_result))


def give_me_pairwise(some_array):
    """

    :param some_array:
    :param some_int:
    :return:
    """
    return list(pairwise(some_array))


def give_me_mutes(some_array, some_int):
    print(list(permutations(some_array, some_int)))

    # AB AC AD BA BC BD CA CB CD DA DB DC


# print('=======*******========')
# print(list(combinations(some_array, some_int)))
#
# # AB AC AD BC BD CD
#
# print(list(combinations_with_replacement(some_array, some_int)))
# print('=======*******========')
# AA AB AC AD BB BC BD CC CD DD
if __name__ == "__main__":
    my_array = ['A', 'B', 'C', 'D']
    my_int = 3

    def make_me_readable(func):
        def wrapper():
            print('===>>>>>>>===')
            func()
            print('----------------------------------------------------------------------------------------------')
        return wrapper


    @make_me_readable
    def example_1():
        example_result = give_me_all_combinations(my_array, my_int)
        print('array:', my_array, 'parameter integer:', my_int, '\n', \
              'function: give_me_all_combinations()\n', \
              'number of combinations', len(example_result), '\n', \
              'Result:\n', \
              example_result)


    def example_2():
        example_result = give_me_all_combinations(my_array)
        print('array:', my_array, 'parameter integer: default\n',
              'function: give_me_all_combinations()\n',
              'number of combinations', len(example_result), '\n',
              'Result:\n',
              example_result)

    def example_3():
        example_result = give_me_pairwise( ['A', 'B', 'C', 'D', 'E', 'z','x','y'])#my_array)
        print('array:', 'my_array', 'parameter integer: default\n',
              'function: give_me_pairwise()\n',
              'number of combinations', len(example_result), '\n',
              'Result:\n',
              example_result)

    #example_1()
    example_3()

    #print(dir(example_result))
