def is_valid(s: str) -> bool:
    char_dict = {"{": "}", "(": ")", "[": "]"}
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
                else:
                    mod_ = diff_in_index % 2
                    status.append(
                        diff_in_index % 2 == mod_
                        and s.index(char_dict[char]) % 2 == mod_
                    )

            except ValueError:
                # this means the bracket was never closed
                status.append(False)
    if all(status):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_valid(r")([]{}"))
