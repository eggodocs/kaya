#   Float Provider

Float providers are data objects that operate on the given context, and return a float based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired float provider type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Float Provider Type
    ----------|------------------
    [String][string] | [`context`](../meta/conditional.md)
    [Float][float] | [`constant`](constant.md)


### Meta types

<div class="annotate" markdown>

- [`absolute`](../meta/number/absolute.md)(1)
- [`clamped`](../meta/number/clamped.md)
- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)
- [`difference`](../meta/number/difference.md)(2)
- [`from_int`](from_int.md)
- [`linear_interpolated`](linear_interpolated.md)(3)
- [`max`](../meta/number/max.md)
- [`min`](../meta/number/min.md)
- [`negate`](../meta/number/negate.md)
- [`power`](power.md)
- [`product`](../meta/number/product.md)(4)
- [`quotient`](../meta/number/quotient.md)(5)
- [`random/uniform`](../meta/number/random_uniform.md)(6)
- [`round`](round.md)
- [`sum`](../meta/number/sum.md)(7)
- [`weighted`](../meta/weighted.md)

</div>

1. Aliases: `abs`
2. Aliases: `sub`, `diff`, `subtract`
3. Aliases: `lerp`
4. Aliases: `mul`, `multiply`
5. Aliases: `div`, `divide`
6. Aliases: `random`, `rand`
7. Aliases: `add`, `addition`


### Types

- `box/component`
- `box/size`
- `brightness`
- `distance_between_positions`
- `entity/attribute`
- `entity/fluid_height`
- `item/attribute`
- `nbt`
- `player/saturation`
- `power/cooldown/progress`
- `vector/component`
- `vector/length`
