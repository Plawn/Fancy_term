[Latest Version = 0.10]

## [Installation]

```shell
	pip install Fancy_term
```

## [How to use]

```python
	import Fancy_term
	my_style    = Fancy_term.Style(color=Fancy_term.colors.red,substyle='bold,faded')
	other_style = Fancy_term.Style(color=Fancy_term.colors.blue,substyle='bold')
	sprint = Fancy_term.Smart_print()
	sprint.use(my_style)
	sprint("test")	#apply style to string
	sprint.set(other_style)	#sets a style for future use
	sprint.reset()	#removes the styles
```

### [Colors and substyles available]
```python
	Colors_available    = ["red","white","green","yellow","purple","rose","blue","reset"]
	Substyles_available = ["bold","faded","less_faded","underligned","blinking","background","normal"]

	#you can print it by typing :
	 	print(Fancy_term.Colors_available)
		print(Fancy_term.Substyles_available)

```
### [Methods available]


```python
	#[Smart_print]
		use(Fancy_term.Style) #sets a style for the printer
		set(Fancy_term.Style) #sets a style for future prints
		reset()
		__call__(string) #prints the string using the selected style
```
### [Functions available]
```python
	#[printc]
		printc(string, Fancy_term.Style) #prints string using the Style
```

This library is compatible with the Fancy_progressbar library
