
function showFileName() {
    const fileInput = document.getElementById("file_upload");
    const fileLabel = document.getElementById("file_label");

    if (fileInput.files.length > 0) {
        // Update label with the file name and make it smaller
        fileLabel.textContent = fileInput.files[0].name;
        fileLabel.classList.add("file-selected");  // Add class for smaller text
    } else {
        // If no file selected, keep the "+" symbol
        fileLabel.textContent = "+";
        fileLabel.classList.remove("file-selected");  // Remove class to reset size
    }
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("file_upload").addEventListener("change", showFileName);
});