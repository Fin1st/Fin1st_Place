#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Базовые классы для векторного редактора.
Содержит абстрактные классы для 2D и 3D фигур.
"""

from abc import ABC, abstractmethod
import json


class Shape(ABC):
    """Абстрактный базовый класс для всех фигур."""
    
    def __init__(self, name):
        """
        Инициализация базового класса фигуры.
        
        Args:
            name (str): Название фигуры
        """
        self.name = name
        self.id = None  # ID будет назначен при добавлении в редактор
    
    @abstractmethod
    def get_info(self):
        """
        Получить информацию о фигуре.
        
        Returns:
            dict: Словарь с информацией о фигуре
        """
        pass
    
    def to_json(self):
        """
        Преобразовать фигуру в JSON-строку.
        
        Returns:
            str: JSON-представление фигуры
        """
        return json.dumps(self.get_info())
    
    @abstractmethod
    def __str__(self):
        """
        Строковое представление фигуры.
        
        Returns:
            str: Строковое представление
        """
        pass


class Shape2D(Shape):
    """Абстрактный класс для 2D фигур."""
    
    def __init__(self, name):
        """
        Инициализация базового класса 2D фигуры.
        
        Args:
            name (str): Название фигуры
        """
        super().__init__(name)
        self.dimension = 2
    
    @abstractmethod
    def get_area(self):
        """
        Получить площадь фигуры.
        
        Returns:
            float: Площадь фигуры
        """
        pass
    
    @abstractmethod
    def get_perimeter(self):
        """
        Получить периметр фигуры.
        
        Returns:
            float: Периметр фигуры
        """
        pass
    
    def get_info(self):
        """
        Получить информацию о 2D фигуре.
        
        Returns:
            dict: Словарь с информацией о фигуре
        """
        info = {
            'id': self.id,
            'name': self.name,
            'type': self.__class__.__name__,
            'dimension': self.dimension
        }
        
        # Добавляем специфичные для фигуры данные
        info.update(self._get_specific_info())
        
        # Добавляем вычисляемые свойства
        try:
            info['area'] = self.get_area()
            info['perimeter'] = self.get_perimeter()
        except Exception as e:
            info['calculation_error'] = str(e)
            
        return info
    
    @abstractmethod
    def _get_specific_info(self):
        """
        Получить специфичную для конкретной фигуры информацию.
        
        Returns:
            dict: Словарь со специфичной информацией
        """
        pass


class Shape3D(Shape):
    """Абстрактный класс для 3D фигур."""
    
    def __init__(self, name):
        """
        Инициализация базового класса 3D фигуры.
        
        Args:
            name (str): Название фигуры
        """
        super().__init__(name)
        self.dimension = 3
    
    @abstractmethod
    def get_volume(self):
        """
        Получить объем фигуры.
        
        Returns:
            float: Объем фигуры
        """
        pass
    
    @abstractmethod
    def get_surface_area(self):
        """
        Получить площадь поверхности фигуры.
        
        Returns:
            float: Площадь поверхности
        """
        pass
    
    def get_info(self):
        """
        Получить информацию о 3D фигуре.
        
        Returns:
            dict: Словарь с информацией о фигуре
        """
        info = {
            'id': self.id,
            'name': self.name,
            'type': self.__class__.__name__,
            'dimension': self.dimension
        }
        
        # Добавляем специфичные для фигуры данные
        info.update(self._get_specific_info())
        
        # Добавляем вычисляемые свойства
        try:
            info['volume'] = self.get_volume()
            info['surface_area'] = self.get_surface_area()
        except Exception as e:
            info['calculation_error'] = str(e)
            
        return info
    
    @abstractmethod
    def _get_specific_info(self):
        """
        Получить специфичную для конкретной фигуры информацию.
        
        Returns:
            dict: Словарь со специфичной информацией
        """
        pass
