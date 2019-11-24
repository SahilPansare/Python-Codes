
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
    
#print(withPole)
def moveDisk(fp,tp):
    print("Move disk from",fp,"to",tp)


moveTower(int(input("\nNumber of bricks : ")),"A","B","C")
