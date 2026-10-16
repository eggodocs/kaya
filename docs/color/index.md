#   Color

Colors are objects used to provide an integer from a context object. The provided integer is a packed ARGB color.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired color type.


!!! question "Implicit `rgba`"

    When defining a color, if a [string][string] is specified, it will implicitly use the `rgba` color type.


### List of color types

- [`argb`](argb.md)
- [`biome/foliage`](biome_foliage.md)
- [`biome/grass`](biome_grass.md)
- [`biome/water`](biome_water.md)
- [`dynamic/argb`](dynamic_argb.md)
- [`dynamic/hsv`](dynamic_hsv.md)
- `dynamic/rgba`
- `hsv`
- `rgba`
