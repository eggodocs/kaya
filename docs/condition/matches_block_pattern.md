#   Matches Block Pattern

Checks if a pattern of blocks is matched.


Type ID: `neo-apoli:matches_block_pattern`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`pattern` | Nested [Array][array] of [Strings][string] | | Determines the pattern of blocks to match.
`where` | [Key-Condition Map](#key-condition_map) | | The map definition for the pattern.
`front_top_left` | [Vec3 Provider][vec3_provider] | | The relative front top-left position to check the pattern.
`forwards` | [Direction Provider][direction_provider] | | The forwards direction used for checking the pattern.
`up` | [Direction Provider][direction_provider] | | The upwards direction used for checking the pattern.
`partial` | [Boolean Provider][boolean_provider] | `false` | Determines whether this type should return true if any of the blocks in the pattern matched.


[](){ #key-condition_map }

???+ info "Key-condition map"

    An object that defines the corresponding condition of a character in a pattern, similar to how the ingredients of a shaped recipe is defined.


    ### Format

    Field | Type | Default | Description
    ------|------|---------|------------
    `<key>` | [Condition][condition] | | Determines the corresponding condition for the character `<key>` for a pattern.


### Example

```json
{
	"type": "neo-apoli:matches_block_pattern",
	"pattern": [
		[
			"###",
			"###",  // top
			"###"
		],
		[
			"###",
			"#~#",
			"###"
		],

		[
			"###",
			"#~#",
			"###"
		],
		[
			"###",
			"###",  // bottom
			"###"
		]
	],
	"where": {
		"#": {
			"type": "neo-apoli:is_block_in_tag",
			"tag": "#minecraft:planks",
			"block": "matching_block"
		},
		"~": {
			"type": "neo-apoli:is_block_of_type",
			"block_type": "minecraft:water",
			"block": "matching_block"
		}
	},
	"front_top_left": {
		"type": "neo-apoli:offset",
		"vector": {
			"type": "neo-apoli:entity/position",
			"entity": "this"
		},
		"offset": [
			1.0,
			0.0,
			1.0
		]
	},
	"forwards": "down",
	"up": "south"
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter is standing on top center of a tank-like structure made up of any wood planks filled with water.


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
