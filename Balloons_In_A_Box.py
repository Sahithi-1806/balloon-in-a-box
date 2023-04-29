import math

def main():
    test_case_number = 1
    while True:
        n = int(input()) 
        if n == 0: 
            break
        
        corner1 = tuple(map(int, input().split()))[:3]
        corner2 = tuple(map(int, input().split()))[:3]
        box_size = (abs(corner1[0] - corner2[0]), abs(corner1[1] - corner2[1]), abs(corner1[2] - corner2[2]))
        
        points = []
        for i in range(n):
            point = tuple(map(int, input().split()))
            points.append(point)
        z = int(input())
        unenclosed_volume = placeBalloons(box_size, points)
        print("Box", test_case_number, ":", unenclosed_volume)
        test_case_number += 1


def placeBalloons(box_size, points):
    balloons = []
    sorted_points = sorted(points, key = lambda x: x[2], reverse = True)
    unenclosed_volume = box_size[0] * box_size[1] * box_size[2]
    for point in sorted_points:
        if not collidesWithBalloons(point, balloons):
            balloon_volume = balloonVolume(point, box_size)
            unenclosed_volume -= balloon_volume

    return unenclosed_volume


def balloonVolume(point, box_size):
        x, y, z = point
        volume = 0
        radius = min(min(x, box_size[0] - x), min(y, box_size[1] - y), min(z, box_size[2] - z))
        volume = round(4 / 3 * math.pi * (radius ** 3))
        return volume


def collidesWithBalloons(point, balloons):
    for balloon in balloons:
        distance = ((balloon[0] - point[0]) * 2 + (balloon[1] - point[1]) * 2 + (balloon[2] - point[2]) * 2) * 0.5
        if distance < balloon[2]:
            return True
    return False


#DriverCode
main()
