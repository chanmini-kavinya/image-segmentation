import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import deque

def region_growing(img, seed, threshold):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    h, w = img.shape
    segmented = np.zeros((h, w), dtype=np.uint8)
    
    neighbors = [(-1,-1), (-1,0), (-1,1),
                 (0,-1),          (0,1),
                 (1,-1),  (1,0), (1,1)]
    
    x, y = seed
    seed_value = img[y, x]
    
    queue = deque()
    queue.append((x, y))
    segmented[y, x] = 255
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < w and 0 <= ny < h:
                if segmented[ny, nx] == 0:
                    if abs(int(img[ny, nx]) - int(seed_value)) <= threshold:
                        segmented[ny, nx] = 255
                        queue.append((nx, ny))
    
    return segmented

def main():
    image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
    seed_point = (170, 100)  
    threshold = 20
    segmented = region_growing(image, seed_point, threshold)

    plt.figure(figsize=(15, 5))
    plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
    plt.subplot(132), plt.imshow(image, cmap='gray')
    plt.plot(seed_point[0], seed_point[1], 'ro'), plt.title('Seed Point')
    plt.subplot(133), plt.imshow(segmented, cmap='gray'), plt.title('Region Growing Result')
    plt.show()

if __name__ == '__main__':
    main()
