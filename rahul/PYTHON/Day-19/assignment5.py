def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

# Example usage
s1 = "abcd"
s2 = "cdab"
 
print(is_rotation(s1, s2))  # Output: True