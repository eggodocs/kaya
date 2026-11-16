import math
import decimal

def define_env(env):

    degrees_to_radians_multiplier = 0.017453292519943295
    radians_to_degrees_multiplier = 57.29577951308232

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
    def brightness_dict(ambient_light=float):

        values = {}

        for light_level in range(16):
            values[light_level] = ambient_light + (1 - ambient_light) * light_level / (60 - 3 * light_level)

        return values

    @env.macro
    def to_radians(degrees):
        return degrees * degrees_to_radians_multiplier

    @env.macro
    def to_degrees(radians):
        return radians * radians_to_degrees_multiplier

    @env.macro
    def cos(radians):
        return math.cos(radians)

    @env.macro
    def acos(cos):
        return math.acos(cos)

    @env.macro
    def sin(radians):
        return math.sin(radians)

    @env.macro
    def asin(sin):
        return math.asin(sin)

    @env.macro
    def sqrt(v):
        return math.sqrt(v)

    @env.macro
    def inv_sqrt(v):
        return 1.0 / sqrt(v)

    @env.macro
    def atan2(y, x):
        return math.atan2(y, x)

    @env.macro
    def atan(x):
        return math.atan(x)

    @env.filter
    def string_transform(elements=list, pattern=str):

        result = []

        for element in elements:
            result.append(pattern.format(element))

        return result


