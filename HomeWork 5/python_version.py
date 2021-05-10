import argparse
import json

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-j", "--json", action="store_true", help="json output")
j = parser.parse_args().json


def count_of_strings():
    with open("access.log", "r") as f:
        return sum(1 for _ in f)


def count_of_get_etc():
    req_type = {}
    with open("access.log", "r") as f:
        for line in f.readlines():
            req = line.split()[5].replace('"', '')
            if req not in req_type:
                req_type[req] = 1
            else:
                req_type[req] += 1
    return req_type


def top_ten_requests():
    req = {}
    with open("access.log", "r") as f:
        for line in f.readlines():
            url = line.split()[6]
            if url not in req:
                req[url] = 1
            else:
                req[url] += 1
    return sorted(req.items(), key=lambda i: i[1], reverse=True)[:10]


def top_five_400():
    urls = []
    with open("access.log", "r") as f:
        for line in f.readlines():
            l = line.split()
            if l[8][0] == "4":
                urls.append([l[6], l[8], l[9], l[0]])
    return sorted(urls, key=lambda i: int(i[2]), reverse=True)[:5]


def top_five_500():
    urls = []
    with open("access.log", "r") as f:
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


print(count_of_strings())
print(count_of_get_etc())
print(top_ten_requests())
print(*top_five_400())
print(*top_five_500())

if j:
    jsonData = json.dumps(
        {"First number": count_of_strings(),
         "Second number": count_of_get_etc(),
         "Third number": top_ten_requests(),
         "Four number": top_five_400(),
         "Five number": top_five_500()})
    with open("data.json", "w", encoding="utf-8") as file:
        file.write(jsonData)
