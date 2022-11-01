from itertools import product,permutations,combinations,combinations_with_replacement


def give_me_all_combinations(cooked_array, length_of_end_tuple=2):
    """
    create all combinations
    :param cooked_array: origin array for combination creating
    :param length_of_end_tuple: itself
    :return: list of tuples
    """
    return list(product(cooked_array, repeat=length_of_end_tuple))

    # AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
def give_me_pairwise (some_array, some_int):

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
    print('=======*******========')
    example_result = give_me_all_combinations(my_array, my_int)
    print('array:', my_array, 'parameter integer:', my_int,'\n',\
          'function: give_me_all_combinations()\n',\
          'number of combinations', len(example_result),'\n',\
          'Result:\n',\
           example_result)
    print('=======*******========')
    print('=======*******========')
    example_result = give_me_all_combinations(my_array)
    print('array:', my_array, 'parameter integer:', my_int,'\n',\
          'function: give_me_all_combinations()\n',\
          'number of combinations', len(example_result),'\n',\
          'Result:\n',\
           example_result)
    print('=======*******========')