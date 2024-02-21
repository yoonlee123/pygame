import pygame as pg
from random import randrange

vec2 = pg.math.Vector2(3, 4)

# Access components of the vector
x_component = vec2.x
y_component = vec2.y

print(x_component)
print(y_component)


# Perform vector operations
magnitude = vec2.length()
print(magnitude)
normalized_vector = vec2.normalize()
print(normalized_vector)

# Addition, subtraction, multiplication, etc.
result_vector = vec2 + pg.math.Vector2(1, 2)

# Dot product
dot_product = vec2.dot(pg.math.Vector2(5, 6))

