# import some utils

class BboxAnnotation:
    def __init__(self, category, x, y, w, h):
        self.category = category

        # Top-left, width, height coordinates RELATIVE to the image
        assert x >= 0 and y >= 0 and w >= 0 and h >= 0
        assert x <= 1 and y <= 1 and w <= 1 and h <= 1

        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return f"Bbox(x={self.x}, y={self.y}, w={self.w}, h={self.h})"

    def __repr__(self):
        return self.__str__()

class PolygonAnnotation:
    def __init__(self, category, points):
        # TODO: allow multiple polygons for single annotation
        self.category = category

        # Points are in the form of a list of (x, y) tuples
        assert len(points) >= 3
        for point in points:
            assert len(point) == 2
            assert point[0] >= 0 and point[1] >= 0
            assert point[0] <= 1 and point[1] <= 1

        self.points = points

    def __str__(self):
        return f"Polygon(points={self.points})"

    def __repr__(self):
        return self.__str__()

