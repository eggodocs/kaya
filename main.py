import math
import decimal

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
