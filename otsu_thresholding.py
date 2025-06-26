import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_test_image():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[20:50, 20:50] = 85
    img[60:90, 60:90] = 170
    return img

def add_gaussian_noise(image, mean=0, std=10):
    noise = np.random.normal(mean, std, image.shape)
    noisy = image + noise
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    return noisy

def apply_otsu_threshold(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, thresh_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh_img

def main():
    img = generate_test_image()
    noisy_img = add_gaussian_noise(img)
    otsu_result = apply_otsu_threshold(noisy_img)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.subplot(1, 3, 2), plt.imshow(noisy_img, cmap='gray'), plt.title('Noisy')
    plt.subplot(1, 3, 3), plt.imshow(otsu_result, cmap='gray'), plt.title("Otsu's Threshold")
    plt.show()

if __name__ == '__main__':
    main()
