from swiplserver import PrologThread


def find_brothers(prolog: PrologThread, person: str):
    query_str = f"brother(Brother, {person}, _)."
    result = prolog.query(query_str)

    if result:
        brothers = list(set([res['Brother'] for res in list(result)]))
        print(f"Братья {person}: {', '.join(brothers)}")
    else:
        print(f"У {person} нет братьев")


def find_sisters(prolog: PrologThread, person: str):
    query_str = f"sister(Sister, {person}, _)."
    result = prolog.query(query_str)

    if result:
        sisters = list(set([res['Sister'] for res in list(result)]))
        print(f"Сестры {person}: {', '.join(sisters)}")
    else:
        print(f"У {person} нет сестер")


def find_parents(prolog: PrologThread, person: str):
    query_str = f"parent(Parent, {person}, _)."
    result = prolog.query(query_str)

    if result:
        parents = list(set([res['Parent'] for res in list(result)]))
        print(f"Родители {person}: {', '.join(parents)}")
    else:
        print(f"У {person} нет известных родителей")


def find_children(prolog: PrologThread, person: str):
    query_str = f"parent({person}, Child, _)."
    result = prolog.query(query_str)

    if result:
        children = list(set([res['Child'] for res in list(result)]))
        print(f"Дети {person}: {', '.join(children)}")
    else:
        print(f"У {person} нет детей")


def find_wife(prolog: PrologThread, person: str):
    query_str = f"married({person}, Wife, _), female(Wife)."
    result = prolog.query(query_str)

    if result:
        wives = list(set([res['Wife'] for res in list(result)]))
        print(f"Жена(ы) {person}: {', '.join(wives)}")
    else:
        print(f"У {person} нет жены")


def find_husband(prolog: PrologThread, person: str):
    query_str = f"married({person}, Husband, _), male(Husband)."
    result = prolog.query(query_str)

    if result:
        husbands = list(set([res['Husband'] for res in list(result)]))
        print(f"Муж(ья) {person}: {', '.join(husbands)}")
    else:
        print(f"У {person} нет мужа")


def check_alive(prolog: PrologThread, person: str, year: int):
    query_str = f"alive({person}, {year})."
    result = prolog.query(query_str)

    if result:
        print(f"Да, {person} жив в {year} году")
    else:
        print(f"Нет, {person} не жив в {year} году")


def find_age_difference(prolog: PrologThread, person1: str, person2: str):
    query_str = f"age_difference({person1}, {person2}, Diff)."
    result = prolog.query(query_str)

    if result:
        diff = result[0]['Diff']
        print(f"Разница в возрасте между {person1} и {person2}: {diff} лет")
    else:
        print(f"Не удалось вычислить разницу в возрасте между {person1} и {person2}")


def find_ancestors(prolog: PrologThread, person: str):
    query_str = f"ancestor(Ancestor, {person})."
    result = prolog.query(query_str)

    if result:
        ancestors = list(set([res['Ancestor'] for res in list(result)]))
        print(f"Предки {person}: {', '.join(ancestors)}")
    else:
        print(f"У {person} нет известных предков")


def find_descendants(prolog: PrologThread, person: str):
    query_str = f"descendant(Descendant, {person})."
    result = prolog.query(query_str)

    if result:
        descendants = list(set([res['Descendant'] for res in list(result)]))
        print(f"Потомки {person}: {', '.join(descendants)}")
    else:
        print(f"У {person} нет известных потомков")


def check_bastard(prolog: PrologThread, person: str):
    query_str = f"bastard({person}, _)."
    result = prolog.query(query_str)

    if result:
        print(f"Да, {person} является бастардом")
    else:
        print(f"Нет, {person} не является бастардом")


def find_grandparents(prolog: PrologThread, person: str):
    query_str = f"grandparent(Grandparent, {person}, _)."
    result = prolog.query(query_str)

    if result:
        grandparents = list(set([res['Grandparent'] for res in list(result)]))
        print(f"Дедушки и бабушки {person}: {', '.join(grandparents)}")
    else:
        print(f"У {person} нет известных дедушек и бабушек")


