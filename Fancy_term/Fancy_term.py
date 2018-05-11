# <-------------- colors --------------> #

class _colors:
	def __init__(self):
		self._beginning = "\033["
		self.red    = "31;10m"
		self.white  = "00;10m"
		self.green  = "32;400m"
		self.yellow = "33;40m"
		self.purple = "34;40m"
		self.rose   = "35;40m"
		self.blue   = "36;36m"
		self.reset  =  self._beginning + self.white
		self.end    = "\033[m"

colors = _colors()

Colors_available    = ["red","white","green","yellow","purple","rose","blue","reset"]
Substyles_available = ["bold","faded","less_faded","underligned","blinking","background","normal"]
# <-------------- colors --------------> #

def sprint(string,style):
	print(style.str(),string,colors.end,sep="")


class Smart_print:
	"""
		Can be used to set a style or directly used as a print function
	"""
	def __init__(self,*args,**kwargs):
		self.actual_style = None
		self.up = '\x1b[1A'
		self._reset = colors.reset
		self.end = "\033[m"
	def set(self,*style):
		"""
			Sets a Style for future use : Should work with any printable stuff
		"""
		if len(style) > 0 :
			print(self.up,style(),sep="")
			self.actual_style = style[0]
		else :
			print(self.end,self.actual_style.str(),self.up,sep='')
	def use(self,style):
		self.actual_style = style
	def reset(self):
		print(self.up,self._reset,sep="")
		self.actual_style = None
	def end(self):
		print(self.up+self._reset,sep="")
		self.actual_style = None
	def __call__(self,string):
		try:
			print(self.end,self.actual_style.str(),string,self.end,sep="")
		except:
			raise ValueError("no style defined")


class Style:
	"""
		Colors    available by typing print(Colors_available)
		Substyles available by typing print(Substyles_available)
	"""
	def __init__(self,*args,**kwargs):
		self._sub_styles = {"bold":"1","faded":"2","less_faded":"3","underligned":"4","blinking":"5","background":"7","normal":"0"}
		self._beginning  = "\033["
		self.default     = 'normal'
		self.bold        = kwargs.get(self.default, True)
		self._color      = kwargs.get('color', colors.red)
		self._sub_style  = self._sub_styles.get(kwargs.get('substyle', self.default))
		self._gen_substyle(kwargs.get('substyle', self.default))
		self.end = "\033[m"
	def str(self):
		return(self.end+self._beginning+self._sub_style+self._color)
	def __call__(self):
		return(self.end+self._beginning+self._sub_style+self._color)
	def __str__(self):
		return(self.end+self._beginning+self._sub_style+self._color)
	def __repr__(self):
		return(self._beginning[1:]+self._sub_style+self._color)
	def _gen_substyle(self,sub_styles):
		styles          = sub_styles.split(",")
		L_styles        = []
		self._sub_style = ""
		for style in styles :
			try:
				L_styles.append(int(self._sub_styles[style]))
			except:
				print(str(style),"not a valid format")
		L_styles.sort()
		for i in L_styles:
			self._sub_style += str(i) + ";"


# <-------------- test unit --------------> #
if __name__ == '__main__':
	red = "\033[" + "0;" + colors.red
	print('\x1b[1A'+red)
	print("bob")


	my_style = Style(color=colors.blue,substyle='blinking')

	c = Color_changer()


	# print(String("test").color(colors.green))
	print("not green")
	c.set(my_style)

	print("red")
	c.reset()
	print("reseted")

	c.reset()

# <-------------- test unit --------------> #





