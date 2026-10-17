#   Vec3

An object that contains 3 [floats][float], usually used to indicate a point in a three-dimensional space.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`x` | [Float][float] | | The X coordinate of the point.
`y` | [Float][float] | | The Y coordinate of the point.
`z` | [Float][float] | | The Z coordinate of the point.


???+ tip

    This type can be inlined by specifying an [array][array] of 3 [floats][float].


### Example

=== "Full"

    ```json
    {
        "x": 1.0,
        "y": 2.0,
        "z": 3.0
    }
    ```

=== "Inlined"

    ```json
    [
        1.0,
        2.0,
        3.0
    ]
    ```

This example provides a vec3 that has XYZ coordinates of 1, 2, 3 respectively.
