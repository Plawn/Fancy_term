[Latest Version = 0.16]

##[Installation]

```shell
	pip install Fancy_term
```

##[How to use]

```python
	import Fancy_term
	my_style    = Fancy_term.Style(color=Fancy_term.colors.red,substyle='bold,faded')
	other_style = Fancy_term.Style(color=Fancy_term.colors.blue,substyle='bold')
	
```

#[Optional]

Create an option object :
```python
	options = bar.Progress_bar_options("kill_when_finished",taskname="bar_name")
	some_bar = bar.Progress_bar(options=options)
```
Or
```python
	some_bar = bar.Progress_bar()
	some_bar.set_options(options)
```

#[Others Options]

You can append multiple bars to the handler :
```python
	bar_handler.append(bar1,bar2)
	bar_handler.append([bar1,bar2])
```

#[Methods available]



```python
	#[Progress_bar]
		update(float)	#updates the bar to the float
		set_options(Fancy_Progressbar.Progress_bar_options) #sets options using an option object
		kill_when_finished()	#kill the handler its located in when finished method is called
		style(Fancy_Term.Style)	#sets a style from the Fancy_Term lib
		no_style()	#removes the style
		hide()
		show()
		delete()
		finish()
		current_task(string)	#sets the current task on a second line under the bar
		text(string)	#sets text on a bar
		blank()	#sets a blank bar
		print_bar()	#used by the handler

	#[Progress_bar_options]
		add_argument(*args,**kwargs)
		#can be used to set this options
			# taskname
			# current
			# style
			# max_lenght
			# hidden
			# blank
			# done
			# pointer (not supported yet)
			# kill_when_finished

	#[Progress_bar_handler]
		append()
		remove()
		pause()
		resume()
		kill()
		exchange_by_index(index1,index2) #exchange the order of the bar --> changes display order
		exchange_by_bar(bar1,bar2)
		start() #starts the handler



```
