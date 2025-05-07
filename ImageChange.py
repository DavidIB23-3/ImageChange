import cv2
import numpy as np

def apply_xor_to_collage(collage_path):
    # Загружаем коллаж
    collage = cv2.imread(collage_path)
    if collage is None:
        print("Ошибка загрузки изображения")
        return

    # Получаем размеры коллажа
    height, width = collage.shape[:2]

    # Вычисляем размеры каждого отдельного изображения в коллаже
    img_height = height // 3
    img_width = width // 3

    # Извлекаем левое нижнее изображение (ряд 3, колонка 1)
    bottom_left = collage[2 * img_height:3 * img_height, 0:img_width]

    # Извлекаем правое верхнее изображение (ряд 1, колонка 3)
    top_right = collage[0:img_height, 2 * img_width:3 * img_width]

    # Проверяем, что изображения одного размера
    if bottom_left.shape != top_right.shape:
        print("Размеры изображений не совпадают")
        return

    # Применяем операцию XOR между изображениями
    xor_result = cv2.bitwise_xor(bottom_left, top_right)

    # Заменяем правое верхнее изображение на результат XOR
    result_collage = collage.copy()
    result_collage[0:img_height, 2 * img_width:3 * img_width] = xor_result

    # Сохраняем результат
    cv2.imwrite('result_collage.jpg', result_collage)
    print("Результат сохранен в result_collage.jpg")

    # Показываем результат
    cv2.imshow('Original Collage', collage)
    cv2.imshow('Result Collage', result_collage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Пример использования
apply_xor_to_collage('result_collage.jpg')