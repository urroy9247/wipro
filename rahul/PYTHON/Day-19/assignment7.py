def is_isomorphic(s1, s2):
    
    if len(s1) != len(s2):

        return False

    map_s1_to_s2 = {}

    map_s2_to_s1 = {}
 
    for c1, c2 in zip(s1, s2):

        if c1 in map_s1_to_s2:

            if map_s1_to_s2[c1] != c2:

                return False

        else:

            map_s1_to_s2[c1] = c2
 
        if c2 in map_s2_to_s1:

            if map_s2_to_s1[c2] != c1:

                return False

        else:

            map_s2_to_s1[c2] = c1
 
    return True
 
# Example usage

s1 = "egg"

s2 = "add"

print(is_isomorphic(s1, s2))  # Output: True
 
s1 = "foo"

s2 = "bar"

print(is_isomorphic(s1, s2))  # Output: False