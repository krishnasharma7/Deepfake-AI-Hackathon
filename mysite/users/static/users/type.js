// Function to fade in the title
function fadeInTitle() {
    var title = document.getElementById("title");
    title.style.display = "block";
    title.style.opacity = 0;

    var fadeEffect = setInterval(function () {
        if (!title.style.opacity) {
            title.style.opacity = 0;
        }
        if (parseFloat(title.style.opacity) < 1) {
            title.style.opacity = parseFloat(title.style.opacity) + 0.1;
        } else {
            clearInterval(fadeEffect);
            typewriter(); // Start typing animation after title fades in completely
        }
    }, 100);
}

// set up text to print, each item in array is new line
var aText = [
    "Unmasking reality, one frame at a time and empowering truth in the age of deepfakes. Guarding authenticity in a digital era, where truth meets technology. Defending reality in a world of deception."
];
var iSpeed = 50; // time delay of print out
var iIndex = 0; // start printing array at this position
var iArrLength = aText[0].length; // the length of the text array
var iScrollAt = 20; // start scrolling up at this many lines

var iTextPos = 0; // initialise text position
var sContents = ''; // initialise contents variable
var iRow; // initialise current row

function typewriter() {
    sContents = ' ';
    iRow = Math.max(0, iIndex - iScrollAt);
    var destination = document.getElementById("typedtext");

    while (iRow < iIndex) {
        sContents += aText[iRow++] + '<br />';
    }
    destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "_";
    if (iTextPos++ == iArrLength) {
        iTextPos = 0;
        iIndex++;
        if (iIndex != aText.length) {
            iArrLength = aText[iIndex].length;
            setTimeout("typewriter()", 500);
        } else {
            showButtons(); // After typing animation ends, show buttons
        }
    } else {
        setTimeout("typewriter()", iSpeed);
    }
}


// Call fadeInTitle function when the window is loaded
window.onload = function () {
    fadeInTitle();
};
