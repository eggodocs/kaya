#   Modifier

Modifiers are objects used to specify how a floating point value is modified.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired modifier type.
`phase` | [Phase](#phase) | | Determines when the modifier will be applied.
`modifiers` | [Array][array] of [Modifiers][modifier] | *optional* | If specified, these modifiers will be applied first before the this modifier is applied.
`amount` | [Float Provider][float_provider] | | The amount of the modifier.

[](){ #phase }

???+ info "Phase"

    Modifiers are applied in the following order:

    Phase | Description
    ------|------------
    `base` | Determines that the base value will be modified. This is the first phase where the total value is equal to the base value.
    `total` | Determines that the total value will be modified.


### Types

!!! note

    Modifiers are applied in the order they're listed below, with `add` being applied first and `set` being applied last.


Type | Description
-----|------------
`add` | Adds all of the modifiers' amounts to the value.<br>$(Total = Amount_1 + Amount_2 + ... + Amount_n)$
`multiply` | Multiplies the modifiers' amounts to the value.<br>$(Total = Amount_1 * Amount_2 + ... + Amount_n)$
`multiply_additive` | Multiplies the base value by (1 + sum of modifiers' amounts.)<br>$(Total = Base * (1 + Amount_1 + Amount_2 + ... + Amount_n))$
`multiply_multiplicative` | Multiplies the base value by (1 + modifiers' amount) for every modifier.<br>$(Total = Base * (1 + Amount_1) * (1 + Amount_2) * ... * (1 + Amount_n))$
`divide` | Divides the value to all of the modifiers' amounts.<br>$(Total = Amount_1 \div Amount_2 \div ... \div Amount_3)$
`min` | Returns the minimum value of all the modifiers' amounts.<br>$(Total = \argmin f(Amount_n))$
`max` | Returns the maximum value of all the modifiers' amounts.<br>$(Total = \argmax f(Amount_n))$
`set` | Uses the modifier's value as the new total value.<br>$(Total = Amount_n)$
