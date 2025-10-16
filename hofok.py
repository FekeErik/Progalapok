vizho=int(input("Adjon meg egy hőmérsékletet!!"))

if(vizho<0):
    print("A víz szilárd.")
elif(vizho>0 and vizho<100):
    print("A víz folyékony")
elif(vizho>100):
    print("a víz gáz")