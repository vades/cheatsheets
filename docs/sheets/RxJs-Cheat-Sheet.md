# RxJS Most Used Operators

This cheat sheet provides a quick reference for most used RxJS operators. However, RxJS offers many more operators with various functionalities that can be explored in the official documentation.

| Operator | Description | Example |
|----------|-------------|---------|
| `map` | Applies a transformation to each emitted value | `source$.pipe(map(value => value * 2))` |
| `filter` | Filters out values based on a condition | `source$.pipe(filter(value => value > 0))` |
| `mergeMap` | Maps each value to an Observable, then flattens the inner Observables | `source$.pipe(mergeMap(value => fetchData(value)))` |
| `concatMap` | Maps each value to an Observable, and concatenates the results in order | `source$.pipe(concatMap(value => fetchData(value)))` |
| `switchMap` | Maps each value to an Observable, discarding previous inner Observables | `source$.pipe(switchMap(value => fetchData(value)))` |
| `debounceTime` | Emits a value after a specified duration of silence | `source$.pipe(debounceTime(300))` |
| `distinctUntilChanged` | Emits values only if they are different from the previous value | `source$.pipe(distinctUntilChanged())` |
| `take` | Emits only the first n values from the source Observable | `source$.pipe(take(5))` |
| `takeUntil` | Emits values until a second Observable emits a value | `source$.pipe(takeUntil(stop$))` |
| `combineLatest` | Combines multiple Observables into one, emitting an array of the latest values | `combineLatest(source1$, source2$).subscribe(([value1, value2]) => console.log(value1, value2))` |
| `zip` | Combines multiple Observables into one, emitting an array of corresponding values | `zip(source1$, source2$).subscribe(([value1, value2]) => console.log(value1, value2))` |
| `retry` | Re-subscribes to the source Observable a specified number of times after an error | `source$.pipe(retry(3))` |
| `catchError` | Catches errors and replaces them with a fallback Observable or value | `source$.pipe(catchError(error => of(fallbackValue)))` |
| `tap` | Performs a side effect without modifying the emitted values | `source$.pipe(tap(value => console.log(value)))` |
| `startWith` | Emits a specified value before the source Observable starts emitting | `source$.pipe(startWith(initialValue))` |
| `pluck` | Extracts a specified nested property from each emitted object | `source$.pipe(pluck('name'))` |
| `finalize` | Performs a specified action when the source Observable completes or errors | `source$.pipe(finalize(() => console.log('Completed')))` |
| `skip` | Skips the first n values emitted by the source Observable | `source$.pipe(skip(3))` |
| `bufferTime` | Collects values emitted within a specified time window into an array | `source$.pipe(bufferTime(1000))` |
| `share` | Shares a single subscription among multiple subscribers | `source$.pipe(share())` |


