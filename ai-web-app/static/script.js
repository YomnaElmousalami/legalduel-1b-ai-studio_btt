
document.getElementById("inputForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const inputText = document.getElementById("inputText").value;
    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: inputText }),
    });

    const result = await response.json();
    const outputElement = document.getElementById("modelOutput");

    if (response.ok) {
        const events = result.summary.split("\n"); // Split by new line
        outputElement.textContent = '';  // Clear previous content

        events.forEach(event => {
            const newLine = document.createElement("p");  // Create a new paragraph element for each event
            newLine.textContent = event; 
            outputElement.appendChild(newLine);  // Append to the output element
        });
    } else {
        outputElement.textContent = result.error || "Something went wrong!";
    }
});

function toggleContent() {
    const showText = document.getElementById("showText").checked;
    const showImage = document.getElementById("showTimeline").checked;

    document.getElementById("textContent").style.display = showText ? "block" : "none";
    document.getElementById("timelineContent").style.display = showImage ? "block" : "none";
}