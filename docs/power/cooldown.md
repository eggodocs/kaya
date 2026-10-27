#   Cooldown

Provides a timer to be used for powers that normally do not have a built-in cooldown, or just as a simple timer.


Type ID: `kaya:cooldown`


???+ info

    This type provides the following context parameter:

    Parameter | Description
    ----------|------------
    `hud/value` | A float that refers to the cooldown's remaining ticks.
    `hud/max_value` | A float specified in the `cooldown` field.
    `hud/min_value` | `0.0`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`hud_element` | [HUD Element][hud_element] | | The HUD element to display while the cooldown is in progress.
`cooldown` | [Int Provider][int_provider] | | Determines the amount of ticks the cooldown will be in progress before it can be triggered again.


### Example

```json
{
	"type": "kaya:cooldown",
	"hud_element": {
		"type": "kaya:overlay/texture",
		"sprite": {
			"atlas": "minecraft:textures/atlas/blocks.png",
			"id": "minecraft:block/water_still"
		},
		"color": {
			"type": "kaya:biome/water",
			"position": {
				"type": "kaya:entity/position",
				"entity": "this"
			},
			"alpha": {
				"type": "kaya:clamped",
				"value": {
					"type": "kaya:quotient",
					"dividend": "hud/value",
					"divisor": "hud/max_value"
				},
				"min": 0.0,
				"max": 0.75
			}
		}
	},
	"cooldown": 400
}
```

This example provides a cooldown that displays a biome color-dependent water overlay that gradually disappears based from the cooldown's remaining ticks.


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
