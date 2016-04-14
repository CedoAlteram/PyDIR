import tuio, math
print "tuio was imported"
tracking = tuio.Tracking()
print "tuio.Tracking variable assigned"
print "loaded profiles:", tracking.profiles.keys()
print "list functions to access tracked objects:", tracking.get_helpers()
print "Waiting for incoming data", str(tracking.host)  + ":" + str(tracking.port)

previous = None
px = 0
cx = 0
py = 0
cy = 0

try:
    while 1:
        tracking.update()
        #print tracking.update(), "this is tracking update"
        for cur in tracking.cursors():
            #print the location of object, current and previous
            #print id(cur), id(previous)
            cx = cur.xpos
            cy = cur.ypos
            if previous:
                if cx != px or cy != py:
                    #uncomment to find space
                    #print "!"*50
                    dx = cx - px
                    dy = cy - py
                    degs = math.atan2(dx, dy)/math.pi*180
                    print degs, "degs"
            previous = cur
            px = cur.xpos
            py = cur.ypos
except KeyboardInterrupt:
    tracking.stop()
