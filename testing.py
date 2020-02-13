alpha = 'abcdefghijklmnopqrstuvwxyz'
given = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_letter = ""
old_letter = ""
mid_letter = 0
for i in range(len(given)):
    if given[i].isalpha():
        old_letter = given[i]
        mid_letter = alpha.index(old_letter)
        if mid_letter == 24:
            new_letter = alpha[0]
        elif mid_letter == 25:
            new_letter = alpha[1]
        else:
            new_letter = alpha[mid_letter+2]
        print(new_letter, end="")
    else:
        print(given[i], end="")

