length=30
breadth=20
total_area=length*breadth

path1=4
path2=3

usable_area=total_area-((path1*length)+(path2*breadth)-(path1*path2))

print(f"The usable area is {usable_area}")