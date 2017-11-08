data = [
        ['01175163','Golf for Health',1,'A'], ['01200101','Innovative Thinking',1,'A'], ['01204111','Computers & Programming',3,'B+'], ['01355112','Foundation English II',3,'A'], ['01417167','Engineering Mathematics I',3,'B'], ['01420111','General Physics I',3,'B+'], ['01420113','Laboratory in Physics I',1,'C+'], ['01999021','Thai Language for Communication',3,'B+']
]
หน่วยกิต = 0
for วิชา in data:
    print("{}({})   {}".format(วิชา[0],วิชา[2],วิชา[3]))
    หน่วยกิต += วิชา[2]
print("หน่วยกิตรวม =",หน่วยกิต)
