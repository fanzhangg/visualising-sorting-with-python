# Lesson 3 - Insertion Sort

The insertion sort algorithm sorts an unordered list by stepping through the list, removing the unordered item, and then shuffling the other items forward in the list, until the correct position is found for the removed item.

Give a small list such as:

    `[4,3,6,2]`

The first value `4` is ignored. The next value `3` is looked at and compared to the first value `4`. As `4` is larger than `3`, they are swapped.

    `[3,4,6,2]`

Next, `6` is looked at. It is larger than 4 so it is left in place.
To finish off `2` is looked at. As `6` is larger, the pair are swapped.

    `[3,4,2,6]`

`2` is also smaller than `4`, so again, the pair are swapped.

    `[3,2,4,6]`

Finally, it can be seen that `3` is larger than `2` so again, they are swapped

	`[2,3,4,6]`

## Starting off

- Load up your *sorting.py* file from the previous lesson.
- You can comment out the last line of the file, so that the `my_bubble_sort()` function isn't called.

	```python
	#my_bubble_sort(create_random_list(20))
	```

## Sorting one item
- You can start off coding the Insertion Sort algorithm, by sorting a single item in a list.
- Start by creating the list you want to sort

	```python
	some_list = [4,1,3,2]
	```

- Now you can pick an item to sort.

	```python
	i = 3
	```

- Here position 2 has been picked, which is the value `2` in the list. The value `2` needs to be moved down the list until the item to it's left is smaller than it. This can be achieved with a `while` loop.

	```python
	some_list = [4,1,3,2]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
	```

- And i needs to be reduced by 1 each time.
	
	```python

	some_list = [4,1,3,2]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		i -= 1
	```

- Run the code and then type `some_list` into the interpreter to check that the item has been moved.

## Out of range!
- So the algorithm you have coded so far appears to move an item to the correct position in the list. To be sure, you can try with a different list. Edit the file so the list is now:

	```python
	some_list = [4,2,3,1]
	```

- Run the code and see what happens. You should get the error:

	```python
	IndexError: list index out of range
	```

- Why did this happen? Type `i` into the interpreter to see what it's value is.

- Let's use the `display()` function to actually see what is happening.

- Edit your code so that the list is displayed each time there is a move.

	```python
	some_list = [4,2,3,1]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
	```

- If it runs too quickly you can place a `sleep(1)` in your file. You'll need to import the time module at the top of your file as well.

	```python
	from time import sleep

	## All your code

	some_list = [4,2,3,1]

	i = 3

	while some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
		i -= 1
		sleep(1)
	```

- Can you see that the value `1` gets moved to the start of the list, then all the way back round to the end, and back to the start again. It appears as if it is begin sorted twice!

- This occurs because of the way lists can be indexed in Python. Once an item has been moved to *position 0* (so when `i` is `0`), `i` is decreased by `1` and so becomes `-1`.

- In Python the *-1st* element of a list is the last element. Similarly, as `i` continues to reduce it started referencing the *-2nd*, *-3rd*, and *-4th* elements. In this list the *-4th* is also the *0th*. In Python, you can't cycle around again, so when the *-5th* element is attempted to be referenced, an error is thrown.

- To avoid this error, you can just make sure the `while` loop only runs while `i > 0`.

	```python
	some_list = [4,2,3,1]

	i = 3

	while i > 0 and some_list[i-1] > some_list[i]:
		some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
		display(some_list)
		i -= 1
		sleep(1)
	```

## Finishing the Insertion Sort

- Now that you have code that can shift any given element in a list, from right to left, until it meets an element smaller than it, you can easily finish off the Insertion Sort.

- All you need to do it to use the algorithm you have written, on every element of the list, from the *1st* to the last. A `for` loop is the perfect way of doing this.

	```python
	some_list = [4,2,3,1]

	for i in range(1,len(some_list)):
			while i > 0 and some_list[i-1] > some_list[i]:
				some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
				i -= 1
				display(some_list)
	```

- Run this to watch your Insertion Sort working.

- Now you can wrap it all in a function, and call it, just like you did with the Bubble Sort.

	```python
	def my_insertion_sort(some_list):
		for i in range(1,len(some_list)):
			while i > 0 and some_list[i-1] > some_list[i]:
				some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
				i-=1
				display(some_list)
		return some_list

	my_insertion_sort(create_random_list(100))
	```

