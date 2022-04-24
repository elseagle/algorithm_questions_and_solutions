def is_valid(s: str) -> bool:
    char_dict = {"{": "}", "(": ")", "[": "]"}
    char_dict_inverse = dict(zip(char_dict.values(), char_dict.keys()))
    status = []
    for char in s:
        if char in char_dict.keys():
            try:
                """the differnce between the index of brackets 
                will always be eith both even or both odd"""
                
                diff_in_index = s.index(char_dict[char]) - s.index(char)
                
                """if it's -ve, it means the closing bracket
                 comes before the opening bracket"""
                 
                if diff_in_index < 0:
                    status.append(False)
                    continue
                elif diff_in_index == 1:
                    status.append(True)
                    continue
                else:
                    mod_ = diff_in_index % 2
                    
                    status.append(
                        diff_in_index % 2 == mod_
                        and s.index(char_dict[char]) % 2 == mod_
                    )
            except ValueError:
                # this means the bracket was never closed
                status.append(False)
        # this is to handle cases where there are no opening brackets
        elif  char_dict_inverse.get(char) not in s:
            status.append(False)

    if all(status):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_valid(r")([]{}"))
    print(is_valid(r"(([]{}"))
    print(is_valid(r"[()]{}"))
    print(is_valid(r"[]{}()"))
    print(is_valid(r"[]{()}"))
    print(is_valid(r"([]{})"))
    print(is_valid(r"([]})"))
    print(is_valid(r"[]{)(}"))

