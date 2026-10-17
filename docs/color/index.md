#   Color

Colors are objects used to provide an integer from a context object. The provided integer is a packed ARGB color.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired color type.


???+ tip

    Specifying a [string][string] will implicitly use the [`rgba`](rgba.md) color type.

  
### Hardcoded types

- [`argb`](argb.md)
- [`hsv`](hsv.md)
- [`rgba`](rgba.md)


### Dynamic types

- [`dynamic/argb`](dynamic_argb.md)
- [`dynamic/hsv`](dynamic_hsv.md)
- [`dynamic/rgba`](dynamic_rgba.md)


### Types

- [`biome/foliage`](biome_foliage.md)
- [`biome/grass`](biome_grass.md)
- [`biome/water`](biome_water.md)
