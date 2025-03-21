#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Главный модуль векторного редактора с CLI интерфейсом.
Обеспечивает взаимодействие пользователя с редактором через командную строку.
"""

import sys
import json
import uuid
from shape import Shape
from shapes_2d import Point, Line, Circle, Square, Rectangle, RegularPolygon
from shapes_3d import Parallelepiped, Tetrahedron


class VectorEditor:
    """Класс векторного редактора с CLI интерфейсом."""
    
    def __init__(self):
        """Инициализация редактора."""
        self.shapes = {}  # Словарь для хранения фигур (id -> фигура)
        self.next_id = 1  # Счетчик для генерации ID
        self.commands = {
            'help': self.show_help,
            'create': self.create_shape,
            'list': self.list_shapes,
            'info': self.show_shape_info,
            'delete': self.delete_shape,
            'clear': self.clear_shapes,
            'exit': self.exit_editor
        }
        
        # Словарь доступных типов фигур и их конструкторов
        self.shape_types = {
            'point': {
                'class': Point,
                'params': ['x', 'y'],
                'help': 'Создать точку: create point x y [name]'
            },
            'line': {
                'class': Line,
                'params': ['x1', 'y1', 'x2', 'y2'],
                'help': 'Создать отрезок: create line x1 y1 x2 y2 [name]'
            },
            'circle': {
                'class': Circle,
                'params': ['center_x', 'center_y', 'radius'],
                'help': 'Создать круг: create circle center_x center_y radius [name]'
            },
            'square': {
                'class': Square,
                'params': ['x', 'y', 'side_length'],
                'help': 'Создать квадрат: create square x y side_length [name]'
            },
            'rectangle': {
                'class': Rectangle,
                'params': ['x', 'y', 'width', 'height'],
                'help': 'Создать прямоугольник: create rectangle x y width height [name]'
            },
            'polygon': {
                'class': RegularPolygon,
                'params': ['center_x', 'center_y', 'num_sides', 'side_length'],
                'help': 'Создать правильный многоугольник: create polygon center_x center_y num_sides side_length [name]'
            },
            'parallelepiped': {
                'class': Parallelepiped,
                'params': ['x', 'y', 'z', 'width', 'height', 'depth'],
                'help': 'Создать параллелепипед: create parallelepiped x y z width height depth [name]'
            },
            'tetrahedron': {
                'class': Tetrahedron,
                'params': ['x', 'y', 'z', 'edge_length'],
                'help': 'Создать тетраэдр: create tetrahedron x y z edge_length [name]'
            }
        }
    
    def show_help(self, args=None):
        """
        Показать справку по командам.
        
        Args:
            args: Не используется
        """
        print("\nДоступные команды:")
        print("  help                      - Показать эту справку")
        print("  create <тип> <параметры>  - Создать новую фигуру")
        print("  list                      - Показать список всех фигур")
        print("  info <id>                 - Показать информацию о фигуре")
        print("  delete <id>               - Удалить фигуру")
        print("  clear                     - Удалить все фигуры")
        print("  exit                      - Выйти из редактора")
        
        print("\nДоступные типы фигур:")
        for shape_type, info in self.shape_types.items():
            print(f"  {info['help']}")
    
    def create_shape(self, args):
        """
        Создать новую фигуру.
        
        Args:
            args (list): Аргументы команды (тип фигуры и параметры)
        """
        if not args:
            print("Ошибка: Не указан тип фигуры")
            return
        
        shape_type = args[0].lower()
        if shape_type not in self.shape_types:
            print(f"Ошибка: Неизвестный тип фигуры '{shape_type}'")
            print("Используйте 'help' для просмотра доступных типов фигур")
            return
        
        shape_info = self.shape_types[shape_type]
        required_params = shape_info['params']
        
        # Проверяем, достаточно ли параметров
        if len(args) - 1 < len(required_params):
            print(f"Ошибка: Недостаточно параметров для создания фигуры '{shape_type}'")
            print(f"Использование: {shape_info['help']}")
            return
        
        # Извлекаем параметры
        params = args[1:len(required_params) + 1]
        
        # Проверяем, являются ли параметры числами
        try:
            # Преобразуем строковые параметры в числа
            numeric_params = []
            for param in params:
                # Для num_sides в многоугольнике нужно целое число
                if shape_type == 'polygon' and param == params[2]:
                    numeric_params.append(int(param))
                else:
                    numeric_params.append(float(param))
        except ValueError:
            print("Ошибка: Параметры должны быть числами")
            return
        
        # Проверяем, указано ли имя
        name = None
        if len(args) > len(required_params) + 1:
            name = args[len(required_params) + 1]
        else:
            # Если имя не указано, используем тип фигуры с порядковым номером
            name = f"{shape_type.capitalize()} {self.next_id}"
        
        # Создаем фигуру
        try:
            shape_class = shape_info['class']
            shape = shape_class(*numeric_params, name=name)
            
            # Назначаем ID и добавляем в словарь
            shape.id = self.next_id
            self.shapes[shape.id] = shape
            self.next_id += 1
            
            print(f"Создана фигура: {shape}")
        except Exception as e:
            print(f"Ошибка при создании фигуры: {e}")
    
    def list_shapes(self, args=None):
        """
        Показать список всех фигур.
        
        Args:
            args: Не используется
        """
        if not self.shapes:
            print("Список фигур пуст")
            return
        
        print("\nСписок фигур:")
        for shape_id, shape in self.shapes.items():
            print(f"  {shape_id}: {shape}")
    
    def show_shape_info(self, args):
        """
        Показать подробную информацию о фигуре.
        
        Args:
            args (list): Аргументы команды (ID фигуры)
        """
        if not args:
            print("Ошибка: Не указан ID фигуры")
            return
        
        try:
            shape_id = int(args[0])
        except ValueError:
            print("Ошибка: ID должен быть числом")
            return
        
        if shape_id not in self.shapes:
            print(f"Ошибка: Фигура с ID {shape_id} не найдена")
            return
        
        shape = self.shapes[shape_id]
        info = shape.get_info()
        
        print(f"\nИнформация о фигуре {shape_id}:")
        print(json.dumps(info, indent=2, ensure_ascii=False))
    
    def delete_shape(self, args):
        """
        Удалить фигуру.
        
        Args:
            args (list): Аргументы команды (ID фигуры)
        """
        if not args:
            print("Ошибка: Не указан ID фигуры")
            return
        
        try:
            shape_id = int(args[0])
        except ValueError:
            print("Ошибка: ID должен быть числом")
            return
        
        if shape_id not in self.shapes:
            print(f"Ошибка: Фигура с ID {shape_id} не найдена")
            return
        
        shape = self.shapes.pop(shape_id)
        print(f"Удалена фигура: {shape}")
    
    def clear_shapes(self, args=None):
        """
        Удалить все фигуры.
        
        Args:
            args: Не используется
        """
        count = len(self.shapes)
        self.shapes.clear()
        print(f"Удалено фигур: {count}")
    
    def exit_editor(self, args=None):
        """
        Выйти из редактора.
        
        Args:
            args: Не используется
        """
        print("Выход из редактора")
        sys.exit(0)
    
    def process_command(self, command_line):
        """
        Обработать введенную команду.
        
        Args:
            command_line (str): Строка с командой
        """
        # Разбиваем строку на команду и аргументы
        parts = command_line.strip().split()
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1:]
        
        # Выполняем команду, если она существует
        if command in self.commands:
            self.commands[command](args)
        else:
            print(f"Ошибка: Неизвестная команда '{command}'")
            print("Используйте 'help' для просмотра доступных команд")
    
    def run(self):
        """Запустить интерактивный режим редактора."""
        print("Векторный редактор CLI")
        print("Введите 'help' для просмотра доступных команд")
        
        while True:
            try:
                command_line = input("\n> ")
                self.process_command(command_line)
            except KeyboardInterrupt:
                print("\nПрервано пользователем")
                break
            except EOFError:
                print("\nКонец ввода")
                break
            except Exception as e:
                print(f"Ошибка: {e}")


if __name__ == "__main__":
    editor = VectorEditor()
    editor.run()
