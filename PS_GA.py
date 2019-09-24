#!/usr/bin/env python
# coding: utf-8

# ### Algoritmos Geneticos para solucionar o problema do escalonamento de horários

# In[1]:


#Import .ipynb as module: %run name.ipynb
import math
import random
import copy


# In[2]:


### Data Structure for the Program Schedule Problem ###

# Macros
WEEK_SIZE         = 5
WEEK_CLASSES_SIZE = 10

# Class Teacher
class Teacher:
    _id = 0
    def __init__(self, name):
        Teacher._id  = Teacher._id +1
        self.id      = Teacher._id
        self.name    = name
        
    def __repr__(self):
        return 'Teacher {}: {}'.format(self.id, self.name)

# Class Classroom
class Classroom:
    _id = 0
    def __init__(self, name):
        if(name==' classroom '):
            self.id = 0
            self.name = name
        else:
            Classroom._id  = Classroom._id +1
            self.id      = Classroom._id
            self.name    = name
        
    def __repr__(self):
        return 'Classroom {}: {}'.format(self.id, self.name)
    
# Class Course
class Course:
    _id = 0
    def __init__(self, name, classes, semester, teacher = None, classroom = None):
        Course._id      = Course._id +1
        self.id         = Course._id
        self.name       = name
        self.classes    = classes
        self.ammo       = classes
        self.semester   = semester
        self.teacher    = teacher
        self.classroom  = Classroom(' classroom ')
        
    def setTeacher(self, teacher):
        self.teacher = teacher
        
    def setClassroom(self, classroom):
        self.classroom = classroom
        
    def __repr__(self):
        if(self.teacher is not None and self.classroom is not None):
            return 'Course {}: {} ({} classes, {}o semester, {} teacher.id, {} classroom.id)'.format(self.id, self.name, self.classes, self.semester, self.teacher.id, self.classroom.id)
        elif(self.teacher is not None):
            return 'Course {}: {} ({} classes, {}o semester, {} teacher.id)'.format(self.id, self.name, self.classes, self.semester, self.teacher.id)
        elif(self.classroom is not None):
            return 'Course {}: {} ({} classes, {}o semester, {} classroom.id)'.format(self.id, self.name, self.classes, self.semester, self.classroom.id)
        else:
            return 'Course {}: {} ({} classes, {}o semester)'.format(self.id, self.name, self.classes, self.semester)
        
# Class Program
class Program:
    def __init__(self, name, semesters):
        self.checked        = False
        self.name           = name
        self.semesters      = semesters
        self.courses        = []
        self.teachers       = []
        self.classrooms     = []
        
    # Utils
    def getCoursesBySemester(self, semester):
        coursesSemester = []
        for i in self.courses:
            if(i.semester is semester and i.ammo > 0):
                coursesSemester.append(i)
        return coursesSemester
    
    def reloadCoursesAmmo(self):
        for i in self.courses:
            i.ammo = i.classes
    
    def getTeacherByName(self, name):
        for teacher in self.teachers:
            if(teacher.name == name):
                return teacher
        return None
    
    def checkCourses(self):
        for course in self.courses:
            if(course.teacher is None):
                print('Info: Courses information are incomplete')
                return False
        print('Info: Courses information are complete')
        return True
    
    # Add/Remove
    def addCourse(self, course):
        try:
            if(course not in self.courses):
                if(sum([c.classes for c in self.getCoursesBySemester(course.semester)])+course.classes<=WEEK_CLASSES_SIZE):
                    self.courses.append(course)
        except:
            return
    
    def removeCourse(self, course):
        try:
            self.courses.remove(course)
        except:
            return
    
    def addTeacher(self, teacher):
        try:
            if(teacher not in self.teachers):
                self.teachers.append(teacher)
        except:
            return
    
    def removeTeacher(self, teacher):
        try:
            self.teachers.remove(teacher)
        except:
            return
        
    def addClassroom(self, classroom):
        try:
            if(classroom not in self.classrooms):
                self.classrooms.append(classroom)
        except:
            return
    
    def removeClassroom(self, classroom):
        try:
            self.classrooms.remove(classroom)
        except:
            return
        
    def __repr__(self):
        return 'Program: {} ({} semesters, {} courses, {} teachers, {} classrooms)'.format(self.name, self.semesters, len(self.courses), len(self.teachers), len(self.classrooms))


