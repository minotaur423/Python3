def parity_ctl(code):
    # Define variables
    bits = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = []
    set_bits = 0
    test_code = code
    letter = ""
    # Translate decimal code integer to binary
    for b in bits:
        if code >= b:
            binary.append(1)
            code -= b
        else:
            binary.append(0)
    # Count the number of set bits 
    set_bits = binary.count(1)
    if set_bits % 2 == 0:
        # Remove the parity bit to get the new ASCII integer
        if test_code not in range(32, 127):
            test_code = test_code - 128
            letter = chr(test_code)
        else:
            letter = chr(test_code)
    else:
        exit
    return letter

data = (152, 65, 41, 210, 114, 246, 168, 120, 160, 57, 239, 160, 160, 32, 101, 89, 216, 213, 112, 210, 177, 227, 226, 64, 228, 250, 42, 70, 232, 76, 250, 204, 210, 68, 209, 215, 106, 160, 69, 61, 120, 97, 53, 111, 69, 80, 52, 160, 237, 234, 113, 216, 78, 72, 65, 195, 232, 66, 91, 232, 209, 160, 246, 77, 240, 184, 115, 48, 160, 215, 168, 210, 113, 160, 232, 66, 148, 102, 228, 84, 251, 99, 224, 102, 204, 183, 243, 198, 106, 109, 225, 181, 65, 243, 248, 99, 57, 48, 128, 210, 46)
for a in data:
    print(parity_ctl(a), end="")