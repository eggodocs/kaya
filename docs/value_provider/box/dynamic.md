#   Dynamic

Provides a box with dynamic bounds.


Type ID: `kaya:dynamic`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`min` | [Vec3 Provider][vec3_provider] | | Determines the minimum bounds of the box.
`max` | [Vec3 Provider][vec3_provider] | | Determiens the maximum bounds of the box.


### Example

```json
{
    "type": "kaya:dynamic",
    "min": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
    },
    "max": {
        "type": "kaya:dynamic",
        "x": {
            "type": "kaya:nbt",
            "source": {
                "type": "kaya:storage",
                "id": "example:data"// (1)!
            },
            "path": "stuff[0]"
        },
        "y": {
            "type": "kaya:nbt",
            "source": {
                "type": "kaya:storage",
                "id": "example:data"// (2)!
            },
            "path": "stuff[1]"
        },
        "z": {
            "type": "kaya:nbt",
            "source": {
                "type": "kaya:storage",
                "id": "example:data"// (3)!
            },
            "path": "stuff[2]"
        }
    }
}
```

1. An example data storage with the following contents:

    ```mcfunction
    {value: true, stuff: [1, 2, 3], string: "Hello world!"}
    ```

2. An example data storage with the following contents:

    ```mcfunction
    {value: true, stuff: [1, 2, 3], string: "Hello world!"}
    ```

3. An example data storage with the following contents:

    ```mcfunction
    {value: true, stuff: [1, 2, 3], string: "Hello world!"}
    ```


This example provides a box whose maximum bounds depend on the values of the first, second, and last elements from the `stuff` NBT of the `example:data` data storage.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
