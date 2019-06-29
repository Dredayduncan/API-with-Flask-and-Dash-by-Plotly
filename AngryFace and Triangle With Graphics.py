from graphics import *
def main():
    win=GraphWin('Angry Face',500,500)
    win.setBackground('yellow')
    #draw the head using a Circle object
    head=Circle(Point(win.getWidth()/2,win.getHeight()/2),100)
    head.draw(win)
    #draw the left eye using a Circle object
    leftEye=Circle(Point(210,210),15)
    leftEye.draw(win)
    #draw right eye by cloning the left eye and moving clone 80 pixels to the right
    rightEye=leftEye.clone()
    rightEye.move(80,0)
    rightEye.draw(win)
    #draw mouth as a horizontal line
    mouth=Line(Point(230,300),Point(270,300))
    mouth.draw(win)
    #draw nose as a triangle
    #nose=Polygon(Point(250,240),Point(240,260),Point(260,260))
    #nose.draw(win)
    message=Text(Point(win.getWidth()/2,20),'Click on three points')
    message.draw(win)
    p1=win.getMouse()
    p1.draw(win)
    p2=win.getMouse()
    p2.draw(win)
    p3=win.getMouse()
    p3.draw(win)
    nose=Polygon(p1,p2,p3)
    nose.draw(win)

    message.setText('Click anywhere to close')
    win.getMouse()
    win.close()


main()











    #message=Text(Point(win.getWidth()/2,20),'Click on three points')
    #message.draw(win)
    #p1=win.getMouse()
    #p1.draw(win)
    #p2=win.getMouse()
    #p2.draw(win)
    #p3=win.getMouse()
    #p3.draw(win)
    #nose=Polygon(p1,p2,p3)

    #message.setText('Click anywhere to quit')
    #win.getMouse()
    #win.close()