# In[3]:


### --- Input Data --- ###
### Program of EngComp ###
engComp = Program('EngComp', 10)

### Teachers ###
teachers = []
teachers.append(Teacher('  Eugenia  '))
teachers.append(Teacher('    JB     '))
teachers.append(Teacher('   Guedes  '))
teachers.append(Teacher('  Joacillo '))
teachers.append(Teacher(' R. Carlos '))
teachers.append(Teacher(' F. Macedo '))
teachers.append(Teacher('F. Antonio '))
teachers.append(Teacher('   Bento   '))
teachers.append(Teacher('  Murilo   '))
teachers.append(Teacher('C. Alberto '))
teachers.append(Teacher(' M. Andre  '))
teachers.append(Teacher('  Alisson  '))
teachers.append(Teacher('  Glauber  '))
teachers.append(Teacher('  Ernani   '))
teachers.append(Teacher('Anaxágoras '))
teachers.append(Teacher('  George   '))
teachers.append(Teacher('  Ronaldo  '))
teachers.append(Teacher('  Ajalmar  '))
teachers.append(Teacher('   Serra   '))
teachers.append(Teacher('F. Parente '))
teachers.append(Teacher('  F. Jose  '))
teachers.append(Teacher(' Cristiane '))
teachers.append(Teacher('   Nidia   '))
teachers.append(Teacher(' C. Olavo  '))
teachers.append(Teacher('   Elias   '))
teachers.append(Teacher('  Hairon   '))
teachers.append(Teacher(' P. Regis  '))
teachers.append(Teacher('  Cidcley  '))
teachers.append(Teacher('  Dijalma  '))
teachers.append(Teacher('  Pedrosa  '))
### Put teachers on program
for teacher in teachers:
    engComp.addTeacher(teacher)

### Classrooms ###
classrooms = []
classrooms.append(Classroom('   BDI01   '))
classrooms.append(Classroom('   BDI02   '))
classrooms.append(Classroom('   BDI03   '))
classrooms.append(Classroom('   BDI04   '))
classrooms.append(Classroom('   BDI05   '))
classrooms.append(Classroom('   BDI06   '))
classrooms.append(Classroom('   BDI07   '))
classrooms.append(Classroom('   BDI08   '))
classrooms.append(Classroom('   BDI09   '))
classrooms.append(Classroom('   BDI10   '))
classrooms.append(Classroom('   BC-01   '))
classrooms.append(Classroom('   BC-02   '))
classrooms.append(Classroom('   BC-03   '))
classrooms.append(Classroom('   BC-04   '))
classrooms.append(Classroom('   BC-05   '))
classrooms.append(Classroom('   BC-06   '))
classrooms.append(Classroom('   BC-07   '))
classrooms.append(Classroom('   BC-08   '))
classrooms.append(Classroom('   BC-09   '))
classrooms.append(Classroom('   BC-10   '))
classrooms.append(Classroom('   LMC01   '))
classrooms.append(Classroom('   LMC02   '))
classrooms.append(Classroom('   LMC03   '))
classrooms.append(Classroom('   LMC04   '))
classrooms.append(Classroom('   LMC05   '))
classrooms.append(Classroom('   LMC06   '))
classrooms.append(Classroom('   LMC07   '))
classrooms.append(Classroom('   LMC08   '))
classrooms.append(Classroom('   LMC09   '))
classrooms.append(Classroom('   LMC10   '))
### Put classrooms on program
for classroom in classrooms:
    engComp.addClassroom(classroom)
    
