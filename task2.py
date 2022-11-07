def get_count_char(str_):

    str_ = str_.split()
    str_ = "".join(str_)
    str_ = str_.lower()

    dic_ = {}

    for index in str_:
        if index.isalpha():
                if index not in dic_:
                    dic_[index] = 1
                else:
                    dic_[index] += 1
    return dic_

def dictionary(dict_):
    new_dict = dict_.copy()
    sum_ = sum(dict_.values())
    for item in dict_:
        new_dict[key] = (new_dict[key] / sum_) * 100
    return dict_

main_str = """
    Данное предложение будет рxазбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
