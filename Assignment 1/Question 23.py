cartoon_len=15
cartoon_bre=9
cartoon_hei=12
cartoon_vol=cartoon_hei*cartoon_len*cartoon_bre

cube_edge=3
cube_vol=cube_edge**3

number=cartoon_vol/cube_vol

print(f"The number of cubical boxes required is {number}")