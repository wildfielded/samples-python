#!/usr/bin/python3

def bananas(in_str: str) -> set:
    ''' Returns all letters combinations that make up the word "banana" word
    from the letters in the initial string
    Arguments:
        in_str [int] -- Initial string
    Returns:
        [set] -- Set of strings (all variants)
    '''

''' =====----- MAIN -----===== '''
if __name__ == '__main__':
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                    "b-a--nana", "-banan--a", "b-ana--na",
                                    "b---anana", "-bana--na", "-ba--nana",
                                    "b-anan--a", "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",
                                   "b--anana", "banana--", "banan--a"}

#####=====----- THE END -----=====#########################################