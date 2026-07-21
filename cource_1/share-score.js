const share=[];
function addShare(stock, price) {
    price=Number(price);
    price=price ?? 0;
    stock=stock.trim().toUpperCase();
    share.push({stock, price});
}
function getgrades() {
   return share.map((share) => {
        let grade ="F";
        if (share.price >= 90)grade = 'A';
        else if (share.price >= 80) grade = 'B';
        else if (share.price >= 60) grade = 'C';
        else if (share.price >= 40) grade = 'D';
        else grade = 'F';
        
        return { ...share, grade };
    });
}

function getTopper() {
    return share.filter((share) => share.price >= 75);
}

function findShare(stock) {
    return share.find((share) => share.stock === stock);
}

function hasfailed() {
    return share.some((share) => share.price < 40);
}
function displayShares() {
    const grades = getgrades();
    console.log("All Shares:");
    console.log("All Shares with Grades");
    console.log("Stock\tPrice\tGrade");
    grades.forEach((share) => {
        console.log(`${share.stock}\t${share.price}\t${share.grade}`);
    });
}

addShare("AAPL", 85);
addShare("GOOGL", 92);
addShare("MSFT", 78);
addShare("AMZN", 55);
addShare("TSLA", 35);

displayShares();
console.log("Topper Shares:");
console.log(getTopper());
console.log("\nFind Shares:");
console.log(findShare("GOOGL"));
console.log("\nFailed Shares:");
console.log(hasfailed() ? "There are shares that have failed." : "No shares have failed.");
