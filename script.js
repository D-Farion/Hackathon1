
const dropBox = document.getElementById("dropBox");
const fileInput = document.getElementById("fileInput");

dropBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropBox.classList.add("dragover");
});

dropBox.addEventListener("dragleave", () => {
    dropBox.classList.remove("dragover");
});

dropBox.addEventListener("drop", (e) => {
    e.preventDefault();
    dropBox.classList.remove("dragover");

    const file = e.dataTransfer.files[0];
    if (file && file.type === "application/pdf") {
        alert(`"${file.name}" selected.\n(This will be sent to Google Calendar in the full app.)`);
    } else {
        alert("Please upload a PDF file.");
    }
});




const fileBtn = document.getElementById("fileBtn");
const fileName = document.getElementById("fileName");

fileBtn.addEventListener("click", () => {
    fileInput.click();
});

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        fileName.textContent = fileInput.files[0].name;
    } else {
        fileName.textContent = "No file selected";
    }
});
