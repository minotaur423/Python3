def xyz_there(str):
    result = bool
    s_len = len(str)
    if s_len > 0:
        for i in range(s_len):
            if 'xyz' == str[i:i+4:]:
                result = True
            else:
                result = False
    else:
        result = False
    return result

print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
