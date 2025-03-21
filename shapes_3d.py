#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Реализация 3D фигур для векторного редактора.
Включает классы: Parallelepiped, Tetrahedron.
"""

import math
from shape import Shape3D


class Parallelepiped(Shape3D):
    """Класс для представления параллелепипеда в 3D пространстве."""
    
    def __init__(self, x, y, z, width, height, depth, name="Parallelepiped"):
        """
        Инициализация параллелепипеда.
        
        Args:
            x (float): X-координата левого нижнего ближнего угла
            y (float): Y-координата левого нижнего ближнего угла
            z (float): Z-координата левого нижнего ближнего угла
            width (float): Ширина (по оси X)
            height (float): Высота (по оси Y)
            depth (float): Глубина (по оси Z)
            name (str, optional): Название параллелепипеда. По умолчанию "Parallelepiped".
        """
        super().__init__(name)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.width = float(width)
        self.height = float(height)
        self.depth = float(depth)
        
        if self.width <= 0 or self.height <= 0 or self.depth <= 0:
            raise ValueError("Ширина, высота и глубина должны быть положительными числами")
    
    def get_volume(self):
        """
        Получить объем параллелепипеда.
        
        Returns:
            float: Объем параллелепипеда
        """
        return self.width * self.height * self.depth
    
    def get_surface_area(self):
        """
        Получить площадь поверхности параллелепипеда.
        
        Returns:
            float: Площадь поверхности параллелепипеда
        """
        return 2 * (self.width * self.height + self.width * self.depth + self.height * self.depth)
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о параллелепипеде.
        
        Returns:
            dict: Словарь с координатами, шириной, высотой и глубиной
        """
        return {
            'origin': {'x': self.x, 'y': self.y, 'z': self.z},
            'width': self.width,
            'height': self.height,
            'depth': self.depth
        }
    
    def __str__(self):
        """
        Строковое представление параллелепипеда.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Parallelepiped(origin=({self.x}, {self.y}, {self.z}), width={self.width}, height={self.height}, depth={self.depth})"


class Tetrahedron(Shape3D):
    """Класс для представления тетраэдра (правильного четырехгранника) в 3D пространстве."""
    
    def __init__(self, x, y, z, edge_length, name="Tetrahedron"):
        """
        Инициализация тетраэдра.
        
        Args:
            x (float): X-координата центра тетраэдра
            y (float): Y-координата центра тетраэдра
            z (float): Z-координата центра тетраэдра
            edge_length (float): Длина ребра тетраэдра
            name (str, optional): Название тетраэдра. По умолчанию "Tetrahedron".
        """
        super().__init__(name)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.edge_length = float(edge_length)
        
        if self.edge_length <= 0:
            raise ValueError("Длина ребра должна быть положительным числом")
    
    def get_volume(self):
        """
        Получить объем тетраэдра.
        
        Returns:
            float: Объем тетраэдра
        """
        return (math.sqrt(2) / 12) * self.edge_length ** 3
    
    def get_surface_area(self):
        """
        Получить площадь поверхности тетраэдра.
        
        Returns:
            float: Площадь поверхности тетраэдра
        """
        return math.sqrt(3) * self.edge_length ** 2
    
    def get_height(self):
        """
        Получить высоту тетраэдра.
        
        Returns:
            float: Высота тетраэдра
        """
        return math.sqrt(6) * self.edge_length / 3
    
    def _get_specific_info(self):
        """
        Получить специфичную информацию о тетраэдре.
        
        Returns:
            dict: Словарь с центром, длиной ребра и высотой
        """
        return {
            'center': {'x': self.x, 'y': self.y, 'z': self.z},
            'edge_length': self.edge_length,
            'height': self.get_height()
        }
    
    def __str__(self):
        """
        Строковое представление тетраэдра.
        
        Returns:
            str: Строковое представление
        """
        return f"{self.name} ({self.id}): Tetrahedron(center=({self.x}, {self.y}, {self.z}), edge_length={self.edge_length})"
