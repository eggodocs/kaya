#   Brightness

Provides the brightness level at a specific position.


Type ID: `kaya:brightness`


???+ info

    The brightness value is calculated using the following formula: $(Brightness = AmbientLight + (1 - AmbientLight) * LightLevel \div (60 - 3 * LightLevel))$


??? tip "Brightness values for the vanilla dimensions"

    Here's a table of light levels with their corresponding brightness values in each vanilla dimension:

    {% for dimension, ambient_light in dimension_ambient_lights.items() %}
    === "`{{ dimension }}` (ambient light of ${{ ambient_light }}$)"

        Light level | Brightness
        ------------|-----------
        {% for light_level, brightness in brightness_dict(ambient_light).items() %}${{ light_level }}$ | ${{ brightness }}$
        {% endfor %}

    {% endfor %}


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to get the brightness from.


### Example

```json
{
    "type": "kaya:brightness",
    "position": {
        "type": "kaya:entity/position",
        "entity": "this",
        "anchor": "eyes"
    }
}
```
