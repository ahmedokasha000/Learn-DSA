class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    
    :param user: user name/id.
    :type user: str.
    :param group: group to check user membership against.
    :type group: Group.
    """
    result = False
    if user in group.users:
        result = True
    else:
        for sub_group in group.groups:
            result = is_user_in_group(user, sub_group)
            if result is True:
                break
    return result


def test_cases():

    # Test Case 1, user in the second child group
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    assert is_user_in_group("sub_child_user", parent), "Test 1 failed."
    print("Test 1 passed.")

    # Test Case 2, user doesn't exist
    parent = Group("parent")
    assert is_user_in_group("sub_child_user2", parent) == False, "Test 2 failed."
    print("Test 2 passed.")

    # Test Case 3, user in the parent group
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)
    assert is_user_in_group("sub_child_user", parent), "Test 3 failed."
    print("Test 3 passed.")


def main():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    print(f"result = {is_user_in_group('sub_child_user', parent)}")
    test_cases()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
