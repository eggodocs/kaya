import math
import decimal

class Vec3f:

    def __init__(self, x=float, y=float, z=float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "X: " + str(self.x) + ", Y: " + str(self.y) + ", Z: " + str(self.z)

def define_env(env):

    def quantize(number, format, rounding_mode=None):
        return decimal.Decimal(number).quantize(decimal.Decimal(format), rounding_mode)

    @env.macro
    def round_up(number, format="1."):
        return quantize(number, format, decimal.ROUND_UP)

    @env.macro
    def round_down(number, format="1."):
        return quantize(number, format, decimal.ROUND_DOWN)

    @env.macro
    def ceil(number, format="1."):
        return quantize(number, format, decimal.ROUND_CEILING)

    @env.macro
    def floor(number, format="1."):
        return quantize(number, format, decimal.ROUND_FLOOR)

    @env.macro
    def round_half_up(number, format="1."):
        return quantize(number, format, decimal.ROUND_HALF_UP)
    
    @env.macro
    def round_half_down(number, format="1."):
        return quantize(number, format, decimal.ROUND_HALF_DOWN)

    @env.macro
    def round_half_even(number, format="1."):
        return quantize(number, format, decimal.ROUND_HALF_EVEN)

    @env.macro
    def clamped_lerp(delta, start, end):

        if delta < 0:
            return start
        
        elif delta > 1:
            return end
        
        else:
            return lerp(delta, start, end)

    @env.macro
    def lerp(delta, start, end):
        return start + delta * (end - start)

    @env.macro
    def sqrt(x):
        return math.sqrt(x)

    @env.macro
    def sqr(x):
        return x * x

    @env.macro
    def brightness_dict(ambient_light=float):

        values = {}

        for light_level in range(16):
            values[light_level] = ambient_light + (1 - ambient_light) * light_level / (60 - 3 * light_level)

        return values

    @env.macro
    def cross_product(a=Vec3f, b=Vec3f):
        return Vec3f(
            floor(a.y * b.z - a.z * b.y, "1.00"),
            floor(a.z * b.x - a.x * b.z, "1.00"),
            floor(a.x * b.y - a.y * b.x, "1.00")
        )

    @env.macro
    def to_str(o):
        return str(o)

    @env.macro
    def vec3f(x=float, y=float, z=float):
        return Vec3f(x, y, z)

    @env.filter
    def string_transform(elements=list, pattern=str):

        result = []

        for element in elements:
            result.append(pattern.format(element))

        return result


