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

- [`box/component`](box_component.md)
- [`box/size`](box_size.md)
- [`brightness`](brightness.md)
- [`distance_between_vectors`](distance_between_vectors.md)
- [`entity/attribute`](entity_attribute.md)
- [`entity/fluid_height`](entity_fluid_height.md)
- [`item/attribute`](item_attribute.md)
- [`nbt`](nbt.md)
- [`player/saturation`](player_saturation.md)
- [`power/cooldown/progress`](power_cooldown_progress.md)
- [`rain_level`](rain_level.md)
- [`thunder_level`](thunder_level.md)
- [`vector/component`](vector_component.md)
- [`vector/length`](vector_length.md)
