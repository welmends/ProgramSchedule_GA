# Program Schedule with Genetic Algorithms
Implementation of the Timetable Problem (Program Schedule) with Genetic Algorithms

## Getting started
This repository provides an Python implementation using Jupyter Notebook

### Prerequisites
  - Python 3.5 or newer

### Genetic Algorithm parameters
  -  **maxGeneration**: Maximum amount of generations
  -  **populationSize**: Initial population size
  -  **mutationMethod**: Mutation method: (1) Shift or (2) Shuffle
  -  **problemGoal**: Goals: (1) Teachers, (2) Classrooms or (3) Both
  -  **reproductionRate**: Rate for number of couples used at cross-over

### Program output
Here is presented an output for the program using the following parameters:

  -  **maxGeneration**: 99999999999999999999999999999999999
  -  **populationSize**: 10
  -  **mutationMethod**: 2 *(Shuffle method)*
  -  **problemGoal**: Goals: 3 *(Both teacher and classrooms)*
  -  **reproductionRate**: 0.5 *(Default value)*
  
The [solution](https://github.com/welmends/ProgramSchedule_GA/blob/master/solution_teacher_classroom.txt) is presented below:

```shell
Parameters: GeneticAlgorithm_ProgramSchedule(99999999999999999999999999999999999,10,2,3)
Program: EngComp (10 semesters, 45 courses, 30 teachers, 30 classrooms)
Info: Courses information are complete
> Iteration 1
Fewer collisions so far: 11 (Gen 1)
Fewer collisions so far: 10 (Gen 12)
Fewer collisions so far: 8 (Gen 18)
Fewer collisions so far: 6 (Gen 23)
Fewer collisions so far: 4 (Gen 548)
Fewer collisions so far: 3 (Gen 3193)
Fewer collisions so far: 2 (Gen 9942)
Fewer collisions so far: 1 (Gen 166323)
Fewer collisions so far: 0 (Gen 245232)
> Genetic Algorithm Succeeded (Gen 245232)

|   Segunda      Terca      Quarta      Quinta       Sexta    |
|-------------------------------------------------------------|
|                         Semester  1                         |
|-------------------------------------------------------------|
|   Int-Prog    Log-Mat     Calc-I      Int-Prog    Int-Prog  |
|    Guedes     Eugenia    R. Carlos     Guedes      Guedes   | AB
|    LMC04       LMC09       BC-07       BC-02       LMC04    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|   E-Digit     Calc-I      Log-Mat     E-Digit     E-Digit   |
|     JB       R. Carlos    Eugenia       JB          JB      | CD
|    LMC03       BDI08       BC-05       BC-01       BDI01    |
|-------------------------------------------------------------|
|                         Semester  2                         |
|-------------------------------------------------------------|
|   M-Disc      E-Anal        POO       Calc-II     Fisic-I   |
|   Murilo       Bento      Alisson    F. Macedo   M. Andre   | AB
|    BDI01       BDI05       BC-01       BDI05       LMC02    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|   M-Disc      E-Anal      Fisic-I     Calc-II       POO     |
|   Murilo       Bento     M. Andre    F. Macedo    Alisson   | CD
|    BC-02       BDI02       LMC07       BDI04       BC-06    |
|-------------------------------------------------------------|
|                         Semester  3                         |
|-------------------------------------------------------------|
|     IAA       Aq-Comp     Cc-Elet     E-Dados     Cc-Elet   |
|   Glauber     Alisson      Bento      Ernani       Bento    | AB
|    BC-07       BDI07       BDI07       BC-01       LMC08    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     IAA       Fisic-II    E-Dados     Aq-Comp     Fisic-II  |
|   Glauber     George      Ernani      Alisson     George    | CD
|    BC-06       LMC08       BDI09       BDI02       LMC05    |
|-------------------------------------------------------------|
|                         Semester  4                         |
|-------------------------------------------------------------|
|     ATC        Micro       Micro       GAAL         ATC     |
|   Ernani    Anaxágoras  Anaxágoras  F. Antonio    Ernani    | AB
|    BC-05       BDI01       BC-04       BC-03       BC-07    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|    GAAL        Micro        PO          PO         GAAL     |
| F. Antonio  Anaxágoras    Ronaldo     Ronaldo   F. Antonio  | CD
|    BDI08       BC-08       LMC01       BC-07       BDI06    |
|-------------------------------------------------------------|
|                         Semester  5                         |
|-------------------------------------------------------------|
|     SO          SL         Metod      C-Numer       ---     |
| F. Parente    F. Jose    Cristiane    Glauber       ---     | AB
|    LMC08       BC-05       LMC10       LMC02        ---     |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     SL          SO          BD          BD        C-Numer   |
|   F. Jose   F. Parente     Serra       Serra      Glauber   | CD
|    LMC02       BDI09       BDI05       LMC03       BC-02    |
|-------------------------------------------------------------|
|                         Semester  6                         |
|-------------------------------------------------------------|
|    Redes     Eng-Soft      SEMB      Eng-Soft      SEMB     |
|    Nidia     C. Olavo      Elias     C. Olavo      Elias    | AB
|    BC-09       LMC06       LMC04       BDI10       BC-09    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|  Prob-Est      Redes        ---      Prob-Est      SEMB     |
| C. Alberto     Nidia        ---     C. Alberto     Elias    | CD
|    BDI04       LMC04        ---        BDI10       BC-03    |
|-------------------------------------------------------------|
|                         Semester  7                         |
|-------------------------------------------------------------|
|    IAIC       Grafos        CG         IAIC         ---     |
|   Joacillo    Glauber     Ajalmar     Joacillo      ---     | AB
|    LMC10       LMC03       LMC01       BDI03        ---     |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     IHC         CG          IHC       Grafos        PT      |
|   Hairon      Ajalmar     Hairon      Glauber    Cristiane  | CD
|    BC-04       BDI04       BC-09       BC-03       BC-10    |
|-------------------------------------------------------------|
|                         Semester  8                         |
|-------------------------------------------------------------|
|     STR        ACON         PSI         IC          IC      |
|  P. Regis    P. Regis     Hairon      Ronaldo     Ronaldo   | AB
|    LMC06       BC-06       BC-10       BDI02       BDI03    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     SD         ACON         ---         ---         PSI     |
|   Cidcley    P. Regis       ---         ---       Hairon    | CD
|    BC-08       LMC10        ---         ---        BDI09    |
|-------------------------------------------------------------|
|                         Semester  9                         |
|-------------------------------------------------------------|
|     ---         TCC       E-Gestao      PPD         PPD     |
|     ---       Cidcley     Dijalma     Cidcley     Cidcley   | AB
|     ---        BDI08       LMC07       LMC05       LMC09    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     ---        Opt-1        ---        Opt-1        PPD     |
|     ---       Pedrosa       ---       Pedrosa     Cidcley   | CD
|     ---        BC-02        ---        LMC06       LMC08    |
|-------------------------------------------------------------|
|                         Semester 10                         |
|-------------------------------------------------------------|
|     ---        Opt-3        ---         ---        Opt-2    |
|     ---        Nidia        ---         ---       Pedrosa   | AB
|     ---        BC-04        ---         ---        BDI01    |
| - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - |
|     ---       P-Social     Opt-2       Opt-3       Etica    |
|     ---      Cristiane    Pedrosa      Nidia       Bento    | CD
|     ---        LMC02       LMC05       LMC10       BC-01    |
```
