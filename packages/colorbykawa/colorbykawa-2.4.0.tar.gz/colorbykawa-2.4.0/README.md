ColorbyKawa

colorbykawa — это библиотека для окрашивания текста в терминале с использованием ANSI-цветов. Библиотека предоставляет класс Color, который содержит константы для различных цветов.

## Установка

Для установки библиотеки используйте pip:

```bash

pip install colorbykawa
```

## Инициализация
```
import colorbykawa
#col можно заменить на любое другое название
col = ColorByKawa()
```

## Примеры использования

Вы можете использовать константы класса Color для окрашивания текста в терминале. Вот несколько примеров:

```python
import colorbykawa
  col = ColorByKawa()
    print(col.Red + "This is red" + col.Reset)
    print(col.Green + "This is green" + col.Reset)
    print(col.Blue + "This is blue" + col.Reset)

```
## Доступные цвета

```Класс Color предоставляет следующие константы:

    Red: Красный
    Green: Зеленый
    Yellow: Желтый
    Blue: Синий
    Magenta: Магентовый
    Cyan: Циан
    Reset: Сброс (возвращает цвет текста в исходное состояние)
    White: Белый
    LightGray: Светло-серый
    LightRed: Светло-красный
    LightGreen: Светло-зеленый
    LightYellow: Светло-желтый
    LightBlue: Светло-синий
    LightMagenta: Светло-магентовый
    LightCyan: Светло-циан
    LightWhite: Светло-белый
    Black: Черный
    Orange: Оранжевый
    Coral: Кораловый
    Pink: Розовый
    LightPink: Светло-розовый
    LightCoral: Светло-коралловый
    Salmon: Лососевый
    Peach: Персиковый
    Apricot: Абрикосовый
    LightApricot: Светло-абрикосовый
    Beige: Бежевый
    Cream: Кремовый
    Milk: Молочный
    Ivory: Слоновая кость
    Lemon: Лимонный
    LightLemon: Светло-лимонный
    Canary: Канареечный
    LightCanary: Светло-канареечный
    Salad: Салатный
    LightSalad: Светло-салатный
    Apple: Яблочный
    LightApple: Светло-яблочный
    Lime: Лаймовый
    LightLime: Светло-лаймовый
    Mint: Мятный
    LightMint: Светло-мятный
    Emerald: Изумрудный
    LightEmerald: Светло-изумрудный
    Turquoise: Бирюзовый
    LightTurquoise: Светло-бирюзовый
    Aquamarine: Аквамариновый
    LightAquamarine: Светло-аквамариновый
    Azure: Лазурный
    LightAzure: Светло-лазурный
    SkyBlue: Небесно-голубой
```
## Примечание

Цвета отображаются корректно только в терминалах, которые поддерживают ANSI-коды. Если ваш терминал не поддерживает ANSI-коды, текст может не окрашиваться должным образом.
Лицензия

Этот проект лицензирован под лицензией MIT. См. файл LICENSE для получения подробной информации
