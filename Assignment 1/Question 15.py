length_shelly=22
breadth_shelly=15
area_shelly=length_shelly*breadth_shelly

side_rachel=21
area_rachel=side_rachel*side_rachel

if(area_rachel>area_shelly):
    print(f"Rachel has bigger garden and by {area_rachel-area_shelly} meter sq.")
else:
    print(f"Shelly has bigger garden and by {area_shelly-area_rachel} meter sq.")