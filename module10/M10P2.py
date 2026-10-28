def getWallArea(length, width, height):
    area = 2*length*height +2*width*height
    return area
def getCeilingArea(length, width):
    area = length * width
    return area
answer = "yes"

while answer == "yes":
    length = float(input("enter room length: "))
    width = float(input("enter room width: "))
    height = float(input("enter room height: "))
    wallArea = getWallArea(length, width, height)
    gallons = wallArea/50
    print("wall square feet:", round(wallArea, 2))
    print("gallons of wall paint needed:", round(gallons, 2))
    ceilingArea = getCeilingArea(length, width)
    ceilingGallons = ceilingArea / 50
    print("ceiling square feet:", round(ceilingArea, 2))
    print("gallons of ceiling paint needed:", round(ceilingGallons, 2))
    answer = input("do you want to continue? (yes or no): ").lower()
