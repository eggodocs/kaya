#   String { #string_comparison }

Compares two strings lexicographically[^1].


Type ID: `kaya:string`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`comparator` | [Comparator][comparator] | | Determines how the strings are compared lexicographically.
`first` | [String Provider][string_provider] | | The first string to compare to.
`second` | [String Provider][string_provider] | | The second string to be compared.
`case_sensitive` | [Boolean Provider][boolean_provider] | `true` | Determines whether comparing the strings should be case-sensitive.


### Example

```json
{
    "type": "kaya:int",
    "comparator": "<",
    "first": "abc",
    "second": "def"
}
```

This example checks if the first string is lexographically less than the second string (which is true.)


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


[^1]: Comparing strings lexicographically means comparing the order of the strings' characters, similar to how words are arranged in a dictionary
