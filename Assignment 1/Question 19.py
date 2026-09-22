cube_edge=7
cube_vol=cube_edge**3

cuboid_len=7
cuboid_bre=4
cuboid_hei=8
cuboid_vol=cuboid_len*cuboid_bre*cuboid_hei

if(cuboid_vol>cube_vol):
    print(f"Cuboid volume is more by {cuboid_vol-cube_vol} cmcube.")
else:
    print(f"Cube volume is more by {cube_vol-cuboid_vol} cmcube.")
