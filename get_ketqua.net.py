__doc__ = """
Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Dạng của câu lệnh::

  ketqua.py [NUMBER1] [NUMBER2] [...]
"""

def get_result_number():
    import requests
    import bs4

    list_result_numbers = []
    r = requests.get("http://ketqua.net")
    tree = bs4.BeautifulSoup(markup=r.text, features="lxml")

    jackpot = tree.find(name="div", attrs={"id": "rs_0_0"})
    list_result_numbers.append(jackpot.text)

    others_result_numbers1 = tree.find_all(
        name="div", attrs={"class": "phoi-size chu22 gray need_blank vietdam hover"}
    )
    others_result_numbers2 = tree.find_all(
        name="div",
        attrs={"class": "phoi-size chu22 gray need_blank vietdam border-right hover"},
    )
    others_result_numbers3 = tree.find_all(
        name="div",
        attrs={
            "class": "phoi-size chu22 gray need_blank vietdam border-bottom border-right hover"
        },
    )
    others_result_numbers4 = tree.find_all(
        name="div",
        attrs={"class": "phoi-size chu22 gray need_blank vietdam border-bottom hover"},
    )
    others_result_numbers = (
        others_result_numbers1
        + others_result_numbers2
        + others_result_numbers3
        + others_result_numbers4
    )
    for i in others_result_numbers:
        list_result_numbers.append(i.text)
    return list_result_numbers


def check_prizes(*args):
    result = ""
    for number in args:
        for result_number in get_result_number():
            if number == result_number[-2:]:
                result += "You are winner with number {}\n".format(number)
    if result == "":
        return "You are loser"
    else:
        return result.strip("\n")


def main():
    import sys

    args = [sys.argv[i] for i in range(1, len(sys.argv))]
    if len(sys.argv) == 1:
        print("List result numbers: {}".format(" ".join(get_result_number())))
    else:
        print(check_prizes(*args))


if __name__ == "__main__":
    main()
