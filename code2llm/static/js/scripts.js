document.addEventListener("DOMContentLoaded", function () {
    const codeContainer = document.getElementById("code-container");
    const completedChunksContainer = document.getElementById("completed-chunks");
    const toast = document.getElementById("toast");

    fetch("/content")
        .then(response => response.json())
        .then(data => {
            const content = data.content;
            const chunks = content.split(/(?=--- File: )/);

            chunks.forEach(chunk => {
                const chunkDiv = document.createElement("div");
                chunkDiv.className = "chunk";

                const copyButton = document.createElement("button");
                copyButton.className = "copy-btn";
                copyButton.textContent = "Copy";
                copyButton.onclick = () => {
                    navigator.clipboard.writeText(chunk).then(() => {
                        showToast();

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
                    });
                };

                chunkDiv.appendChild(copyButton);

                const pre = document.createElement("pre");
                const code = document.createElement("code");
                code.className = "language-text";
                code.textContent = chunk;
                pre.appendChild(code);
                chunkDiv.appendChild(pre);

                codeContainer.appendChild(chunkDiv);
                Prism.highlightElement(code);
            });
        });

    function showToast() {
        toast.className = "toast show";
        setTimeout(() => { toast.className = "toast"; }, 3000);
    }
});
