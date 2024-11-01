import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_normalized_intensity_profile(image_path):
    # Загрузка изображения в градациях серого
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Усреднение интенсивности вдоль оси Y для профиля по Z
    intensity_profile = np.mean(image, axis=0)

    # Нахождение максимальной интенсивности и нормировка
    B_max = np.max(intensity_profile)
    normalized_intensity_profile = intensity_profile / B_max

    return normalized_intensity_profile

# Пример использования для одного изображения
image_path = 'air_1_torr.JPG'
normalized_intensity_profile = calculate_normalized_intensity_profile(image_path)

# Построение графика
plt.plot(normalized_intensity_profile)
plt.xlabel('Z (положение вдоль оси трубки)')
plt.ylabel('Интенсивность (B / Bmax)')
plt.title('Нормированный профиль интенсивности вдоль оси Z')
plt.show()
plt.savefig('intensity_profile_air_1_torr.png')

