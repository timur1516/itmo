% ############ ФАКТЫ #############

% ===== РОЖДЕНИЯ =====
birth(eddard_stark, 263).
birth(lyarra_stark, 240).
birth(edwyle_stark, 218).
birth(marna_locke, 222).
birth(catelyn_tully, 264).
birth(lysa_tully, 266).
birth(edmure_tully, 267).
birth(hoster_tully, 240).
birth(minisa_tully, 244).
birth(robb_stark, 283).
birth(sansa_stark, 286).
birth(arya_stark, 289).
birth(bran_stark, 290).
birth(rickon_stark, 295).
birth(john_snow, 283).
birth(benjen_stark, 265).
birth(lyanna_stark, 266).
birth(rickard_stark, 238).
birth(brandon_stark_sr, 262).
birth(jeyne_westerling, 284).
birth(rhaegar_targaryen, 259).
birth(aerys_targaryen, 244).
birth(rhaella_targaryen, 245).
birth(daenerys_targaryen, 284).
birth(viserys_targaryen, 276).
birth(cersei_lannister, 266).
birth(tyrion_lannister, 273).
birth(jaime_lannister, 266).
birth(tywin_lannister, 242).
birth(joanna_lannister, 245).

% ===== СМЕРТИ =====
death(eddard_stark, 299).
death(lyarra_stark, 266).       
death(edwyle_stark, 255).         
death(marna_locke, 260).       
death(catelyn_tully, 299).    
death(lysa_tully, 300).   
death(hoster_tully, 299).        
death(minisa_tully, 274).     
death(robb_stark, 299).      
death(rickon_stark, 303).       
death(john_snow, 303).            
death(benjen_stark, 298).
death(lyanna_stark, 283).
death(rickard_stark, 282).
death(brandon_stark_sr, 282).
death(rhaegar_targaryen, 283).
death(aerys_targaryen, 283).
death(rhaella_targaryen, 284).
death(viserys_targaryen, 298). 
death(tywin_lannister, 300).
death(joanna_lannister, 273).
death(jeyne_westerling, 299).

% ==== МУЖЧИНЫ ====
male(eddard_stark).
male(edwyle_stark).
male(rickard_stark).
male(brandon_stark_sr).
male(robb_stark).
male(bran_stark).
male(rickon_stark).
male(john_snow).
male(benjen_stark).
male(rhaegar_targaryen).
male(aerys_targaryen).
male(viserys_targaryen).
male(tyrion_lannister).
male(jaime_lannister).
male(tywin_lannister).
male(edmure_tully).
male(hoster_tully).

% ==== ЖЕНЩИНЫ ====
female(lyarra_stark).
female(marna_locke).
female(catelyn_tully).
female(lysa_tully).
female(minisa_tully).
female(sansa_stark).
female(arya_stark).
female(lyanna_stark).
female(jeyne_westerling).
female(rhaella_targaryen).
female(daenerys_targaryen).
female(cersei_lannister).
female(joanna_lannister).

% ===== БРАКИ =====
marriage_fact(edwyle_stark, marna_locke, 236).
marriage_fact(rickard_stark, lyarra_stark, 262). 
marriage_fact(hoster_tully, minisa_tully, 262).
marriage_fact(tywin_lannister, joanna_lannister, 263).
marriage_fact(aerys_targaryen, rhaella_targaryen, 259).
marriage_fact(eddard_stark, catelyn_tully, 282). 
marriage_fact(rhaegar_targaryen, lyanna_stark, 280).
marriage_fact(robb_stark, jeyne_westerling, 299).
marriage_fact(sansa_stark, tyrion_lannister, 299).

% ===== РОДИТЕЛИ =====
parent_fact(edwyle_stark, rickard_stark).
parent_fact(marna_locke, rickard_stark).

