#纪录步数
origins = 0
def get_step(origin):
    def go(step):
        nonlocal origin
        new_origin = origin + step
        origin = new_origin
        return new_origin

    return go(origin)

tourist = get_step(origins)
print(tourist(3))
print(tourist.__closure__[0].cell_contents)
print(tourist(4))
print(tourist(5))
'''
origin = 0
def go(step):
    global origin
    new_step = origin+step
    origin = new_step
    return new_step

print(go(3))
print(go(4))
print(go(5))
'''