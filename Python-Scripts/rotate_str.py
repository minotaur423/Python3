def rotate_str(k, word):
    subword = ""
    if k > 0:
        subword = word[:k]
        result = word[k:] + subword
    else:
        subword = word[k:]
        result = subword + word[:k]
    return result

data = ([-6, "pxjlixoplhgsqifuio"], [-3, "aaraiiuvzifrirzyyi"], [-6, "exnclwieahfuyaeavtat"], [-6, "keoknhruejkhuafzonyqfyng"], [-4, "iamefraqihbomlg"], [1, "azdhytmybtmcuveaa"], [4, "tqcvmpasdaaeaefsqrkrfxuz"], [5, "hvkcjafiguyzyatwaronbmx"], [4, "ileaeeqohzjmyqbxjzxe"], [-2, "liqywdkglvdgziwippru"], [1, "ylxwjgixshikiluexjiecquka"])

for k, w in data:
    print(rotate_str(k, w), end=" ")