#   Color

Colors are objects used to provide an integer from a context object. The provided integer is a packed ARGB color.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired color type.


!!! question "Implicit type"

    When defining a color, if a [string][string] is specified, it will implicitly use the `rgba` color type.

  
### List of hardcoded color types

- [`argb`](argb.md)
- [`hsv`](hsv.md)
- [`rgba`](rgba.md)


### List of dynamic color types

- [`dynamic/argb`](dynamic_argb.md)
- [`dynamic/hsv`](dynamic_hsv.md)
- [`dynamic/rgba`](dynamic_rgba.md)


### List of other color types

- [`biome/foliage`](biome_foliage.md)
- [`biome/grass`](biome_grass.md)
- [`biome/water`](biome_water.md)
