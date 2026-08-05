console.log("receipt-preview.js loaded");

const fileInput = document.getElementById("receipt-upload");

if (fileInput) {

    fileInput.addEventListener("change", (event) => {

        const file = event.target.files[0];

        if (!file) {
            return;
        }

        const title = document.getElementById("receipt-title");

        if (title) {
            title.textContent = file.name;
        }

       const placeholder = document.getElementById("receipt-placeholder");
const previewImage = document.getElementById("receipt-preview-image");

if (
    placeholder &&
    previewImage &&
    file.type.startsWith("image/")
) {

    placeholder.hidden = true;

    previewImage.src = URL.createObjectURL(file);

    previewImage.hidden = false;

}

    });

}