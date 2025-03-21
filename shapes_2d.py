#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Реализация 2D фигур для векторного редактора.
Включает классы: Point, Line, Circle, Square, Rectangle, RegularPolygon.
"""

import math
from shape import Shape2D


class Point(Shape2D):
    """Класс для представления точки в 2D пространстве."""
    
    def __init__(self, x, y, name="Point"):
        """
        Инициализация точки.
        
        Args:
            x (float): X-координата
            y (float): Y-координата
            name (str, optional): Название точки. По умолчанию "Point".
        """
        super().__init__(name)
        self.x = float(x)
        self.y = float(y)
    
    def get_area(self):
        """
        Площадь точки всегда равна 0.
        
        Returns:
            float: 0
        """
        return 0.0
    
    def get_perimeter(self):
        """
        Периметр точки всегда равен 0.
        
        Returns:
            float: 0
        """
        return 0.0
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о точке.
        
        Returns:
            dict: Словарь с координатами
        """
        return {
            'x': self.x,
            'y': self.y
        }
    
    def __str__(self):
        """
        Строковое представление точки.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Point({self.x}, {self.y})"


class Line(Shape2D):
    """Класс для представления отрезка в 2D пространстве."""
    
    def __init__(self, x1, y1, x2, y2, name="Line"):
        """
        Инициализация отрезка.
        
        Args:
            x1 (float): X-координата первой точки
            y1 (float): Y-координата первой точки
            x2 (float): X-координата второй точки
            y2 (float): Y-координата второй точки
            name (str, optional): Название отрезка. По умолчанию "Line".
        """
        super().__init__(name)
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
    
    def get_length(self):
        """
        Получить длину отрезка.
        
        Returns:
            float: Длина отрезка
        """
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
    
    def get_area(self):
        """
        Площадь отрезка всегда равна 0.
        
        Returns:
            float: 0
        """
        return 0.0
    
    def get_perimeter(self):
        """
        Периметр отрезка равен его длине.
        
        Returns:
            float: Длина отрезка
        """
        return self.get_length()
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию об отрезке.
        
        Returns:
            dict: Словарь с координатами и длиной
        """
        return {
            'start_point': {'x': self.x1, 'y': self.y1},
            'end_point': {'x': self.x2, 'y': self.y2},
            'length': self.get_length()
        }
    
    def __str__(self):
        """
        Строковое представление отрезка.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Line(({self.x1}, {self.y1}), ({self.x2}, {self.y2})), Length: {self.get_length():.2f}"


class Circle(Shape2D):
    """Класс для представления круга в 2D пространстве."""
    
    def __init__(self, center_x, center_y, radius, name="Circle"):
        """
        Инициализация круга.
        
        Args:
            center_x (float): X-координата центра
            center_y (float): Y-координата центра
            radius (float): Радиус круга
            name (str, optional): Название круга. По умолчанию "Circle".
        """
        super().__init__(name)
        self.center_x = float(center_x)
        self.center_y = float(center_y)
        self.radius = float(radius)
        
        if self.radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
    
    def get_area(self):
        """
        Получить площадь круга.
        
        Returns:
            float: Площадь круга
        """
        return math.pi * self.radius ** 2
    
    def get_perimeter(self):
        """
        Получить длину окружности.
        
        Returns:
            float: Длина окружности
        """
        return 2 * math.pi * self.radius
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о круге.
        
        Returns:
            dict: Словарь с центром и радиусом
        """
        return {
            'center': {'x': self.center_x, 'y': self.center_y},
            'radius': self.radius
        }
    
    def __str__(self):
        """
        Строковое представление круга.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Circle(center=({self.center_x}, {self.center_y}), radius={self.radius})"


class Square(Shape2D):
    """Класс для представления квадрата в 2D пространстве."""
    
    def __init__(self, x, y, side_length, name="Square"):
        """
        Инициализация квадрата.
        
        Args:
            x (float): X-координата левого нижнего угла
            y (float): Y-координата левого нижнего угла
            side_length (float): Длина стороны
            name (str, optional): Название квадрата. По умолчанию "Square".
        """
        super().__init__(name)
        self.x = float(x)
        self.y = float(y)
        self.side_length = float(side_length)
        
        if self.side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом")
    
    def get_area(self):
        """
        Получить площадь квадрата.
        
        Returns:
            float: Площадь квадрата
        """
        return self.side_length ** 2
    
    def get_perimeter(self):
        """
        Получить периметр квадрата.
        
        Returns:
            float: Периметр квадрата
        """
        return 4 * self.side_length
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о квадрате.
        
        Returns:
            dict: Словарь с координатами и длиной стороны
        """
        return {
            'bottom_left': {'x': self.x, 'y': self.y},
            'top_right': {'x': self.x + self.side_length, 'y': self.y + self.side_length},
            'side_length': self.side_length
        }
    
    def __str__(self):
        """
        Строковое представление квадрата.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Square(bottom_left=({self.x}, {self.y}), side_length={self.side_length})"


class Rectangle(Shape2D):
    """Класс для представления прямоугольника в 2D пространстве."""
    
    def __init__(self, x, y, width, height, name="Rectangle"):
        """
        Инициализация прямоугольника.
        
        Args:
            x (float): X-координата левого нижнего угла
            y (float): Y-координата левого нижнего угла
            width (float): Ширина
            height (float): Высота
            name (str, optional): Название прямоугольника. По умолчанию "Rectangle".
        """
        super().__init__(name)
        self.x = float(x)
        self.y = float(y)
        self.width = float(width)
        self.height = float(height)
        
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Ширина и высота должны быть положительными числами")
    
    def get_area(self):
        """
        Получить площадь прямоугольника.
        
        Returns:
            float: Площадь прямоугольника
        """
        return self.width * self.height
    
    def get_perimeter(self):
        """
        Получить периметр прямоугольника.
        
        Returns:
            float: Периметр прямоугольника
        """
        return 2 * (self.width + self.height)
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о прямоугольнике.
        
        Returns:
            dict: Словарь с координатами, шириной и высотой
        """
        return {
            'bottom_left': {'x': self.x, 'y': self.y},
            'top_right': {'x': self.x + self.width, 'y': self.y + self.height},
            'width': self.width,
            'height': self.height
        }
    
    def __str__(self):
        """
        Строковое представление прямоугольника.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Rectangle(bottom_left=({self.x}, {self.y}), width={self.width}, height={self.height})"


class RegularPolygon(Shape2D):
    """Класс для представления правильного многоугольника в 2D пространстве."""
    
    def __init__(self, center_x, center_y, num_sides, side_length, name="RegularPolygon"):
        """
        Инициализация правильного многоугольника.
        
        Args:
            center_x (float): X-координата центра
            center_y (float): Y-координата центра
            num_sides (int): Количество сторон
            side_length (float): Длина стороны
            name (str, optional): Название многоугольника. По умолчанию "RegularPolygon".
        """
        super().__init__(name)
        self.center_x = float(center_x)
        self.center_y = float(center_y)
        self.num_sides = int(num_sides)
        self.side_length = float(side_length)
        
        if self.num_sides < 3:
            raise ValueError("Количество сторон должно быть не менее 3")
        if self.side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом")
    
    def get_radius(self):
        """
        Получить радиус описанной окружности.
        
        Returns:
            float: Радиус описанной окружности
        """
        return self.side_length / (2 * math.sin(math.pi / self.num_sides))
    
    def get_apothem(self):
        """
        Получить апофему (радиус вписанной окружности).
        
        Returns:
            float: Апофема
        """
        return self.get_radius() * math.cos(math.pi / self.num_sides)
    
    def get_area(self):
        """
        Получить площадь правильного многоугольника.
        
        Returns:
            float: Площадь многоугольника
        """
        return 0.5 * self.num_sides * self.side_length * self.get_apothem()
    
    def get_perimeter(self):
        """
        Получить периметр правильного многоугольника.
        
        Returns:
            float: Периметр многоугольника
        """
        return self.num_sides * self.side_length
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о правильном многоугольнике.
        
        Returns:
            dict: Словарь с центром, количеством сторон, длиной стороны и радиусом
        """
        return {
            'center': {'x': self.center_x, 'y': self.center_y},
            'num_sides': self.num_sides,
            'side_length': self.side_length,
            'radius': self.get_radius(),
            'apothem': self.get_apothem()
        }
    
    def __str__(self):
        """
        Строковое представление правильного многоугольника.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): RegularPolygon(center=({self.center_x}, {self.center_y}), sides={self.num_sides}, side_length={self.side_length})"
