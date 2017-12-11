class PostIt(object):
    def __init__(self, background, text, text_color):
        self.background = background
        self.text = text
        self.text_color = text_color

PostIt1 = PostIt("yellow", "Don't forget to clean", "black")
PostIt2 = PostIt("orange", "Don't forget the classes", "black")
PostIt3 = PostIt("Green", "Don't forget your dinner", "black")

print("The background will be: " + PostIt1.background + ", the text will be: " + PostIt1.text + ", and the text color will be: " + PostIt1.text_color + ".")
print("The background will be: " + PostIt2.background + ", the text will be: " + PostIt2.text + ", and the text color will be: " + PostIt2.text_color + ".")
print("The background will be: " + PostIt3.background + ", the text will be: " + PostIt3.text + ", and the text color will be: " + PostIt3.text_color + ".")