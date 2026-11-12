#   Float Provider

Float providers are data objects that operate on the given context, and return a [float][float] based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired float provider type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Float Provider Type
    ----------|------------------
    [String][string] | [`context`](../meta/context.md)
    [Float][float] | [`constant`](constant.md)


### Meta types

- [`absolute`](../meta/number/absolute.md)(1)
- [`clamped`](../meta/number/clamped.md)
- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/context.md)
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


### Types

- [`box/component`](box_component.md)
- [`box/size`](box_size.md)
- [`brightness`](brightness.md)
- [`distance_between_vectors`](distance_between_vectors.md)
- [`entity/attribute`](entity_attribute.md)
- [`entity/fluid_height`](entity_fluid_height.md)
- [`entity/pitch`](entity_pitch.md)
- [`entity/yaw`](entity_yaw.md)
- [`item/attribute`](item_attribute.md)
- [`nbt`](nbt.md)
- [`player/saturation`](player_saturation.md)
- [`power/cooldown/progress`](power_cooldown_progress.md)
- [`rain_level`](rain_level.md)
- [`resource`](resource.md)
- [`thunder_level`](thunder_level.md)
- [`vector/component`](vector_component.md)
- [`vector/length`](vector_length.md)
