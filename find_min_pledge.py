############
#
# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.
#
############


def find_min_pledge(pledge_list):
    """
    returns the minimum amount which has not been pledged yet
    :param pledge_list: the list of previously pledged amounts
    """
    assert max(pledge_list) < 1000000, "maximum pledged amount should be less than 1000000"
    assert len(pledge_list) < 100000, "number of pledges should be less than 10000"
    pledge_list_c = pledge_list.copy()
    pledge_list_c.sort()
    for x in pledge_list_c:
        if not x + 1 in pledge_list_c and x > 0:
            return x + 1
    return 1


assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1