### Courses ###
courses = []
# 1 Semester
courses.append(Course('  Log-Mat  ',2,1, engComp.getTeacherByName('  Eugenia  ')))
courses.append(Course('  Int-Prog ',3,1, engComp.getTeacherByName('   Guedes  ')))
courses.append(Course('  E-Digit  ',3,1, engComp.getTeacherByName('    JB     ')))
courses.append(Course('  Calc-I   ',2,1, engComp.getTeacherByName(' R. Carlos ')))
# 2 Semester
courses.append(Course('  M-Disc   ',2,2, engComp.getTeacherByName('  Murilo   ')))
courses.append(Course('    POO    ',2,2, engComp.getTeacherByName('  Alisson  ')))
courses.append(Course('  E-Anal   ',2,2, engComp.getTeacherByName('   Bento   ')))
courses.append(Course('  Calc-II  ',2,2, engComp.getTeacherByName(' F. Macedo ')))
courses.append(Course('  Fisic-I  ',2,2, engComp.getTeacherByName(' M. Andre  ')))
# 3 Semester
courses.append(Course('    IAA    ',2,3, engComp.getTeacherByName('  Glauber  ')))
courses.append(Course('  E-Dados  ',2,3, engComp.getTeacherByName('  Ernani   ')))
courses.append(Course('  Cc-Elet  ',2,3, engComp.getTeacherByName('   Bento   ')))
courses.append(Course('  Aq-Comp  ',2,3, engComp.getTeacherByName('  Alisson  ')))
courses.append(Course('  Fisic-II ',2,3, engComp.getTeacherByName('  George   ')))
# 4 Semester
courses.append(Course('    ATC    ',2,4, engComp.getTeacherByName('  Ernani   ')))
courses.append(Course('    PO     ',2,4, engComp.getTeacherByName('  Ronaldo  ')))
courses.append(Course('   Micro   ',3,4, engComp.getTeacherByName('Anaxágoras ')))
courses.append(Course('   GAAL    ',3,4, engComp.getTeacherByName('F. Antonio ')))
# 5 Semester
courses.append(Course('   Metod   ',1,5, engComp.getTeacherByName(' Cristiane ')))
courses.append(Course('  C-Numer  ',2,5, engComp.getTeacherByName('  Glauber  ')))
courses.append(Course('    BD     ',2,5, engComp.getTeacherByName('   Serra   ')))
courses.append(Course('    SL     ',2,5, engComp.getTeacherByName('  F. Jose  ')))
courses.append(Course('    SO     ',2,5, engComp.getTeacherByName('F. Parente ')))
# 6 Semester
courses.append(Course(' Eng-Soft  ',2,6, engComp.getTeacherByName(' C. Olavo  ')))
courses.append(Course(' Prob-Est  ',2,6, engComp.getTeacherByName('C. Alberto ')))
courses.append(Course('   Redes   ',2,6, engComp.getTeacherByName('   Nidia   ')))
courses.append(Course('   SEMB    ',3,6, engComp.getTeacherByName('   Elias   ')))
# 7 Semester
courses.append(Course('    IHC    ',2,7, engComp.getTeacherByName('  Hairon   ')))
courses.append(Course('    CG     ',2,7, engComp.getTeacherByName('  Ajalmar  ')))
courses.append(Course('  Grafos   ',2,7, engComp.getTeacherByName('  Glauber  ')))
courses.append(Course('    PT     ',1,7, engComp.getTeacherByName(' Cristiane ')))
courses.append(Course('   IAIC    ',2,7, engComp.getTeacherByName('  Joacillo ')))
# 8 Semester
courses.append(Course('    PSI    ',2,8, engComp.getTeacherByName('  Hairon   ')))
courses.append(Course('    IC     ',2,8, engComp.getTeacherByName('  Ronaldo  ')))
courses.append(Course('    SD     ',1,8, engComp.getTeacherByName('  Cidcley  ')))
courses.append(Course('    STR    ',1,8, engComp.getTeacherByName(' P. Regis  ')))
courses.append(Course('   ACON    ',2,8, engComp.getTeacherByName(' P. Regis  ')))
# 9 Semester
courses.append(Course('    TCC    ',1,9, engComp.getTeacherByName('  Cidcley  ')))
courses.append(Course('  E-Gestao ',1,9, engComp.getTeacherByName('  Dijalma  ')))
courses.append(Course('    PPD    ',3,9, engComp.getTeacherByName('  Cidcley  ')))
courses.append(Course('   Opt-1   ',2,9, engComp.getTeacherByName('  Pedrosa  ')))
# 10 Semester
courses.append(Course('   Etica   ',1,10,engComp.getTeacherByName('   Bento   ')))
courses.append(Course('  P-Social ',1,10,engComp.getTeacherByName(' Cristiane ')))
courses.append(Course('   Opt-2   ',2,10,engComp.getTeacherByName('  Pedrosa  ')))
courses.append(Course('   Opt-3   ',2,10,engComp.getTeacherByName('   Nidia   ')))
### Put courses on program
for course in courses:
    engComp.addCourse(course)
    
### Print program object
print(engComp)
engComp.checkCourses()


# In[4]:


