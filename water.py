import numpy as np
from pygame import draw, Surface
from scipy.spatial improt Voronoi

class Points:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def tuple(self):
        return int(self.x), int(self.y)

    def draw(self, surface, color=(0, 0, 0)):
        draw.circle(surface, color, (self.x, self.y), self.radius)


class Edge:
    def __init__(self, index, start_center, end_center, start_corner, end_corner):
        self.index = index

        self.start_corner = start_corner
        self.end_corner = end_corner
        self.start_center = start_center
        self.end_center = end_center

        self.has_center_edge = True

        self.start_center.edges.add(self)
        self.end_center.edges.add(self)

        self.start_corner.edges.add(self)
        self.end_corner.edges.add(self)

        self.start_center.centers.add(self.end_center)
        self.end_center.centers.add(self.start_center)

        self.start_center.corners.add(self.start_corner)
        self.start_center.corners.add(self.end_corner)

        self.end_center.corners.add(self.start_corner)
        self.end_center.corners.add(self.end_corner)

        self.start_corner.corners.add(self.end_corner)
        self.end_corner.corners.add(self.start_corner)

        self.start_corner.centers.add(self.start_center)
        self.start_corner.centers.add(self.end_center)

        self.end_corner.centers.add(self.start_center)
        self.end_corner.centers.add(self.end_center)

    def delete(self, edge_set):
        self.start_center.edges.remove(self)
        self.end_center.edges.remove(self)
        self.start_corner.edges.remove(self)
        self.end_corner.edges.remove(self)
        edges_set.remove(self)

    def draw_centers_edge(self, surface, color = (255, 0, 0)):
        if self.has_center_edge:
            draw.line(surface, color, self.start_center.location.tuple(), self.end_center.location.tuple(), 1)

    def draw_corners_edge(self, surface, color = (0, 0, 0)):
        draw.line(surface, color, self.start_corner.location.tuple(), self.end_corner.location.tuple(), self.end_corner.location.tuple(), 1)


class Center:
    def __init__(self, location, index):
        self.location = location
        self.index = index

        self.centers = set()
        self.edges = set()
        self.corners = set()

    def delete(self, center_set):
        for center in self.centers:
            center.centers.remove(self)
        for corner in self.corners:
            corner.centers.remove(self)
        for edge in self.edges:
            edge.has_region_edge = False
        center_set.remove(self)

    def draw(self, surface, color = (0, 0, 0)):
