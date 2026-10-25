#   Int Provider

Int providers are data objects that operate on the given context, and return an [integer][integer] based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired int provider type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Int Provider Type
    ----------|------------------
    [String][string] | [`context`](../meta/conditional.md)
    [Integer][integer] | [`constant`](constant.md)


### Meta types

<div class="annotate" markdown>

- [`absolute`](../meta/number/absolute.md)(1)
- [`clamped`](../meta/number/clamped.md)
- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`context`](../meta/conditional.md)
- [`difference`](../meta/number/difference.md) (2)
- [`from_float`](from_float.md)
- [`max`](../meta/number/max.md)
- [`min`](../meta/number/min.md)
- [`negate`](../meta/number/negate.md)
- [`product`](../meta/number/product.md) (3)
- [`quotient`](../meta/number/quotient.md)(4)
- [`random/binomial`](random_binomial.md)
- [`random/uniform`](../meta/number/random_uniform.md)(5)
- [`sum`](../meta/number/sum.md)(6)
- [`weighted`](../meta/weighted.md)

</div>

1. Aliases: `abs`
2. Aliases: `sub`, `diff`, `subtract`
3. Aliases: `mul`, `multiply`
4. Aliases: `div`, `divide`
5. Aliases: `rand`, `random`
6. Aliases: `add`, `addition`


### Types

- [`adjacent_blocks`](adjacent_blocks.md)
- [`blocks_colliding_box`](blocks_colliding_box.md)
- [`blocks_intersecting_box`](blocks_intersecting_box.md)
- [`count_in_area`](count_in_area.md)
- [`effect/amplifier`](effect_amplifier.md)
- [`entity/active_effects`](entity_active_effects.md)
- [`equipped_enchantment_level`](equipped_enchantment_level.md)
- [`item/count/max`](item_count_max.md)
- [`item/count`](item_count.md)
- [`item/fuel`](item_fuel.md)
- [`key/pressed_ticks`](key_pressed_ticks.md)
- [`key/pressed_time`](key_pressed_time.md)
- [`light_level`](light_level.md)
- [`nbt`](nbt.md)
- [`player/food`](player_food.md)
- [`power/cooldown/remaining_ticks`](power_cooldown_remaining_ticks.md)
- [`slot_id`](slot_id.md)
- [`time`](time.md)
