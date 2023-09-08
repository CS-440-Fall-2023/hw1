import math

def diff(v1, v2):
    if isinstance(v1, int) or isinstance(v1, float):
        assert isinstance(v2, int) or isinstance(v2, float)
        return v1 - v2
    assert isinstance(v1, tuple) and isinstance(v2, tuple) and len(v1) == len(v2)
    return tuple([e-v2[i] for i,e in enumerate(v1)])
    
# def smul(s, v):
#     if isinstance(v, int) or isinstance(v, float):
#         return s * v
#     return tuple([s*e for e in v])
    
def length(v):
    if isinstance(v, int) or isinstance(v, float):
        return v 
    assert isinstance(v, tuple)
    return math.sqrt(sum(e*e for e in v))
    
# def add(v1, v2):
#     if isinstance(v1, int) or isinstance(v1, float):
#         assert isinstance(v2, int) or isinstance(v2, float)
#         return v1 + v2
#     assert isinstance(v1, tuple) and isinstance(v2, tuple) and len(v1) == len(v2)
#     return tuple([e+v2[i] for i,e in enumerate(v1)])

def mix(u, v, a):
    def mix_s(x,y,a):
        return (1-a) * x + a * y
    if isinstance(u, int) or isinstance(u, float):
        assert isinstance(v, int) or isinstance(v, float)
        return mix_s(u, v, a)
    assert isinstance(u, tuple) and isinstance(v, tuple) and len(u) == len(v)
    return tuple(mix_s(e, v[i], a) for i,e in enumerate(u))
    
def map_point(P, Q, A, B, X):
    s = length(diff(P, X)) / length(diff(P, Q))
    return mix(A, B, s)


def q4a(W):
    w = W - 1
    print('input\tcoordinate\n------------------------------')
    for s in [0,w,w//4,w//2,3*w//4,w] + list(range(100, W, 100)):
        print(f'{s}\t({map_point(0, w, -1, 1, s)}, 0)')


def q4b(W):
    w = W - 1
    white = (1,1,1)
    black = (0,0,0)
    print('input\tgray\n------------------------------')
    for s in [0,w,w//4,w//2,3*w//4,w] + list(range(100, W, 100)):
        print(f'{s}\t{map_point(0, w, black, white, s)}')


def q4c(W):
    w = W - 1
    red = (1,0,0)
    green = (0,1,0)
    blue = (0,0,1)
    print('input\tcolor\n------------------------------')
    for s in [0,w//4,w//2,3*w//4,w] + list(range(100, W, 100)):
        if s < w/2:
            print(f'{s}\t{map_point(0, w/2, red, green, s)}')
        else:
            print(f'{s}\t{map_point(w/2, w, green, blue, s)}')


def q5a(W):
    w = W - 1
    print('pixel\tcomplex number\n------------------------------')
    for x in [0,w//4,w//2,3*w//4,w]:
        for y in [0,w//4,w//2,3*w//4,w]:
            real = map_point(0,w, -2, 2, x)
            comp = map_point(0,w, 2, -2, y)
            s = f"{real} {'+' if comp >= 0 else '-'} {abs(comp)}i"
            print(f'({x}, {y})\t{s}')


def q5b(W):
    w = W - 1
    print('pixel\tcomplex number\n------------------------------')
    for x in [0,w//4,w//2,3*w//4,w]:
        for y in [0,w//4,w//2,3*w//4,w]:
            x1 = map_point(0,w,-1,1,x)
            y1 = map_point(0,w,1,-1,y)
            print(f'({x}, {y})\t({x1}, {y1})')


def gen_cases():
    for f in [q4a, q4b, q4c, q5a, q5b]:
        for L in [256, 513]:
            print(f'{f.__name__}({L})')
            f(L)
            print("==================================================")

            
