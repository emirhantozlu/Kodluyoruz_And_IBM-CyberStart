import math

# noktalar adında bir dizi oluşturup. Bu dizide tuple türünde noktalar tuttuk.
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # Öklid Mesafesi formülünü kullanarak iki nokta arasındaki mesafeyi hesapladık.
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        # Her iki nokta arasındaki mesafeyi hesaplayıp distances listesine ekledik.
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması için min fonksiyonunu kullandık.
min_distance = min(distances)

print("Minimum Mesafe:", min_distance)
