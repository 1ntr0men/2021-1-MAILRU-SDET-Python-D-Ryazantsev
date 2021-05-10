def first_number():
    with open("../tests/access.log", "r") as f:
        return sum(1 for _ in f)


def second_number():
    req_type = {}
    with open("../tests/access.log", "r") as f:
        for line in f.readlines():
            req = line.split()[5].replace('"', '')
            if req not in req_type:
                req_type[req] = 1
            else:
                req_type[req] += 1
    return req_type


def third_number():
    req = {}
    with open("../tests/access.log", "r") as f:
        for line in f.readlines():
            url = line.split()[6]
            if url not in req:
                req[url] = 1
            else:
                req[url] += 1
    return sorted(req.items(), key=lambda i: i[1], reverse=True)[:10]


def fourth_number():
    urls = []
    with open("../tests/access.log", "r") as f:
        for line in f.readlines():
            l = line.split()
            if l[8][0] == "4":
                urls.append([l[6], l[8], l[9], l[0]])
    return sorted(urls, key=lambda i: int(i[2]), reverse=True)[:5]


def fifth_number():
    urls = []
    with open("../tests/access.log", "r") as f:
        for line in f.readlines():
            l = line.split()
            if l[8][0] == "5":
                if l[0] in [_[0] for _ in urls]:
                    for k in range(len(urls)):
                        if urls[k][0] == l[0]:
                            urls[k][1] += 1
                else:
                    urls.append([l[0], 1])
    return sorted(urls, key=lambda i: i[1], reverse=True)[:5]
