brick_length=15
brick_height=5
brick_breadth=8
brick_vol=(brick_breadth*100)*(brick_height*100)*(brick_length*100)

wall_length=15
wall_breadth=10
wall_height=8
wall_vol=wall_breadth*wall_height*wall_length

number=wall_vol/brick_vol

print(f"The number of bricks required is {number}")