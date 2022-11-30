import math
import turtle

#this was going to be a donut but i cant be bothered

def applymatrix(vec, mx,my,mz):
    x = [vec[0] * mx[0], vec[0] * mx[1], vec[0] * mx[2]]
    y = [vec[1] * my[0], vec[1] * my[1], vec[1] * my[2]]
    z = [vec[2] * mz[0], vec[2] * mz[1], vec[2] * mz[2]]
    result = [x[0] + y[0] + z[0],x[1] + y[1] + z[1],x[2] + y[2] + z[2]]
    return result #oh lord


ang = 0
ang2 = 1

circle = []


for circleang in range(0,45): #construct disc(s)
    for i in range(0,30):
        ca = (circleang/45)*math.pi*2
        
        dot = applymatrix([(math.sin(i/2)*4)+7,(math.cos(i/2)*4),0],
                          [math.cos(ca),0,math.sin(ca)],
                          [0,1,0],
                          [-math.sin(ca),0,math.cos(ca)])
        
        circle.append(dot)


def find(dots,x,y):
    found = False
    for d in dots:
        if math.floor(d[0]) == x-15 and math.floor(d[1]) == y-15:
            found = True
    return found

turtle.speed(999)
turtle.tracer(0,0)
while True:
    ang += 0.03 
    ang2 += 0.01

    dots = [] ##store the rotated points
    
    for dot in circle:
        res = dot
        #apply x and y rotation
        res = applymatrix(res ,
                          [1,0,0],
                          [0,math.cos(ang),math.sin(ang)],
                          [0,-math.sin(ang),math.cos(ang)])
        
        res = applymatrix(res,
                          [math.cos(ang2),0,math.sin(ang2)],
                          [0,1,0],
                          [-math.sin(ang2),0,math.cos(ang2)])
        
        dots.append(res)

    turtle.clear()
    for newdot in dots:
        turtle.setpos(newdot[0]*30,newdot[1]*30)
    turtle.update()


    #world = ""
    
    #for x in range(0,30): #draw simple 30x30 orthographic view
     #   world = world + "\n"
     #   for y in range(0,30):
      #      if find(dots,x,y):
      #          world = world + "##"
      #      else:
       #         world = world + "  "

                
    #print("\n"*100)#clear screen
    #print(world)
    
