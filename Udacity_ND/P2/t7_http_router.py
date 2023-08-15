from collections import defaultdict


class RouteTrieNode():
    """
    RouteTrieNode to store the handler and children.
    """

    def __init__(self, handler_str=None):
        """
        Initialize the node with children as a dictionary and handler as None.

        :param handler_str: handler string
        :type handler_str: str
        """
        self.handler = handler_str
        self.children = defaultdict(RouteTrieNode)


class RouteTrie():
    """
    Route Trie for storing HTTP routes in a trie structure.
    """

    def __init__(self, root_handler_str):
        """
        Initialize the trie with an root node and a handler, this is the root path or home page node.

        :param root_handler_str: root handler string
        :type root_handler_str: str
        """
        self.root = RouteTrieNode(root_handler_str)

    def add(self, path_list, handler_str=None):
        """
        Add a handler to the trie from a path list and handler string.

        :param path_list: path list
        :type path_list: list of strings
        :param handler_str: handler string
        :type handler_str: str
        """
        cur_node = self.root
        for directory in path_list:
            cur_node = cur_node.children[directory]
        cur_node.handler = handler_str

    def find(self, path_list):
        """
        Check if a path exists in the trie and has a handler.

        :param path_list: path list
        :type path_list: list of strings
        :return: handler string
        :rtype: str
        """
        cur_node = self.root
        if len(path_list) == 1:
            return self.root.handler
        for directory in path_list:
            if directory not in cur_node.children:
                return None
            else:
                cur_node = cur_node.children[directory]
        return cur_node.handler


class Router:
    """
    A Router class to wrap the Trie and its interfaces.
    """

    def __init__(self, root_handler_str, not_found_handler_str):
        """
        Initialize the Router with a RouteTrie for holding routes and their handlers.

        :param root_handler_str: root handler string
        :type root_handler_str: str
        :param not_found_handler_str: not found handler string
        :type not_found_handler_str: str
        """
        self.router = RouteTrie(root_handler_str)
        self.not_found_handler = not_found_handler_str

    def add_handler(self, path, handler_str):
        """
        Add a handler for a path to the existing routes.

        :param path: path string
        :type path: str
        :param handler_str: handler string
        :type handler_str: str
        """
        self.router.add(self._split_path(path), handler_str)

    def lookup(self, path):
        """
        Search for a route and return the handler if found, otherwise return the "not found" handler.

        :param path: path string
        :type path: str
        :return: handler string
        :rtype: str
        """
        handler = self.router.find(self._split_path(path))
        return self.not_found_handler if handler is None else handler

    def _split_path(self, path):
        """
        Split the path into a list of directories.

        :param path: path string
        :type path: str
        :return: list of directories
        :rtype: list of strings
        """
        return path.rstrip('/').split('/')

## Here are some test cases and expected outputs you can use to test your implementation


## create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
