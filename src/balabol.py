import secrets
from collections import Counter

class balabol:
    def __init__(self):
        self.data = []
        self.filter = []
        self.suc_filtred = 0
    def learn(self, base):
        base2 = base.strip().split()
        if len(base2) > secrets.randbelow(2) + 1:
            i = secrets.randbelow(len(base2))
            j = secrets.randbelow(len(base2))
            start, end = sorted([i, j])
            for word in base2[start:end+1]:
                word = str(word)
                if word not in self.data:
                    self.data.append(word)
        else:
            base = str(base)
            if base not in self.data:
                    self.data.append(base)
    def generate(self, message="", tokenize=10, minimal_r=10, max_rai_input=20, minimal_rai_input=10, noremember=False, morelearn=False, raitingchars="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?/~` \"\"\\/", custom_data=None, usefilter=True, filtermemory=20):
        most_common_text = ""
        if usefilter:
            if len(self.filter) > 0:
                counter = Counter(self.filter)
                most_common_text = counter.most_common()
            if len(self.filter) > filtermemory:
                self.filter = self.filter[-filtermemory:]
        if not noremember and not morelearn and custom_data is None:
            self.learn(message)
        if custom_data is None:
            customdata = self.data
        else:
            customdata = [str(item) for item in custom_data]
        if len(customdata) == 0:
            return "Я ещё ничего не знаю! Научи меня через функцию learn."
        special_chars = raitingchars
        raiting_tabel = {
	        char: secrets.randbelow(max_rai_input) + minimal_rai_input
	        for char in special_chars
	    }
        total = 0
        rai_tabel2 = {}
        total2 = []
        for char in message:
            if char in raiting_tabel:
                total2.append(raiting_tabel[char])
        total_old = total
        result = []
        tabel_for_regeneration = []
        total2 = sorted(total2)
        if len(total2) >= 3:
            if len(total2) % 2 == 0:
                temp = []
                temp.append(round(len(total2) / 2))
                temp.append(round((len(total2) / 2) + 1))
                total = ((total2[temp[0]] + total2[temp[1]]) / 2)
            else:
                total = total2[round((len(total2) + 1) / 2)]
        i = (secrets.randbelow(len(customdata) - 1) + tokenize) % len(customdata) - 2
        for word in customdata[i:]:
            for i in word:
                if i in raiting_tabel:
                    total += raiting_tabel[i]
                if total >= minimal_r:
                    if word not in rai_tabel2:
                        rai_tabel2[word] = total
                    total = total_old
                    if word not in result and len(result) != tokenize:
                        if not morelearn:
                            result.append(word)
                            if secrets.randbelow(100) < 10 and custom_data is None:
                                i = secrets.randbelow(len(result))
                                j = secrets.randbelow(len(result))
                                start, end = sorted([i, j])
                                result2 = " ".join(result[start:end+1])
                                i = secrets.randbelow(len(self.data))
                                result2 = result2 + " " + self.data[i]
                                self.learn(result2)
                        else:
                            if custom_data is None:
                                result.append(word)
                                i = secrets.randbelow(len(result))
                                j = secrets.randbelow(len(result))
                                start, end = sorted([i, j])
                                result2 = " ".join(result[start:end+1])
                                i = secrets.randbelow(len(self.data))
                                result2 = result2 + " " + self.data[i]
                                self.learn(result2)
                    else:
                        break
                else:
                    if word not in rai_tabel2:
                        rai_tabel2[word] = total
                    total = total_old
        if secrets.randbelow(10) == 5 and len(message) > 0 and not morelearn:
            for i in range(len(result) - 1):
                if (len(result[i]) + rai_tabel2[result[i]]) < (len(result[i+1]) + rai_tabel2[result[i+1]]):
                    if secrets.randbelow(100) < 50:
                        tabel_for_regeneration.append(i)
            if len(tabel_for_regeneration) > 2:
                new_words = []
                for i in rai_tabel2:
                    ii = rai_tabel2[i] + tabel_for_regeneration[secrets.randbelow(len(tabel_for_regeneration))]
                    if ii >= minimal_r:
                        if i not in new_words and i not in result:
                            if len(new_words) != len(tabel_for_regeneration):
                                new_words.append(i)
                            else:
                                break
                for i in tabel_for_regeneration:
                    for n in range(len(new_words)):
                        if i not in result:
                            result[i] = new_words[n]
        if usefilter and custom_data is None:
            for i in most_common_text:
                if i[1] > 1:
                    tmp = len(result)
                    result = [text for text in result if text != i[0]]
                    self.suc_filtred += tmp - len(result)
            for i in result:
                self.filter.append(i)
        if not morelearn:
            return " ".join(result)
        else:
            return ""
