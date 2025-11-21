File1=input("Enter the source filen to be copied")
File2=input("Enter the destion file name")

Fr=open(File1,"r")
Fw=open(File2,"w")

for line in Fr.readlines():
    Fw.write(line)
Fr.close()
Fw.close()