parent_fact(rickard_stark, brandon_stark_sr).
parent_fact(lyarra_stark, brandon_stark_sr).
parent_fact(rickard_stark, eddard_stark).
parent_fact(lyarra_stark, eddard_stark).
parent_fact(rickard_stark, benjen_stark).
parent_fact(lyarra_stark, benjen_stark).
parent_fact(rickard_stark, lyanna_stark).
parent_fact(lyarra_stark, lyanna_stark).

parent_fact(hoster_tully, catelyn_tully).
parent_fact(minisa_tully, catelyn_tully).
parent_fact(hoster_tully, lysa_tully).
parent_fact(minisa_tully, lysa_tully).
parent_fact(hoster_tully, edmure_tully).
parent_fact(minisa_tully, edmure_tully).

parent_fact(eddard_stark, robb_stark).
parent_fact(catelyn_tully, robb_stark).
parent_fact(eddard_stark, sansa_stark).
parent_fact(catelyn_tully, sansa_stark).
parent_fact(eddard_stark, arya_stark).
parent_fact(catelyn_tully, arya_stark).
parent_fact(eddard_stark, bran_stark).
parent_fact(catelyn_tully, bran_stark).
parent_fact(eddard_stark, rickon_stark).
parent_fact(catelyn_tully, rickon_stark).

parent_fact(rhaegar_targaryen, john_snow).
parent_fact(lyanna_stark, john_snow).

parent_fact(aerys_targaryen, rhaegar_targaryen).
parent_fact(rhaella_targaryen, rhaegar_targaryen).

parent_fact(aerys_targaryen, viserys_targaryen).
parent_fact(rhaella_targaryen, viserys_targaryen).

parent_fact(aerys_targaryen, daenerys_targaryen).
parent_fact(rhaella_targaryen, daenerys_targaryen).

parent_fact(tywin_lannister, jaime_lannister).
parent_fact(joanna_lannister, jaime_lannister).

parent_fact(tywin_lannister, cersei_lannister).
parent_fact(joanna_lannister, cersei_lannister).

parent_fact(tywin_lannister, tyrion_lannister).
parent_fact(joanna_lannister, tyrion_lannister).


% ############ ПРАВИЛА #############

% Мёртв
dead(Person, Year) :-
    death(Person, DeathYear),
    ( var(Year) -> true ; Year >= DeathYear ).

% Был рождён
was_born(Person, Year) :-
    birth(Person, BirthYear),
    ( var(Year) -> true ; Year >= BirthYear ).

% Жив
alive(Person, Year) :-
    was_born(Person, Year),
    ( var(Year) -> true ; \+ dead(Person, Year)).

% Факт женитьбы, без привязки к порядку
marriage(Person1, Person2, Year) :-
    marriage_fact(Person1, Person2, Year);
    marriage_fact(Person2, Person1, Year).

% Факт супрежества без привязки к жизни\смерти
spouses(Person1, Person2, Year) :-
    marriage(Person1, Person2, MarriageYear),
    ( var(Year) -> true ; Year >= MarriageYear ).

% Состоит в браке
married(Person1, Person2, Year) :-
    spouses(Person1, Person2, Year),
    alive(Person1, Year),
    alive(Person2, Year).

% Муж
husband(Person, Year) :-
    male(Person),
    married(Person, _, Year).

% Жена
wife(Person, Year) :-
    female(Person),
    married(Person, _, Year).

% Вдовец/вдова
widowed(Person, Year) :-
    spouses(Person, Spouse, Year),
    alive(Person, Year),
    dead(Spouse, Year).

% Вдова
widow(Person, Year) :-
    female(Person),
    widowed(Person, Year).

% Вдовец
widower(Person, Year) :-
    male(Person),
    widowed(Person, Year).

% Родитель
parent(Parent, Child, Year) :-
    parent_fact(Parent, Child),
    was_born(Child, Year).

% Одинокий родитель
single_parent(Parent, Year) :-
    parent(Parent, _, Year),
    widowed(Parent, Year).

% Мать
mother(Mother, Child, Year) :-
    female(Mother),
    parent(Mother, Child, Year).

