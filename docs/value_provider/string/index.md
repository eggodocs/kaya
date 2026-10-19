# String Provider

String providers are data objects that operate on the given context, and return a [string][string] based on the provided information.


### Format
Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired string provider type. |

???+ tip
    
    Specifying a [string][string] will implicitly use the `constant` string provider type.


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`constant`](constant.md)
- [`escape`](escape.md)
- [`join`](join.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`entity/uuid`](entity_uuid.md)
- [`from_float`](from_float.md)
- [`from_int`](from_int.md)
- [`nbt`](nbt.md)