class Schedule:
    def __init__(self, program):
        # week name list
        self.weekName = ['Segunda', ' Terca ', 'Quarta ', 'Quinta ', ' Sexta ']
        # schedule 3-dimensional list
        self.schedule = list([[[None for z in range((int)(WEEK_CLASSES_SIZE/WEEK_SIZE))] for j in range(WEEK_SIZE)] for i in range(program.semesters)])
        # generate random schedule based on the program (engComp)
        self.generateRandomSchedule(program)
        # reload course ammo to generate another schedule based on the program (engComp)
        program.reloadCoursesAmmo()
    
    def __getitem__(self, key):
        return self.schedule[key]
    
    def __len__(self):
        return len(self.schedule)
    
    # method to generate a random schedule based on courses of the program (engComp)
    def generateRandomSchedule(self, program):
        # create a random list of classrooms
        classroomsCount  = 0
        classroomsRandom = random.sample(range(0,len(program.classrooms)),len(program.classrooms))
        # concatenate the classroomsRandom list with the purpose of classrooms repeat less
        for i in range((WEEK_CLASSES_SIZE*program.semesters)-len(program.classrooms)):
            classroomsRandom.append(classroomsRandom[i%len(program.classrooms)])
        # shuffle classroomsRandom 3 times
        random.shuffle(classroomsRandom)
        random.shuffle(classroomsRandom)
        random.shuffle(classroomsRandom)
        # randomize courses based on each semester
        for semester in range(1, program.semesters+1):
            history = []
            while(True):
                courses = program.getCoursesBySemester(semester)
                if(courses == []):
                    break
                randomCourse = random.choice(courses)
                program.courses[program.courses.index(randomCourse)].ammo-=1
                #Put class on a random place
                while(True):
                    random1 = random.randint(1,WEEK_SIZE)
                    random2 = random.randint(1,(int)(WEEK_CLASSES_SIZE/WEEK_SIZE))
                    if((random1,random2) not in history):
                        history.append((random1,random2))
                        break
                #Put random choosen course
                randomCourseCopy = copy.deepcopy(randomCourse) # copy to change nothing in program
                randomCourseCopy.setClassroom(program.classrooms[classroomsRandom[classroomsCount]])
                classroomsCount+=1
                self.schedule[semester-1][random1-1][random2-1] = randomCourseCopy
        return True
    
    # toString equivalent method
    def __repr__(self):
        ### Week Name
        strOut = '|   '
        for i in self.weekName:
            if i == self.weekName[-1]:
                strOut += i + '   '
            else:
                strOut += i + '     '
        strOut += '|\n'
        for i in range(len(self.schedule)):
            ### Semesters
            strOut += '|-------------------------------------------------------------|\n'
            if(i+1>=10):
                strOut += '|                         ' + 'Semester '  + str(i+1)  + '                         |\n'
            else:
                strOut += '|                         ' + 'Semester  ' + str(i+1)  + '                         |\n'
            strOut += '|-------------------------------------------------------------|\n'
            
            ### Classtime: AB
            # Course Name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][0] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][0].name) + ' '
            strOut += '|\n'
            # Teacher Name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][0] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][0].teacher.name) + ' '
            strOut += '| AB\n'
            # Classroom Name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][0] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][0].classroom.name) + ' '
            strOut += '|\n'
            strOut += '| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |\n'
            ### Classtime: CD
            # Course name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][1] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][1].name) + ' '
            strOut += '|\n'
            # Teacher name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][1] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][1].teacher.name) + ' '
            strOut += '| CD\n'
            # Classroom name
            strOut += '| '
            for j in range(len(self.schedule[i])):
                if(self.schedule[i][j][1] is None):
                    strOut += '    ---     '
                else: 
                    strOut += str(self.schedule[i][j][1].classroom.name) + ' '
            strOut += '|\n'
        return strOut


# In[5]:


