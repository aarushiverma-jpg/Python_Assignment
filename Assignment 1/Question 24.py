brick_length=25
brick_height=10
brick_breadth=7.5
brick_vol=brick_breadth*brick_height*brick_length

wall_length=2000
wall_breadth=200
wall_height=75
wall_vol=wall_breadth*wall_height*wall_length

number=wall_vol/brick_vol

price=0.9*number

print(F"The number required is {number} with a total cost of ${price} per thousand")