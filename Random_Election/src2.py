import random

def main():
    list=[]
    for i in range(0, 1001):
        list.append(random.randint(0, 6))
    apaar=list.count(0)
    swamy = list.count(1)
    souradeep = list.count(2)
    devyanshi = list.count(3)
    riya = list.count(4)
    ankur = list.count(5)
    nikhil = list.count(6)

    print("Apaar's total = "+str(apaar))
    print("Swamy's total = " + str(swamy))
    print("Souradeep's total = " + str(souradeep))
    print("Devyanshi's total = " + str(devyanshi))
    print("Riya's total = " + str(riya))
    print("Ankur's total = " + str(ankur))
    print("Nikhil's total = " + str(nikhil)+"\n")

    dict1 = { apaar: 'Apaar',  swamy: 'Swamy', souradeep : 'Souradeep', devyanshi : 'Devyanshi',  riya : 'Riya', ankur : 'Ankur',  nikhil: 'nikhil'}

    print ("The winner is "+(dict1.get(max(dict1)))+", Congrats on being the Proud owner of the repository.")



if __name__ == "__main__":
    main()

