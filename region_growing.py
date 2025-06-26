import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import deque

def region_growing(img, seed_points, threshold):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape
    segmented = np.zeros((h, w), dtype=np.uint8)
    visited = np.zeros((h, w), dtype=bool)

    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0), (1,1)]

    queue = deque()
    
    for seed in seed_points:
        x, y = seed
        seed_value = img[y, x]
        queue.append((x, y, seed_value))
        segmented[y, x] = 255
        visited[y, x] = True

    while queue:
        x, y, seed_value = queue.popleft()

        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy

            if 0 <= nx < w and 0 <= ny < h and not visited[ny, nx]:
                if abs(int(img[ny, nx]) - int(seed_value)) <= threshold:
                    segmented[ny, nx] = 255
                    visited[ny, nx] = True
                    queue.append((nx, ny, seed_value))

    return segmented

def main():
    image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
    seed_points = [(170, 290), (110, 110)] 
    threshold = 15
    segmented = region_growing(image, seed_points, threshold)

    plt.figure(figsize=(15, 5))
    plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
    plt.subplot(132), plt.imshow(image, cmap='gray')
    plt.plot(seed_points[0], seed_points[1], 'ro'), plt.title('Seed Points')
    plt.subplot(133), plt.imshow(segmented, cmap='gray'), plt.title('Region Growing Result')
    plt.show()

if __name__ == '__main__':
    main()
