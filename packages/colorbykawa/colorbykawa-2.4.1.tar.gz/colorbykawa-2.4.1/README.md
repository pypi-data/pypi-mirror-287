ColorbyKawa

colorbykawa — это библиотека для окрашивания текста в терминале с использованием ANSI-цветов. Библиотека предоставляет класс Color, который содержит константы для различных цветов.

## Установка

Для установки библиотеки используйте pip:

```bash

pip install colorbykawa
```

## Инициализация
```
from colorbykawa import ColorByKawa

cola = ColorByKawa()

```

## Примеры использования

Вы можете использовать константы класса Color для окрашивания текста в терминале. Вот несколько примеров:

```python
from colorbykawa import ColorByKawa

cola = ColorByKawa()
print(cola.Red + "This is red" + cola.Reset)
print(cola.Blue + "This is blue" + cola.Reset)


```
## Доступные цвета

```Класс Color предоставляет следующие константы:
    Reset: сброс
    Black: Черный
    Red: Красный
    Green: Зеленый
    Yellow: Желтый
    Blue: Синий
    Magenta: Пурпурный
    Cyan: Голубой
    White: Белый
    Gray: Серый
    RedLight: Светло-красный
    GreenLight: Светло-зеленый
    YellowLight: Светло-желтый
    BlueLight: Светло-синий
    MagentaLight: Светло-пурпурный
    CyanLight: Светло-голубой
    WhiteLight: Светло-белый
    BlackBright: Ярко-черный
    RedBright: Ярко-красный
    GreenBright: Ярко-зеленый
    YellowBright: Ярко-желтый
    BlueBright: Ярко-синий
    MagentaBright: Ярко-пурпурный
    CyanBright: Ярко-голубой
    WhiteBright: Ярко-белый
    Orange: Оранжевый
    Purple: Пурпурный
    Turquoise: Бирюзовый
    Brown: Коричневый
    Pink: Розовый
    LightGray: Светло-серый
    DarkGray: Темно-серый
    LightRed: Светло-красный
    LightGreen: Светло-зеленый
    LightYellow: Светло-желтый
    LightBlue: Светло-синий
    LightMagenta: Светло-пурпурный
    LightCyan: Светло-голубой
    LightWhite: Светло-белый
    DarkRed: Темно-красный
    DarkGreen: Темно-зеленый
    DarkYellow: Темно-желтый
    DarkBlue: Темно-синий
    DarkMagenta: Темно-пурпурный
    DarkCyan: Темно-голубой
    DarkWhite: Темно-белый
    SkyBlue: Небесно-голубой
    SeaGreen: Морской зеленый
    Indigo: Индиго
    Coral: Кораловый
    Beige: Бежевый
    Lime: Лаймовый
    Cherry: Вишневый
    Salmon: Лососевый
    Olive: Оливковый
    Tan: Загар
    IndigoBlue: Индиго-синий
    Wheat: Пшеничный
    Honeydew: Медовый
    Mint: Мятный
    Rose: Розовый
    Moccasin: Мокасин
    Caramel: Карамельный
    Lavender: Лавандовый
    Mauve: Маув
    Goldenrod: Золотисто-желтый
    Ivory: Слоновая кость
    Aquamarine: Аквамарин
    Raspberry: Малина
    Cantaloupe: Дыня
    Ash: Пепельный
    Chocolate: Шоколадный
    Emerald: Изумрудный
    Ruby: Рубиновый
    TerraCotta: Терракотовый
    MintGreen: Мятно-зеленый
    Blush: Румянец
    Tangerine: Мандариновый
    Auburn: Рыжий
    Coffee: Кофейный
    Papaya: Папайя
    CherryRed: Вишневый
    Cinnamon: Коричный
    Daffodil: Нарцисс
    MossGreen: Мшисто-зеленый
    Aubergine: Баклажановый
    Lilac: Сиреневый
    MoonYellow: Лунный желтый
    Eggplant: Баклажан
    PapayaWhip: Папайя (цвет)
    Granite: Гранитный
    Khaki: Хаки
    Sunflower: Подсолнух
    MauveTaupe: Маув-тауpe
    Fuchsia: Фуксия

```
## Примечание

Цвета отображаются корректно только в терминалах, которые поддерживают ANSI-коды. Если ваш терминал не поддерживает ANSI-коды, текст может не окрашиваться должным образом.
Лицензия

Этот проект лицензирован под лицензией MIT. См. файл LICENSE для получения подробной информации
