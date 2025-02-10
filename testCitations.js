// Regular Expression Pattern
// You have to create a regular expression pattern to match the given citation formats. The pattern should account for the different formats provided in the examples.

function findCitations(text) {
  // your logic here
}

// Test Cases
console.log(
  findCitations(
    "Pfizer, 2018 (2) SCC 39, it is held that exercise of power by the Central Government under Sections 10A or 26A does not require previous consultation with the DTAB. [23]"
  )
);
// Expected Output: ["2018 (2) SCC 39"]

console.log(
  findCitations("State of H.P., (2018) 1 SCC 202]. Penal Code, 1860 — S. 30")
);
// Expected Output: ["2018 1 SCC 202"]

console.log(
  findCitations(
    "in the Chapter on fundamental rights as embodying a distinct protection, was held not to be good law by an eleven Judge Bench in Rustom Cavasji Cooper vs. Union of India ((1970) 1 SCC 248). Hence, the Petitioners submitted that the basis of the two earlier decisions was not valid. It was also urged that in the seven Judge Bench decision in Maneka Gandhi vs. Union of India ((1978) 1 SCC 248), the minority judgment of Justice Subba Rao in Kharak Singh was specifically approved while the decision of the majority was overruled."
  )
);
// Expected Output: ["1970 1 SCC 248", "1978 1 SCC 248"]

console.log(findCitations("[AIR 2019 SC 1296]. 3. It is also submitted that"));
// Expected Output: ["AIR 2019 SC 1296"]
