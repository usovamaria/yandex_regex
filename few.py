def checkEmail():
    import re
    # Компилируем все регулярные выражения
    domenPattern = re.compile('[a-z0-9_\-]+\.[a-z0-9_\-]+')
    namePattern = re.compile('[a-z0-9"\.\_\-\!\;\,]+')
    dots = re.compile('\.\.')

    email = input('Введите e-mail адрес: ')
    # выделим имя и доменную часть
    result = re.split('@', email);
    if len(result) != 2:
        print('E-mail введен некорректно.');
        return 1
    else:
        name = result[0];
        domen = result[1];

    # Проверим доменную часть
    # длина, допустимые символы, нет символа '-' в конце и в начале каждой части домена
    if (len(domen) <= 256) and (len(domen) >= 3) and (re.match(domenPattern, domen)):
        if re.match(domenPattern, domen).end() != len(domen):
            print('Неверно введен домен')
            return 1
        result = re.split('\.', domen)
        post = result[0]
        dom = result[1]
        if (post[0] == '-') or (post[len(post)-1] == '-') or (dom[0] == '-') or (dom[len(dom)-1] == '-'):
            print('Неверно введен домен')
            return 1
    else:
        print('Неверно введен домен')
        return 1
    # Проверим часть с именем
    # длина, допустимые символы, нет повторяющихся точек, четное кол-во кавычек
    if len(name) <= 128 and (re.match(namePattern, name).start() == 0) and (re.match(namePattern, name).end() == len(name)) \
            and (re.search('\.\.', name) == None) and (len(re.findall(r'"', name)) % 2 == 0):
            if len(re.findall(r'"', name)) == 0 and (len(re.findall(r'[!;,]+', name)) > 0):
                print('Недопустимые знаки в имени')
                return 1
            elif (len(re.findall(r'"', name)) > 0) and (re.match(r'[a-z0-9"\.\_\-]+\"[a-z0-9\"\.\_\-\!\;\,]*\"[a-z0-9"\.\_\-]+', name).end() != len(name)):
                print('Недопустимые знаки в имени')
                return 1
    else:
        print('Недопустимое имя')
        return 1
    print ('E-mail введен верно')
    return 0

checkEmail()
