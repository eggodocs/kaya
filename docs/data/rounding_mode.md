---
numbers:
    example1: 3.54
    example2: 2.87
    example3: 1.34
    example4: 1.0
    example5: -1.0
    example6: -1.23
    example7: -2.34
    example8: -3.86
---


#   Rounding Mode

A [string][string] that determines how a [float][float] is rounded off.


### Values

Value | Description
------|------------
`up` | Rounds the value away from zero, where the digit prior to a non-zero value is incremented.
`down` | Rounds the value towards zero, where the float is truncated to the specified decimal places.
`ceiling` | Rounds the value towards positive infinity. If the value is positive, it behaves like `up` and if it's negative, it behaves like `down`.
`floor` | Rounds the value towards negative infinity. If the value is positive, it behaves like `down` and if it's negative, it behaves like `up`.
`half_up` | Rounds the value towards the "nearest neighbor" unless both neighbors are equidistant, in which case, it'll be rounded up.<br>Behaves like `up` if the digit is $\gtrapprox 0.5$, otherwise, it behaves like `down`.
`half_down` | Rounds the value towards the "nearest neighbor" unless both neighbors are equidistant, in which case, it'll be rounded down.<br>Behaves like `up` if the digit is $\gt 0.5$, otherwise, it behaves like `down`.
`half_even` | Rounds the value towards the "nearest neighbor" unless both neighbors are equidistant, in which case, it'll round towards the even neighbor.<br>Behaves like `half_up` if the digit to the left is odd, otherwise, it behaves like `half_down` if it's even.


### Examples

=== "`up`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ round_up(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ round_up(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ round_up(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ round_up(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ round_up(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ round_up(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ round_up(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ round_up(numbers.example8) }}$

=== "`down`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ round_down(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ round_down(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ round_down(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ round_down(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ round_down(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ round_down(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ round_down(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ round_down(numbers.example8) }}$
    
=== "`ceiling`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ ceil(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ ceil(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ ceil(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ ceil(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ ceil(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ ceil(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ ceil(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ ceil(numbers.example8) }}$

=== "`floor`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ floor(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ floor(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ floor(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ floor(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ floor(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ floor(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ floor(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ floor(numbers.example8) }}$

=== "`half_up`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ round_half_up(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ round_half_up(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ round_half_up(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ round_half_up(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ round_half_up(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ round_half_up(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ round_half_up(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ round_half_up(numbers.example8) }}$

=== "`half_down`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ round_half_down(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ round_half_down(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ round_half_down(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ round_half_down(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ round_half_down(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ round_half_down(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ round_half_down(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ round_half_down(numbers.example8) }}$

=== "`half_even`"

    Input | Rounded off to 1 digit
    ------|------------
    ${{ numbers.example1 }}$ | ${{ round_half_even(numbers.example1) }}$
    ${{ numbers.example2 }}$ | ${{ round_half_even(numbers.example2) }}$
    ${{ numbers.example3 }}$ | ${{ round_half_even(numbers.example3) }}$
    ${{ numbers.example4 }}$ | ${{ round_half_even(numbers.example4) }}$
    ${{ numbers.example5 }}$ | ${{ round_half_even(numbers.example5) }}$
    ${{ numbers.example6 }}$ | ${{ round_half_even(numbers.example6) }}$
    ${{ numbers.example7 }}$ | ${{ round_half_even(numbers.example7) }}$
    ${{ numbers.example8 }}$ | ${{ round_half_even(numbers.example8) }}$
