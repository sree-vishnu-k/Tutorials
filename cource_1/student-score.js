const student=[];
function addstudent(name, score) {
    name=name.trim().toUpperCase();
    score=Number(score);
    score=score ?? 0;
    student.push({ name, score });
}

function getgrades() {
    return student.map(student => {
        let grade="f";
        if (student.score >= 90) grade = "A";
        else if (student.score >= 75) grade = "B";
        else if (student.score >= 60) grade = "C";
        else if (student.score >= 40) grade = "D";  
        else grade = "F";
        return{...student, grade};
        });
}
    
function gettopper() {
    return student.filter(student => student.score >= 90);
}

function tofind(name) {
    return student.find(student => student.name === name);
}

function hasfailed() {
    return student.some(student => student.score < 40);
}



function displaystudents(){;
const grades = getgrades();
console.log("output ");
console.log("all students with grades: ");
console.log("Name\tScore\tGrade");
grades.forEach(student => {
    console.log(`${student.name}\t${student.score}\t${student.grade}`);
});

}


addstudent("Alice", 95);
addstudent("Bob", 82);
addstudent("Charlie", 67);
addstudent("David", 45);
addstudent("Eve", 30); 

displaystudents();
console.log("Topper(s):");
console.log(gettopper());
console.log("Find student by name (Alice):");
console.log(tofind("ALICE"));
console.log("Has any student failed?");
console.log(hasfailed());
