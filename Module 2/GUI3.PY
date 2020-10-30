from tkinter import * 
print("Use the buttons below to create shapes and drag them. If you have a custom button, enter the name \n followed by a comma followed by the height and width (in feet) comma separated followed by a \n color into the text box and click create. Example: lamp,1,1,pink \n \n")
root = Tk()
global width
global height
global widthr
global heightr
global order
order = list()
width = (float)(input("Enter the width of your room: "))
height = (float)(input("Enter the length of your room: "))
width = (width)
height = (height)
if width>height:
	widthr = 502
	heightr = (502*height/width)
	canvas = Canvas(root, width=widthr, height=heightr)
	# canvas.create_rectangle(3,3,widthr,heightr, outline="#4a4a4a", width = 4)
else:
	heightr = 502
	widthr = (500*width/height)+2
	canvas = Canvas(root, width=widthr, height=heightr)
	# canvas.create_rectangle(2,2,widthr,heightr, outline="#4a4a4a", width = 4)

canvas.pack()
def make_bed1(x=10,y=2):
	h = 6
	w = 3
	nh = h*heightr/height
	nw = w*widthr/width
	Bed = canvas.create_rectangle(x,y,x+nw,y+nh, outline="blue", width = 4)
	order.append("bed")
def make_bed2(x=10,y=2):
	bedh = 3
	bedw = 6
	nbedh = bedh*heightr/height
	nbedw = bedw*widthr/width
	Bed2 = canvas.create_rectangle(x,y,x+nbedw,y+nbedh, outline="blue", width = 4)
	order.append("bed")
def make_desk(x=20,y=2):
	h = 1.5
	w = 3
	nh = h*heightr/height
	nw = w*widthr/width
	desk = canvas.create_rectangle(x,y,x+nw,y+nh, outline="brown", width = 4)
	order.append("desk")
def make_wardrobe(x=30,y=2):
	h = 2
	w = 3
	nh = h*heightr/height
	nw = w*widthr/width
	ward = canvas.create_rectangle(x,y,x+nw,y+nh, outline="red", width = 4)
	order.append("ward")
def make_door_vert(x=40,y=2):
	h = 2.6
	w = 0.3
	nh = h*heightr/height
	nw = w*widthr/width
	door = canvas.create_rectangle(x,y,x+nw,y+nh, outline="green", width = 4)
	order.append("door")
def make_door_horizontal(x=40,y=2):
	h = 0.3
	w = 2.6
	nh = h*heightr/height
	nw = w*widthr/width
	door2 = canvas.create_rectangle(x,y,x+nw,y+nh, outline="green", width = 4)
	order.append("doorh")
Button(root, text='Bed', command=make_bed1).pack()
Button(root, text='Bed Horizontal', command=make_bed2).pack()
Button(root, text='Desk', command=make_desk).pack()
Button(root, text='Wardrobe/closet', command=make_wardrobe).pack()
Button(root, text='Door Vertical', command=make_door_vert).pack()
Button(root, text='Door Horizontal', command=make_door_horizontal).pack()

class MouseMover():
  def __init__(self):
    self.item = 0; self.previous = (0, 0)
  def select(self, event):
    widget = event.widget                       
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]  
    self.previous = (xc, yc)
    print((xc, yc, self.item))
  def drag(self, event):
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
    self.previous = (xc, yc)

mm = MouseMover()
canvas.bind("<Button-1>", mm.select)
canvas.bind("<B1-Motion>", mm.drag)

textentry = Entry(root)
textentry.pack()
def getvals ():  
	x1 = textentry.get()
	x = x1.split(',')
	a = (str)(x[0])
	print(a)
	b = (float)(x[1])
	# print(b)
	c = (float)(x[2])
	# print(c)
	d = (str)(x[3])
	# print(d)

	nh = b*heightr/height
	nw = c*widthr/width
	order.append(a)
	canvas.create_rectangle(150,2,150+nw,2+nh, outline=d, width = 4)

def getvals2 ():  
	print()
	print(widthr, heightr)
	for i in range(len(order)):
		print(order[i])
		print(canvas.coords(i+1))
	print()
	f = open("floorplan_1.txt", "w")
	f.write("1000	1000\n4")
	length1 = "\n0	0	0	" + (str)(round(heightr)) + "	11	11"
	length2 = "\n0	0	" + (str)(round(widthr)) +"	0"+ "	11	11"
	length3 = "\n0	" + (str)(round(heightr)) + "	" + (str)(round(widthr)) + "	" + (str)(round(heightr))+ "	11	11"
	length4 = "\n"  + (str)(round(widthr)) + "	0" + "	" + (str)(round(widthr)) + "	" + (str)(round(heightr))+ "	11	11\n"
	print(length1, length2,length3, length4)
	f.write(length1 + length2 + length3 + length4)
	entrance = ""
	for i in range(len(order)):
		topush = ""
		name = order[i]
		tempo = canvas.coords(i+1)
		count = 0
		keep = tempo[0]
		keep1 = tempo[1]
		for i in tempo:
			tem = (str)(round(i))
			if(count==2 and name=="door"):
				tem = (str)(round(keep))
			if(count==3 and name=="doorh"):
				tem = (str)(round(keep1))
				name = "door"
			topush = topush + tem + "	"
			count+=1
		if name == "door":
			entrance = topush + "entrance	1	1"
		topush = topush + name + "	1	1\n"
		f.write(topush)
	if(len(entrance)==0):
		entrance = "5	113	5	217	entrance	1	1"	
	f.write(entrance)
	f.close()


buttoncreate = Button(text='Create', command=getvals)
buttoncreate.pack()
buttoncreate = Button(text='Save', command=getvals2)
buttoncreate.pack()
mainloop()
