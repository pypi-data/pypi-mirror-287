ColorbyKawa

colorbykawa — это библиотека для окрашивания текста в терминале с использованием ANSI-цветов. Библиотека предоставляет класс Color, который содержит константы для различных цветов.

## Установка

Для установки библиотеки используйте pip:

```bash

pip install colorbykawa
```
## Примеры использования

Вы можете использовать константы класса Color для окрашивания текста в терминале. Вот несколько примеров:

```python
import colorbykawa

# Get a singleton instance of the Color class
col = colorbykawa.color

# Examples of usage
print(col.Red + "This is red text" + col.Reset)
print(col.Green + "This is green text" + col.Reset)
print(col.Yellow + "This is yellow text" + col.Reset)
print(col.Blue + "This is blue text" + col.Reset)
print(col.Magenta + "This is magenta text" + col.Reset)
print(col.Cyan + "This is cyan text" + col.Reset)
print(col.White + "This is white text" + col.Reset)
print(col.LightGray + "This is light gray text" + col.Reset)
print(col.Black + "This is black text" + col.Reset)
print(col.Orange + "This is orange text" + col.Reset)

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
