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
    if (response.ok) {
        document.getElementById("modelOutput").textContent = result.summary;
    } else {
        document.getElementById("modelOutput").textContent = result.error || "Something went wrong!";
    }
});