def find_uncles_aunts(prolog: PrologThread, person: str):
    query_str = f"uncle_or_aunt(UncleAunt, {person}, _)."
    result = prolog.query(query_str)

    if result:
        uncles_aunts = list(set([res['UncleAunt'] for res in list(result)]))
        print(f"Дяди и тети {person}: {', '.join(uncles_aunts)}")
    else:
        print(f"У {person} нет известных дядей и тетей")


def find_nephews_nieces(prolog: PrologThread, person: str):
    query_str = f"nephew_or_niece(NephewNiece, {person}, _)."
    result = prolog.query(query_str)

    if result:
        nephews_nieces = list(set([res['NephewNiece'] for res in list(result)]))
        print(f"Племянники и племянницы {person}: {', '.join(nephews_nieces)}")
    else:
        print(f"У {person} нет известных племянников и племянниц")


def find_cousins(prolog: PrologThread, person: str):
    query_str = f"cousin(Cousin, {person}, _)."
    result = prolog.query(query_str)

    if result:
        cousins = list(set([res['Cousin'] for res in list(result)]))
        print(f"Двоюродные братья и сестры {person}: {', '.join(cousins)}")
    else:
        print(f"У {person} нет известных двоюродных братьев и сестер")


def find_mother(prolog: PrologThread, person: str):
    query_str = f"mother(Mother, {person}, _)."
    result = prolog.query(query_str)

    if result:
        mothers = list(set([res['Mother'] for res in list(result)]))
        print(f"Мать {person}: {', '.join(mothers)}")
    else:
        print(f"У {person} нет известной матери")


def find_father(prolog: PrologThread, person: str):
    query_str = f"father(Father, {person}, _)."
    result = prolog.query(query_str)

    if result:
        fathers = list(set([res['Father'] for res in list(result)]))
        print(f"Отец {person}: {', '.join(fathers)}")
    else:
        print(f"У {person} нет известного отца")


def find_widowed(prolog: PrologThread, year: int):
    query_str = f"widowed(Person, {year})."
    result = prolog.query(query_str)

    if result:
        widowed = list(set([res['Person'] for res in list(result)]))
        print(f"Вдовы и вдовцы в {year} году: {', '.join(widowed)}")
    else:
        print(f"В {year} году нет вдов и вдовцов")


def find_single_parents(prolog: PrologThread, year: int):
    query_str = f"single_parent(Person, {year})."
    result = prolog.query(query_str)

    if result:
        single_parents = list(set([res['Person'] for res in list(result)]))
        print(f"Одинокие родители в {year} году: {', '.join(single_parents)}")
    else:
        print(f"В {year} году нет одиноких родителей")


def find_orphans(prolog: PrologThread, year: int):
    query_str = f"orphan(Person, {year})."
    result = prolog.query(query_str)

    if result:
        orphans = list(set([res['Person'] for res in list(result)]))
        print(f"Сироты в {year} году: {', '.join(orphans)}")
    else:
        print(f"В {year} году нет сирот")


def find_lifespan(prolog: PrologThread, person: str):
    query_str = f"lifespan({person}, Years)."
    result = prolog.query(query_str)

    if result:
        years = result[0]['Years']
        print(f"Продолжительность жизни {person}: {years} лет")
    else:
        print(f"Не удалось определить продолжительность жизни {person}")


def check_older(prolog: PrologThread, person1: str, person2: str):
    query_str = f"older_than({person1}, {person2})."
    result = prolog.query(query_str)

    if result:
        print(f"{person1} старше {person2}")
    else:
        print(f"{person1} не старше {person2}")


def check_younger(prolog: PrologThread, person1: str, person2: str):
    query_str = f"younger_than({person1}, {person2})."
    result = prolog.query(query_str)

    if result:
        print(f"{person1} младше {person2}")
    else:
        print(f"{person1} не младше {person2}")
