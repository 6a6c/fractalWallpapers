# This program outputs 2560*1600 pngs of Julia sets where the constant term walks around a circle about the origin.
# It took just over one night to run through, and that's with only one thread. Could easily be expanded to
# output pictures quicker. Maybe make one that syncs with temperature for the gradient? IDK.
# Code inspired by a Gekks for Geeks article: https://www.geeksforgeeks.org/julia-fractal-python/

from PIL import Image
from PIL import ImageColor
from math import sin, cos, pi

def main():
    # wd, ht, zoom define the image size and zoom of image
    # pix is some Pillow magic, need to learn this
    # cX, cY are the constatnts in the no nose quation
    # offX, offY are the offset from the origin of the center
    # iters is the desired number of iters

    wd = 2560
    ht = 1600
    zoom = 1

    # grad is the array that gradient of colors is stored in. more iterations before breaking out of function means 
    # being deeper in the gradient. It's really just like 5 gradients duct-taped to each other, so thats why we have
    # all this messy assigning and revesing. hey, it looks cool though

    grad = ["#030645","#061c96","#0b198a","#11177f","#171574","#1c1268","#071268","#0e1268","#161168","#1d1167","#241167","#2b1167","#331167","#3a1067","#411067","#481067","#4f1066","#570f66","#5e0f66"]

    arr = ["#e85657","#e75657","#e65557","#e55556","#e45456","#e35456","#e25356","#e15356","#df5256","#de5255","#dd5155","#dc5155","#db5055","#da4f55","#d94f55","#d84e55","#d74e54","#d64d54","#d54d54","#d44c54","#d34c54","#d24b54","#d14b54","#d04a53","#cf4a53","#ce4953","#cc4853","#cb4853","#ca4753","#c94752","#c84652","#c74652","#c64552","#c54552","#c44452","#c34452","#c24351","#c14351","#c04251","#bf4151","#be4151","#bd4051","#bc4051","#bb3f50","#b93f50","#b83e50","#b73e50","#b63d50","#b53d50","#b43c4f","#b33c4f","#b23b4f","#b13b4f","#b03a4f","#af394f","#ae394f","#ad384e","#ac384e","#ab374e","#aa374e","#a9364e","#a7364e","#a6354d","#a5354d","#a4344d","#a3344d","#a2334d","#a1324d","#a0324d","#9f314c","#9e314c","#9d304c","#9c304c","#9b2f4c","#9a2f4c","#992e4c","#982e4b","#972d4b","#962d4b","#942c4b","#932b4b","#922b4b","#912a4a","#902a4a","#8f294a","#8e294a","#8d284a","#8c284a","#8b274a","#8a2749","#892649","#882649","#872549","#862449","#852449","#842349","#832348","#812248","#802248","#7f2148","#7e2148","#7d2048","#7c2047","#7b1f47","#7a1f47"]
    arr = arr[::-1]
    grad += arr

    arr = ["#fcaf00","#fcaf00","#fcae00","#fbad01","#fbad01","#fbac01","#fbac01","#fbab01","#fbaa01","#fbaa01","#fba901","#faa802","#faa802","#faa702","#faa702","#faa602","#faa502","#faa502","#f9a402","#f9a303","#f9a303","#f9a203","#f9a103","#f9a103","#f9a003","#f8a003","#f89f03","#f89e04","#f89e04","#f89d04","#f89c04","#f89c04","#f89b04","#f79b04","#f79a04","#f79905","#f79905","#f79805","#f79705","#f79705","#f69605","#f69505","#f69505","#f69406","#f69406","#f69306","#f69206","#f69206","#f59106","#f59006","#f59007","#f58f07","#f58f07","#f58e07","#f58d07","#f48d07","#f48c07","#f48b07","#f48b08","#f48a08","#f48908","#f48908","#f48808","#f38808","#f38708","#f38608","#f38609","#f38509","#f38409","#f38409","#f28309","#f28309","#f28209","#f28109","#f2810a","#f2800a","#f27f0a","#f17f0a","#f17e0a","#f17e0a","#f17d0a","#f17c0a","#f17c0b","#f17b0b","#f17a0b","#f07a0b","#f0790b","#f0780b","#f0780b","#f0770b","#f0770c","#f0760c","#ef750c","#ef750c","#ef740c","#ef730c","#ef730c","#ef720d","#ef720d","#ef710d","#ee700d","#ee700d","#ee6f0d","#ee6e0d","#ee6e0d","#ee6d0e","#ee6c0e","#ed6c0e","#ed6b0e","#ed6b0e","#ed6a0e","#ed690e","#ed690e","#ed680f","#ed670f","#ec670f","#ec660f","#ec660f","#ec650f","#ec640f","#ec640f","#ec6310","#eb6210","#eb6210","#eb6110","#eb6010","#eb6010","#eb5f10","#eb5f10","#ea5e11","#ea5d11","#ea5d11","#ea5c11","#ea5b11","#ea5b11","#ea5a11","#ea5a11","#e95912","#e95812","#e95812"]

    arr = arr[::-1]
    grad += arr

    arr = ["#ffd685","#ffd583","#ffd482","#ffd380","#ffd27e","#ffd17c","#fed07b","#fecf79","#fece77","#fecc75","#fecb73","#feca72","#fec970","#fec86e","#fec76c","#fec66a","#fec569","#fec467","#fdc365","#fdc263","#fdc162","#fdc060","#fdbf5e","#fdbe5c","#fdbd5a","#fdbc59","#fdbb57","#fdb955","#fdb853","#fdb751","#fcb650","#fcb54e","#fcb44c","#fcb34a","#fcb249","#fcb147"]

    arr = arr[::-1]
    grad += arr

    arr = ["#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9","#ffd889","#ffe3aa","#ffeec9"]

    grad += arr

    #print(len(grad))

    # thanks PIL!
    png = Image.new("RGB", (wd, ht), "white")
    pix = png.load()

    # offX and offY are offset from origin, keep at 0
    offX, offY = 0.0, 0.0
    # this ensures we don't access past the gradient
    iters = 345

    # creating 2880 images:
    for t in range(2880):
        # we set theta relative to what image we are creating.
        # i.e. img 0 = 0, img 720 = pi/4, and img 1440 = pi
        theta = (t * pi) / (360 * 4)

        # then, we calculate the constant used in the function using Euler's formula
        # .7885 puts the circle in a nice place
        cX = .7885 * cos(theta)
        cY = .7885 * sin(theta)

        # good to leave as a progress bar
        print (theta, cX, cY)

        # creates the image 
        for x in range(wd):
            for y in range(ht):

                zx = 1.5*(x - wd/2)/(0.5*zoom*wd) + offX
                zy = 1.0*(y - ht/2)/(0.5*zoom*ht) + offY
                
                # the julia function itself
                for i in range(iters):
                    if zx * zx + zy * zy >= 4:
                        break

                    tmp = zx*zx - zy*zy + cX
                    zy,zx = 2.0*zx*zy + cY, tmp

                pix[x,y] = ImageColor.getrgb(grad[i])

            # also good progress bar
            print (x, end = "\r")

        # save the image
        fn = "julia/" + " %04s" % t + "julia.png"
        png.save(fn)


if __name__ == "__main__":
    main()
