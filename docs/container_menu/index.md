#   Container Menu

Container menus are objects that defines the GUI (graphical user interface) and container of an inventory.


!!! note

    This type is mainly used by the `inventory` power type.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired container menu type.


???+ tip

    Specifying a [string][string] will implicitly use one of the following types that match:

    - [`generic_9x1`](generic_9x1.md)
    - [`generic_9x2`](generic_9x2.md)
    - [`generic_9x3`](generic_9x3.md)
    - [`generic_9x4`](generic_9x4.md)
    - [`generic_9x5`](generic_9x5.md)
    - [`generic_9x6`](generic_9x6.md)
    - [`generic_3x3`](generic_3x3.md)
    - [`hopper`](hopper.md)


## Types

- [`generic_9x1`](generic_9x1.md)
- [`generic_9x2`](generic_9x2.md)
- [`generic_9x3`](generic_9x3.md)
- [`generic_9x4`](generic_9x4.md)
- [`generic_9x5`](generic_9x5.md)
- [`generic_9x6`](generic_9x6.md)
- [`generic_3x3`](generic_3x3.md)
- [`hopper`](hopper.md)
- [`dynamic`](dynamic.md)
