
---

# GeoAreaCalc

**GeoAreaCalc** — это Python-библиотека для вычисления площадей различных геометрических фигур, таких как круги и треугольники. Библиотека также включает проверку треугольников на прямоугольность.

## Установка

Для установки библиотеки выполните:

```bash
pip install GeoAreaCalc
```

или установите напрямую из GitHub:

```bash
pip install git+https://github.com/Qiaxx/GeoAreaCalc
```

## Использование

### Круг

Чтобы вычислить площадь круга, используйте класс `Circle`:

```python
from GeoAreaCalc.shapes import Circle

circle = Circle(radius=5)
area = circle.area()
print(f"Площадь круга: {area}")
```

Вывод:
```
Площадь круга: 78.53981633974483
```

### Треугольник

Чтобы вычислить площадь треугольника по трём сторонам и проверить, является ли треугольник прямоугольным, используйте класс `Triangle`:

```python
from GeoAreaCalc.shapes import Triangle

triangle = Triangle(3, 4, 5)
area = triangle.area()
is_right = triangle.is_right_triangle()

print(f"Площадь треугольника: {area}")
print(f"Является ли треугольник прямоугольным? {'Да' if is_right else 'Нет'}")
```

Вывод:
```
Площадь треугольника: 6.0
Является ли треугольник прямоугольным? Да
```

### Универсальный интерфейс

Используйте функцию `calculate_area` для вычисления площади фигуры без необходимости заранее знать её тип:

```python
from GeoAreaCalc.shapes import Circle, Triangle
from GeoAreaCalc.area_calculator import calculate_area

shapes = [Circle(5), Triangle(3, 4, 5)]

for shape in shapes:
    print(f"Площадь фигуры: {calculate_area(shape)}")
```

Вывод:
```
Площадь фигуры: 78.53981633974483
Площадь фигуры: 6.0
```

## Добавление новых фигур

Чтобы добавить новую фигуру, создайте новый класс, наследующий `Shape`, и реализуйте метод `area` для вычисления её площади. Пример:

```python
from GeoAreaCalc.shapes import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
```

Теперь вы можете вычислять площадь квадрата так же, как и для других фигур.

## Лицензия

Проект лицензирован под MIT License. Подробности см. в файле LICENSE.

## Авторы

[Dmitry B.](https://github.com/Qiaxx/GeoAreaCalc)

---