--creating domains
CREATE DOMAIN positive_integer AS integer
CHECK(VALUE > 0);

CREATE DOMAIN percentage AS decimal
CHECK(VALUE >= 0 AND VALUE <= 100);

--creating tables
CREATE TABLE IF NOT EXISTS Тип_сущности (
	ИД serial PRIMARY KEY,
	ТИП text UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Объект(
 ИД serial PRIMARY KEY,
 ТИП_СУЩНОСТИ integer REFERENCES Тип_сущности(ИД) NOT NULL,
 ИМЯ text
);

CREATE TABLE IF NOT EXISTS Группа_людей(
  ИД serial PRIMARY KEY,
  КОЛИЧЕСТВО_УЧАСТНИКОВ positive_integer NOT NULL,
  ОПИСАНИЕ text,
  ИД_ОБЪЕКТА integer REFERENCES Объект(ИД) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Температура(
  ИД serial PRIMARY KEY,
  ЗНАЧЕНИЕ decimal UNIQUE NOT NULL,
  ОПИСАНИЕ text NOT NULL,
  КОНТРАСТНОСТЬ percentage NOT NULL
);

CREATE TABLE IF NOT EXISTS Запах(
  ИД serial PRIMARY KEY,
  ЕДКОСТЬ percentage NOT NULL,
  НЕВЫНОСИМОСТЬ percentage NOT NULL,
  UNIQUE(ЕДКОСТЬ, НЕВЫНОСИМОСТЬ)
);

CREATE TABLE IF NOT EXISTS Координаты(
  ИД serial PRIMARY KEY,
  КООРДИНАТА_X decimal NOT NULL,
  КООРДИНАТА_Y decimal NOT NULL,
  КООРДИНАТА_Z decimal NOT NULL,
  ОПИСАНИЕ text,
  UNIQUE(КООРДИНАТА_X, КООРДИНАТА_Y, КООРДИНАТА_Z)
);

CREATE TABLE IF NOT EXISTS Нахождение_сущности(
  ИД serial PRIMARY KEY,
  ОБЪЕКТ_СУЩНОСТИ integer REFERENCES Объект(ИД) NOT NULL,
  ОБЪЕКТ_МЕСТА integer REFERENCES Объект(ИД),
  КООРДИНАТЫ integer REFERENCES Координаты(ИД),
  ВРЕМЯ_НАЧАЛА timestamp DEFAULT NOW() NOT NULL,
  CHECK ((ОБЪЕКТ_МЕСТА IS NOT NULL) OR (КООРДИНАТЫ IS NOT NULL)),
  CHECK (ОБЪЕКТ_СУЩНОСТИ != ОБЪЕКТ_МЕСТА)
);

CREATE TABLE IF NOT EXISTS Ощущениея(
  ЗАПАХ integer REFERENCES Запах(ИД),
  ТЕМПЕРАТУРА integer REFERENCES Температура(ИД),
  НАХОЖДЕНИЕ integer REFERENCES Нахождение_сущности(ИД),
  PRIMARY KEY (ЗАПАХ, ТЕМПЕРАТУРА, НАХОЖДЕНИЕ)
);

CREATE TABLE IF NOT EXISTS Лагерь(
  ИД serial PRIMARY KEY,
  ЛОКАЦИЯ integer REFERENCES Координаты(ИД) UNIQUE NOT NULL,
  ИД_ОБЪЕКТА integer REFERENCES Объект(ИД) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Вещь(
  ИД serial PRIMARY KEY,
  ВИД text NOT NULL,
  МАТЕРИАЛ text NOT NULL,
  ВЛАДЕЛЕЦ integer REFERENCES Лагерь(ИД) NOT NULL,
  ИД_ОБЪЕКТА integer REFERENCES Объект(ИД) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Подземный_ход(
  ИД serial PRIMARY KEY,
  ТИП text NOT NULL,
  КООРДИНАТЫ_НАЧАЛА integer REFERENCES Координаты(ИД) NOT NULL,
  КООРДИНАТЫ_КОНЦА integer REFERENCES Координаты(ИД) NOT NULL,
  CHECK (КООРДИНАТЫ_НАЧАЛА != КООРДИНАТЫ_КОНЦА),
  ИД_ОБЪЕКТА integer REFERENCES Объект(ИД) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Соединение_ходов (
  ПОДЗЕМНЫЙ_ХОД_1 integer REFERENCES Подземный_ход(ИД),
  ПОДЗЕМНЫЙ_ХОД_2 integer REFERENCES Подземный_ход(ИД),
  CHECK (ПОДЗЕМНЫЙ_ХОД_1 < ПОДЗЕМНЫЙ_ХОД_2),
  PRIMARY KEY (ПОДЗЕМНЫЙ_ХОД_1, ПОДЗЕМНЫЙ_ХОД_2)
);