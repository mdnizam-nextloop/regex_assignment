 Regular Expressions
A) Write a regular expression pattern that can catch any of the SCC or AIR citation formats in a string, as an example resource, here are some sample formats https://main.sci.gov.in/pdf/ECT/journal2.pdf. Given a string, return a list of all citation substrings. Also account for complexity in journal names in the above, eg “2018 (1) SCC 202, AIR 2018 SC (CRIMINAL) 97”

Test case 1: 

Pfizer, 2018 (2) SCC 39, it is held that exercise of power by the Central Government under Sections 10A or 26A does not require previous consultation with the DTAB. [23]

A: [2018 (2) SCC 39]


Test case 2:

State of H.P., (2018) 1 SCC 202]. Penal Code, 1860 — S. 30

A: [2018 1 SCC 202]


Test case 3:

in the Chapter on fundamental rights as embodying a distinct protection, was held not to be good law by an eleven Judge Bench in Rustom Cavasji Cooper vs. Union of India ((1970) 1 SCC 248). Hence, the Petitioners submitted that the basis of the two earlier decisions was not valid. It was also urged that in the seven Judge Bench decision in Maneka Gandhi vs. Union of India ((1978) 1 SCC 248), the minority judgment of Justice Subba Rao in Kharak Singh was specifically approved while the decision of the majority was overruled. 

A: [1970 1 SCC 248, 1978 1 SCC 248] or [1 SCC 248, 1 SCC 248] are OK

Test case 4: 

[AIR 2019 SC 1296]. 3. It is also submitted that

A: [AIR 2019 SC 1296]


B) Write a function that returns the above but accepting spelling errors using Levenshtein distances or similar.

Test case 1:

Pfizer, 2018 (2) SCCC 39, it is held that exercise of power by the Central Government under Sections 10A or 26A does not require previous consultation with the DTAB. [23]

A: [(2) SCCC 39]

Test case 2:

[AIIR    2019 SC 1296]. 3. It is also submitted that

A: [AIIR    2019 SC 1296]
