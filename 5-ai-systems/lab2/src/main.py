import os
import re

from swiplserver import PrologMQI, create_posix_path

import queries

KNOWLEDGE_BASE_PATH = "../prolog/main.pl"

requests = [
    "Кто братья john_snow?",
    "Кто сестры sansa_stark?",
    "Кто родители eddard_stark?",
    "Кто дети tywin_lannister?",
    "Кто жена eddard_stark?",
    "Кто муж cersei_lannister?",
    "Жив ли eddard_stark в 298 году?",
    "Какая разница в возрасте между eddard_stark и tyrion_lannister?",
    "Кто предки daenerys_targaryen?",
    "Кто потомки rickard_stark?",
    "Является ли john_snow бастардом?",
    "Кто дедушки и бабушки arya_stark?",
    "Кто дяди и тети robb_stark?",
    "Кто племянники и племянницы tywin_lannister?",
    "Кто двоюродные братья и сестры daenerys_targaryen?",
    "Кто мать john_snow?",
    "Кто отец john_snow?",
    "Кто вдовы в 299 году?",
    "Кто одинокие родители в 298 году?",
    "Кто сироты в 300 году?",
    "Какова продолжительность жизни eddard_stark?",
    "Кто старше: eddard_stark или tywin_lannister?",
    "Кто младше: arya_stark или bran_stark?",
]

patterns = {
    r"Кто братья (.+)\?": lambda prolog, person: queries.find_brothers(prolog, person),
    r"Кто сестры (.+)\?": lambda prolog, person: queries.find_sisters(prolog, person),
    r"Кто родители (.+)\?": lambda prolog, person: queries.find_parents(prolog, person),
    r"Кто дети (.+)\?": lambda prolog, person: queries.find_children(prolog, person),
    r"Кто жена (.+)\?": lambda prolog, person: queries.find_wife(prolog, person),
    r"Кто муж (.+)\?": lambda prolog, person: queries.find_husband(prolog, person),
    r"Жив ли (.+) в (.+) году\?": lambda prolog, person, year: queries.check_alive(prolog, person, int(year)),
    r"Какая разница в возрасте между (.+) и (.+)\?": lambda prolog, person1, person2: queries.find_age_difference(
        prolog, person1, person2),
    r"Кто предки (.+)\?": lambda prolog, person: queries.find_ancestors(prolog, person),
    r"Кто потомки (.+)\?": lambda prolog, person: queries.find_descendants(prolog, person),
    r"Является ли (.+) бастардом\?": lambda prolog, person: queries.check_bastard(prolog, person),
    r"Кто дедушки и бабушки (.+)\?": lambda prolog, person: queries.find_grandparents(prolog, person),
    r"Кто дяди и тети (.+)\?": lambda prolog, person: queries.find_uncles_aunts(prolog, person),
    r"Кто племянники и племянницы (.+)\?": lambda prolog, person: queries.find_nephews_nieces(prolog, person),
    r"Кто двоюродные братья и сестры (.+)\?": lambda prolog, person: queries.find_cousins(prolog, person),
    r"Кто мать (.+)\?": lambda prolog, person: queries.find_mother(prolog, person),
    r"Кто отец (.+)\?": lambda prolog, person: queries.find_father(prolog, person),
    r"Кто вдовы в (.+) году\?": lambda prolog, year: queries.find_widowed(prolog, int(year)),
    r"Кто одинокие родители в (.+) году\?": lambda prolog, year: queries.find_single_parents(prolog, int(year)),
    r"Кто сироты в (.+) году\?": lambda prolog, year: queries.find_orphans(prolog, int(year)),
    r"Какова продолжительность жизни (.+)\?": lambda prolog, person: queries.find_lifespan(prolog, person),
    r"Кто старше: (.+) или (.+)\?": lambda prolog, person1, person2: queries.check_older(prolog, person1, person2),
    r"Кто младше: (.+) или (.+)\?": lambda prolog, person1, person2: queries.check_younger(prolog, person1, person2),
}


def main():
    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog:
            path = create_posix_path(KNOWLEDGE_BASE_PATH)

            prolog.query(f'consult("{path}")')
            print("База знаний успешно загружена")

            print("\nПримеры доступных запросов:")
            for request in requests:
                print(f" * {request}")
            print("\nДля выхода введите: exit")

            while True:
                query = input("$ ")
                if query.lower() == "exit":
                    break

                matched = False
                for pattern in patterns:
                    match = re.match(pattern, query, re.IGNORECASE)

                    if match is None:
                        continue

                    patterns[pattern](prolog, *match.groups())
                    matched = True
                    break

                if not matched:
                    print("Некорректный запрос")


if __name__ == "__main__":
    main()
