# 1) Update the comments and choose between "function", "variable", and "parameter"

import turtle

# `dance` is a ...[function/variable/parameter]...
def dance():
  turtle.left(1000)
  turtle.right(500)

# `pi` is a  ...[function/variable/parameter]...
pi = 3.1415926535

# `convert` is a ...[function/variable/parameter]...
# and `celcius` is a ...[function/variable/parameter]...
def convert(celcius):
  # `fahrenheit` is a  ...[function/variable/parameter]...
  fahrenheit = celcius * 9 / 5 + 32
  print(fahrenheit)

# `draw_spiral` is a ...[function/variable/parameter]...
# and `num_loops` is a ...[function/variable/parameter]...
# and `distance` is a ...[function/variable/parameter]...
# and `angle` is a ...[function/variable/parameter]...
def draw_spiral(num_loops, distance, angle):
  for i in range(num_loops):
    for _ in range(2):
      # `arm_length` is a ...[function/variable/parameter]...
      arm_length = i*distance
      turtle.forward(arm_length)
      turtle.left(angle)

# `say_hello` is a ...[function/variable/parameter]...
# and `name` is a ...[function/variable/parameter]...
def say_hello(name):
  print("Hello, " + name + "!")
  print("How are you today?")

# 2. Call `say_hello`
#    a) Call `say_hello` with the argument "Dr. EB"
say_hello("Dr. EB")
#    b) Call `say_hello` with your name as the argument
say_hello("Jordan")
#    c) Call `say_hello` with a friend's name as the argument
say_hello("Kyle")

# 3. Call `draw_spiral` with the following arguments:
#    a) use 5 for `num_loops`
#       use 10 for `distance`
#       use 45 for `angle`
draw_spiral(5,10,45)
#    b) use 11 for `num_loops`
#       use 5 for `distance`
#       use 120 for `angle`
draw_spiral(11,5,120)
#    c) use 20 for `num_loops`
#       use 1 for `distance`
#       use 60 for `angle`
draw_spiral(20,1,60)

turtle.exitonclick()
