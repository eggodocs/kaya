#   Container Menu

Container menus are objects that defines the GUI (graphical user interface) and container of an inventory.


!!! note

    This type is mainly used by the `inventory` power type.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired container menu type.


???+ question "Implicit types"

    When defining a container menu, if a [string][string] is specified, it will implicitly use one of the following container menu types that match:

    - [`generic_9x1`](generic_9x1.md)
    - [`generic_9x2`](generic_9x2.md)
    - [`generic_9x3`](generic_9x3.md)
    - [`generic_9x4`](generic_9x4.md)
    - [`generic_9x5`](generic_9x5.md)
    - [`generic_9x6`](generic_9x6.md)
    - [`generic_3x3`](generic_3x3.md)
    - [`hopper`](hopper.md)


## Types

<div class="annotate" markdown>

- [`generic_9x1`](generic_9x1.md)
- [`generic_9x2`](generic_9x2.md)
- [`generic_9x3`](generic_9x3.md)(1)
- [`generic_9x4`](generic_9x4.md)
- [`generic_9x5`](generic_9x5.md)
- [`generic_9x6`](generic_9x6.md)(2)
- [`generic_3x3`](generic_3x3.md)(3)
- [`hopper`](hopper.md)
- [`dynamic`](dynamic.md) (<span style="color:darkred"><b>Doesn't currently work</b></span>)

</div>

1. Aliases: `chest`
2. Aliases: `double_chest`
3. Aliases: `dispenser`, `dropper`
