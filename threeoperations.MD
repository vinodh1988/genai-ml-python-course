# Map, Filter, and Reduce Notes

## Map
- **Purpose:** Transforms each element in an array.
- **Syntax:** `array.map(callback)`
- **Example:**
    ```js
    const numbers = [1, 2, 3];
    const doubled = numbers.map(n => n * 2); // [2, 4, 6]
    ```

## Filter
- **Purpose:** Selects elements that match a condition.
- **Syntax:** `array.filter(callback)`
- **Example:**
    ```js
    const numbers = [1, 2, 3, 4];
    const even = numbers.filter(n => n % 2 === 0); // [2, 4]
    ```

## Reduce
- **Purpose:** Reduces array to a single value.
- **Syntax:** `array.reduce(callback, initialValue)`
- **Example:**
    ```js
    const numbers = [1, 2, 3, 4];
    const sum = numbers.reduce((acc, n) => acc + n, 0); // 10
    ```

## Summary Table

| Operation | Purpose         | Returns      |
|-----------|----------------|--------------|
| map       | Transform      | New array    |
| filter    | Select         | New array    |
| reduce    | Aggregate      | Single value |