% Отец
father(Father, Child, Year) :-
    male(Father),
    parent(Father, Child, Year).

% Сирота
% Только если он жив, несовершеннолетний, у него были родители, но в данный момент они мертвы
orphan(Person, Year) :-
    findall(Parent, parent_fact(Parent, Person), Parents),
    Parents \= [],
    forall(member(P, Parents), dead(P, Year)),
    alive(Person, Year),
    birth(Person, BirthYear),
    (Year - BirthYear) < 18.

% Брат/сестра
sibling(Sibling1, Sibling2, Year) :-
    parent(Parent, Sibling1, Year),
    parent(Parent, Sibling2, Year),
    Sibling1 \= Sibling2,
    was_born(Sibling1, Year),
    was_born(Sibling2, Year).
    

% Брат
brother(Brother, Person, Year) :-
    male(Brother),
    sibling(Brother, Person, Year).

% Сестра
sister(Sister, Person, Year) :-
    female(Sister),
    sibling(Sister, Person, Year).

% Дедушка/бабушка
grandparent(Grandparent, Grandchild, Year) :-
    parent(Grandparent, Parent, Year),
    parent(Parent, Grandchild, Year),
    was_born(Grandchild, Year).

% Бабушка
grandmother(Grandmother, Grandchild, Year) :-
    female(Grandmother),
    grandparent(Grandmother, Grandchild, Year).

% Дедушка
grandfather(Grandfather, Grandchild, Year) :-
    male(Grandfather),
    grandparent(Grandfather, Grandchild, Year).

% Дядя/тётя
uncle_or_aunt(UncleAunt, NephewNiece, Year) :-
    sibling(UncleAunt, Parent, Year),
    parent(Parent, NephewNiece, Year).

% Дядя
uncle(Uncle, NephewNiece, Year) :-
    male(Uncle),
    uncle_or_aunt(Uncle, NephewNiece, Year).

% Тётя
aunt(Aunt, NephewNiece, Year) :-
    female(Aunt),
    uncle_or_aunt(Aunt, NephewNiece, Year).

% Племянник/племянница
nephew_or_niece(NephewNiece, UncleAunt, Year) :-
    uncle_or_aunt(UncleAunt, NephewNiece, Year).

% Племянник
nephew(Nephew, UncleAunt, Year) :-
    male(Nephew),
    nephew_or_niece(Nephew, UncleAunt, Year).

% Племянница
niece(Niece, UncleAunt, Year) :-
    female(Niece),
    nephew_or_niece(Niece, UncleAunt, Year).

% Двоюродный брат/сестра
cousin(Person1, Person2, Year) :- 
    parent(Parent1, Person1, Year),
    parent(Parent2, Person2, Year),
    sibling(Parent1, Parent2, Year),
    Person1 \= Person2,
    was_born(Person1, Year),
    was_born(Person2, Year).

% Бастард
bastard(Person, Year) :-
    birth(Person, BirthYear),
    father(Father, Person, Year),
    mother(Mother, Person, Year),
    \+ spouses(Father, Mother, BirthYear).

% Предок
ancestor(Ancestor, Descendant) :-
    parent_fact(Ancestor, Descendant).
ancestor(Ancestor, Descendant) :-
    parent_fact(Ancestor, X),
    ancestor(X, Descendant).

% Потомок
descendant(Descendant, Ancestor) :-
    ancestor(Ancestor, Descendant).

% Старше ли один другого
older_than(P1, P2) :-
    birth(P1, Y1),
    birth(P2, Y2),
    Y1 < Y2.

% Младше ли один другого
younger_than(P1, P2) :-
    birth(P1, Y1),
    birth(P2, Y2),
    Y1 > Y2.

% Разница в возрасте
age_difference(P1, P2, Diff) :-
    birth(P1, Y1),
    birth(P2, Y2),
    Diff is abs(Y1 - Y2).

% Продолжительность жизни
lifespan(Person, Years) :-
    birth(Person, Y1),
    death(Person, Y2),
    Years is Y2 - Y1.