class GeneticAlgorithm_ProgramSchedule:
    #|------------------------------- PARAMETERS --------------------------------|
    #| maxGenerations   -> Maximum amount of generations                         |
    #| populationSize   -> Initial population size                               |
    #| mutationMethod   -> Mutation method: (1) Shift or (2) Shuffle             |
    #| problemGoal      -> Goals: (1) Teachers, (2) Classrooms or (3) Both       |
    #| reproductionRate -> Rate for number of couples used at cross-over         |
    #|---------------------------------------------------------------------------|
    def __init__(self, maxGenerations, populationSize, mutationMethod=1, problemGoal=3, reproductionRate=0.5):
        self.maxGenerations    = maxGenerations
        self.populationSize    = populationSize
        self.mutationMethod    = mutationMethod
        self.problemGoal       = problemGoal
        self.couplesSize       = int(self.populationSize*reproductionRate)
        
        self.fitnessResults    = list()
        self.lessCollisions    = WEEK_CLASSES_SIZE**WEEK_CLASSES_SIZE
        
        if(self.mutationMethod is not 1 and self.mutationMethod is not 2):
            self.mutationMethod = 1
        
        if(self.problemGoal is not 1 and self.problemGoal is not 2 and self.problemGoal is not 3):
            self.problemGoal is 3
            
        if(self.problemGoal is 1):
            self.teacherIncrement   = 1
            self.classroomIncrement = 0
        elif(self.problemGoal is 2):
            self.teacherIncrement   = 0
            self.classroomIncrement = 1
        else:
            self.teacherIncrement   = 1
            self.classroomIncrement = 1
        
    def geneticRun(self, program):
        ### Initial Population
        schedulesPopulation = list([Schedule(program) for i in range(self.populationSize)])
        
        ### Iterations
        for generation in range(1,self.maxGenerations+1):
            ### Goal Test [1]
            goalResult = self.goalTest(schedulesPopulation, generation)
            if(goalResult!=-1):
                return '> Genetic Algorithm Succeeded (Gen {})\n\n{}'.format(generation,goalResult),goalResult
            
            ### Evolution (Selection, Cross-Over and Mutation)
            schedulesPopulation_new = list()
            
            ### Selection
            selectedBreeders = self.selection(schedulesPopulation)
            males   = selectedBreeders[:self.couplesSize]
            females = selectedBreeders[self.couplesSize:]
            
            ### Cross-Over
            for m,f in zip(males,females):
                s1,s2 = self.cross_over(m,f)
                schedulesPopulation_new.append(s1)
                schedulesPopulation_new.append(s2)
            
            ### Goal Test [2]
            goalResult = self.goalTest(schedulesPopulation, generation)
            if(goalResult!=-1):
                return '> Genetic Algorithm Succeeded (Gen {})\n\n{}'.format(generation,goalResult),goalResult
            
            ### Mutation
            #Select randomly a individual
            for schedule in schedulesPopulation_new:
                #Probability of mutation happening in each semester
                if(random.randint(0,100)<10):
                    #Update individual after mutation
                    if(self.mutationMethod==1):
                        #Shift method
                        schedule = self.mutation_shift(schedule)
                    else:
                        #Shuffle method
                        schedule = self.mutation_shuffle(schedule)
                    
            ### Update population with better individuals
            schedulesPopulation = schedulesPopulation_new
        return '> Genetic Algorithm Failed',schedulesPopulation[0]
    
    def goalTest(self, schedulePopulation, generation):
        # run fitness method
        self.fitnessResults = list(self.fitness(schedule) for schedule in schedulePopulation)
        #print(list('%.1f' % elem for elem in self.fitnessResults))
        try:
            mininum = min(self.fitnessResults)
            if(mininum<self.lessCollisions):
                self.lessCollisions = mininum
                print('Fewer collisions so far: {} (Gen {})'.format(self.lessCollisions, generation))
            goalIndex = self.fitnessResults.index(0)
            return schedulePopulation[goalIndex]
        except(ValueError):
            return -1
    
    def fitness(self, schedule):
        collisionsCount_teachers   = 0
        collisionsCount_classrooms = 0
        # walk into week (mon-fri) and classtime (AB-CD)
        for week in range(len(schedule[0])):
            for classTime in range(len(schedule[0][0])):
                # each position to compare
                for s_out in range(len(schedule)):
                    for s_in in range(s_out+1,len(schedule)):
                        v_out = schedule[s_out][week][classTime]
                        v_in  = schedule[s_in][week][classTime]
                        if(v_out != None and v_in != None):
                            # verify if has collision - teacher
                            if(v_in.teacher.id==v_out.teacher.id):
                                # increment
                                collisionsCount_teachers+=self.teacherIncrement
                            # verify if has collision - classroom
                            if(v_in.classroom.id==v_out.classroom.id):
                                # increment
                                collisionsCount_classrooms+=self.classroomIncrement
        # return fitness = collisionsCount (less is better)
        return collisionsCount_teachers+collisionsCount_classrooms
    
    def selection(self, schedulePopulation):
        selected = []
        # select 2*couple individuals
        for i in range(2*self.couplesSize):
            ### Using Addicted Roulette to select each individual
            # sum fitness results
            fitnessResSum = sum(self.fitnessResults)
            # separate roulette portions
            roulettePortions = list(1-(f/fitnessResSum) for f in self.fitnessResults)
            # set intervals
            intervals = []
            accum = 0
            for rp in roulettePortions:
                accum+=rp
                intervals.append(round(accum,2))
            # spin addicted roulette
            rouletteResult = random.randint(0,len(schedulePopulation))/len(schedulePopulation)
            # get selected indivitual based on the addicted roulette result
            individual = 0
            while(rouletteResult>intervals[individual]):
                individual+=1
            # append on select list
            selected.append(schedulePopulation[individual])
        # return selected list
        return selected
    
    def cross_over(self, male, female):
        # create copies of male and female
        m   = copy.deepcopy(male)
        f   = copy.deepcopy(female)
        # get a random number of cut
        cut = random.randint(0,len(m)-1)
        # cross-over male and female
        male.schedule   = m.schedule[:cut] + f.schedule[cut:]
        female.schedule = f.schedule[:cut] + m.schedule[cut:]
        # return male and female
        return male,female
    
    def mutation_shift(self, schedule):
        # select semester to mutate
        semesterToMutate = random.randint(0,len(schedule)-1)
        # set gene shift
        geneShift = random.randint(1,WEEK_CLASSES_SIZE-1)
        # get sequential week numbers
        seqWeek = []
        for week in range(len(schedule[0])):
            for classTime in range(len(schedule[0][0])):
                if(schedule[semesterToMutate][week][classTime] is not None):
                    seqWeek.append(schedule[semesterToMutate][week][classTime])
        # shift (geneShift times) the seqWeek list
        for i in range(geneShift):
            last = seqWeek.pop()
            seqWeek.insert(0, last)
        # update shifted list on schedule
        cont = 0
        for week in range(len(schedule[0])):
            for classTime in range(len(schedule[0][0])):
                if(schedule[semesterToMutate][week][classTime] is not None):
                    schedule[semesterToMutate][week][classTime] = seqWeek[cont]
                    cont+=1
        # shift (geneShift times) the seqWeek list and update shifted list on schedule (classrooms)
        if(self.problemGoal==3):
            for i in range(geneShift):
                last = seqWeek.pop()
                seqWeek.insert(0, last)
            cont = 0
            for week in range(len(schedule[0])):
                for classTime in range(len(schedule[0][0])):
                    if(schedule[semesterToMutate][week][classTime] is not None):
                        schedule[semesterToMutate][week][classTime].classroom = seqWeek[cont].classroom
                        cont+=1
        # return schedule
        return schedule
    
    def mutation_shuffle(self, schedule):
        # select semester to mutate
        semesterToMutate = random.randint(0,len(schedule)-1)
        # shuffle the semester's week (courses)
        random.shuffle(schedule[semesterToMutate])
        # shuffle the semester's week (classrooms)
        if(self.problemGoal==3):
            schedule2 = copy.deepcopy(schedule)
            random.shuffle(schedule2[semesterToMutate])
            seq = list()
            cont = 0
            for week in range(len(schedule2[0])):
                for classTime in range(len(schedule2[0][0])):
                    if(schedule2[semesterToMutate][week][classTime] is not None):
                        seq.append(schedule2[semesterToMutate][week][classTime])
            for week in range(len(schedule[0])):
                for classTime in range(len(schedule[0][0])):
                    if(schedule[semesterToMutate][week][classTime] is not None):
                        schedule[semesterToMutate][week][classTime].classroom = seq[cont].classroom      
                        cont += 1
        # return schedule
        return schedule


# In[6]:


#Testing Genetic Algorithm
iteration = 0
print('> Iteration {}'.format(iteration+1))
while True:
    iteration += 1
    GA = GeneticAlgorithm_ProgramSchedule(2000,10,2,1)
    solution,programSchedule = GA.geneticRun(engComp)
    if(solution!='> Genetic Algorithm Failed'):
        print(solution)
        break
    else:
        print('> Iteration {}'.format(iteration+1))

