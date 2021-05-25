def summary(*args):
    total = sum(args)
    return total, max(args), min(args), total / len(args)

def q3():
    total, maxval, minval, avg = summary(80,75,90,95,85)
    print(total, maxval,minval, avg)

def q4():
    s = """
    we encourage everyone to contribute to Python
    If you still have questions after reviewing the material
    in this 
    """

    # wjdwp
    s = s.replace(",","").repalce(".","").replace("\n","").upper()
    splits = s.split()
    print("splits:", splits)

    summary = {}        # 결과 dict
    for word in splits:
        if word in summary.key():   # 이미 키에 있으면
            summary[word] += 1
        else:   # 키가 없으면
            summary[word] = 1




if __name__ == "__main__":
    q3()