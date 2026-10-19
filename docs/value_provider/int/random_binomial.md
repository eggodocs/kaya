---
example:
    attempts: 8
    probability: 0.5
---


#   Random Binomial

Provides an integer value randomly calculated with [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).


Type ID: `neo-apoli:random/binomial`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`attempts` | [Int Provider][int_provider] | | The number of attempts.
`probability` | [Float Provider][float_provider] | | The success probability for each trial.


### Example
```json
{
    "type": "neo-apoli:random_binomial",
    "attempts": {{ example.attempts }},
    "probability": {{ example.probability }}
}
```

This example will loop for ${{ example.attempts }}$ of times and will provide the count of how many times a random float is less than ${{ example.probability }}$.


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
