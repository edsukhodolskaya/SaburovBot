import urllib.request
import re
import locale

class Saburov_concert(object):

    def __init__(self, date_saburov, seats_left, cost):
        """Constructor"""
        self.date_saburov = date_saburov
        self.seats_left = seats_left
        self.cost = cost

    def string_representation(self):
        return "На " + str(self.date_saburov) + ", шоу Сабурова за " + str(self.cost) + "руб,  осталось " + str(self.seats_left) + " мест."

locale.setlocale(locale.LC_ALL, '')
base_url = 'https://standupstore.ru/page/'
img = re.compile('uploads/2019/03/e508ee6b-ac1e-4d96-a1b9-54d88ec2b6a3.jpg')
date = re.compile("\d{1,2}\s[а-яА-Я]{3,8}\,\s[1-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")
saburov_concerts = []
unique_dates = set()
any_adv = "data-id"
i = 1

while(True):
    url = base_url + str(i)
    with urllib.request.urlopen(url) as response:
       page = response.read().decode()
       if page.find(any_adv) == -1:
           break
       idxs = [el.start() for el in re.finditer(img, page)]
       for idx in idxs:
           page = page[:idx]
           page = page[page.rfind("data-date"):]
           date_saburov = re.search(date, page).group(0)
           cost = page[page.find("data-cost") + len("data-cost=\""):page.find("data-id") - len("\" ")]
           seats = int(page[page.find("data-seats") + len("data-seats=\""):page.find(">") - len(" >")])
           if date_saburov not in unique_dates:
               saburov_concerts.append(Saburov_concert(date_saburov, seats, cost))
               unique_dates.add(date_saburov)
       i += 1


