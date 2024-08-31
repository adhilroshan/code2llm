document.addEventListener("DOMContentLoaded", function () {
    const codeContainer = document.getElementById("code-container");
    const completedChunksContainer = document.getElementById("completed-chunks");
    const toast = document.getElementById("toast");
    const loadingScreen = document.getElementById("loading-screen");
    const container = document.querySelector(".container");

    // Fetch content from the server
    fetch("/content")
        .then(response => response.json())
        .then(data => {
            const content = data.content;
            const chunks = content.split(/(?=--- File: )/);

            chunks.forEach(chunk => {
                createChunkElement(chunk);
            });

            // Hide loading screen and show content
            loadingScreen.style.display = "none";
            container.style.display = "block";
        })
        .catch(error => {
            console.error("Error fetching content:", error);
            showToast("Failed to load content.", true);
            loadingScreen.innerHTML = "<p>Failed to load content. Please try again later.</p>";
        });

    function createChunkElement(chunk) {
        const chunkDiv = document.createElement("div");
        chunkDiv.className = "chunk";

        const copyButton = document.createElement("button");
        copyButton.className = "copy-btn";
        copyButton.textContent = "Copy";
        copyButton.onclick = () => handleCopy(chunk, chunkDiv);

        chunkDiv.appendChild(copyButton);

        const pre = document.createElement("pre");
        const code = document.createElement("code");
        code.className = "language-text";
        code.textContent = chunk;
        pre.appendChild(code);
        chunkDiv.appendChild(pre);

        codeContainer.appendChild(chunkDiv);
        Prism.highlightElement(code);
    }

    function handleCopy(chunk, chunkDiv) {
        navigator.clipboard.writeText(chunk)
            .then(() => {
                showToast("Copied to clipboard!");

                const completedItemDiv = document.createElement("div");
                completedItemDiv.className = "copied-item";

                const pre = document.createElement("pre");
                const code = document.createElement("code");
                code.className = "language-text";
                code.textContent = chunk;
                pre.appendChild(code);
                completedItemDiv.appendChild(pre);

                completedChunksContainer.appendChild(completedItemDiv);

                Prism.highlightElement(code);

                // Remove the copied chunk from the original container
                codeContainer.removeChild(chunkDiv);
            })
            .catch(error => {
                console.error("Error copying to clipboard:", error);
                showToast("Failed to copy to clipboard.", true);
            });
    }

    function showToast(message, isError = false) {
        toast.textContent = message;
        toast.style.backgroundColor = isError ? "#e53e3e" : "#38b2ac";
        toast.className = "toast show";
        setTimeout(() => { toast.className = "toast"; }, 3000);
    }
});
