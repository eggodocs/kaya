# String Provider

String providers are data objects that operate on the given context, and return a [string][string] based on the provided information.


### Format
Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired string provider type. |

???+ tip
    
    Specifying a [string][string] will implicitly use the `constant` string provider type.


### Meta types

- `conditional/composite`
- `conditional`
- `constant`
- `escape`
- `join`


### Types

- `entity/uuid`
- `from_float`
- `from_int`
- `nbt`
