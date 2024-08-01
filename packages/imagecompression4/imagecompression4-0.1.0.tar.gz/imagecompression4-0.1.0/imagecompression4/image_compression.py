from PIL import Image
import numpy as np
from .reis_algorithm import reis_algorithm

def image_to_matrix(image_path):
    image = Image.open(image_path).convert('L')
    matrix = np.array(image)
    return matrix

def matrix_to_image(matrix, output_path):
    image = Image.fromarray(matrix)
    image.save(output_path)

def compress_image(matrix, epsilon=1e-6):
    n = matrix.shape[0]
    P = np.eye(n)
    R = reis_algorithm(matrix, P, epsilon)
    return R

def normalize(matrix):
    matrix = matrix - np.min(matrix)
    matrix = matrix / np.max(matrix) * 255
    return matrix.astype(np.uint8)

def main(image_path, compressed_image_path, epsilon=1e-6):
    matrix = image_to_matrix(image_path)
    compressed_matrix = compress_image(matrix, epsilon)
    normalized_matrix = normalize(compressed_matrix)
    matrix_to_image(normalized_matrix, compressed_image_path)