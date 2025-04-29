document.addEventListener('DOMContentLoaded', function() {
    const positionSelect = document.getElementById('positionSelect');
    const statsContainers = {
        'QB': document.getElementById('qbStats'),
        'RB': document.getElementById('rbStats'),
        'WR': document.getElementById('wrStats')
    };

    // Function to show/hide stat inputs based on position
    function updateStatInputs(position) {
        // Hide all stat containers first
        Object.values(statsContainers).forEach(container => {
            container.style.display = 'none';
        });

        // Show the selected position's stats
        if (statsContainers[position]) {
            statsContainers[position].style.display = 'block';
        }
    }

    // Listen for changes in position selection
    positionSelect.addEventListener('change', (e) => {
        updateStatInputs(e.target.value);
    });

    // Initialize with the default selected position
    updateStatInputs(positionSelect.value);
    
    // Make predict button work
    
document.getElementById("predictButton").addEventListener("click", function () {
    const isQB = document.getElementById("qbStats").style.display !== "none";
    const isRB = document.getElementById("rbStats").style.display !== "none";
    const isWR = document.getElementById("wrStats").style.display !== "none";

    let endpoint = "";
    let params = new URLSearchParams();

    if (isQB) {
        endpoint = "/api/QB_RF";
        params.append("Rate", document.getElementById("Rate").value);
        params.append("QBR", document.getElementById("QBR").value);
        params.append("Cmp.", document.getElementById("Cmp").value);
        params.append("TD", document.getElementById("TD").value);
        params.append("Yds", document.getElementById("Yds").value);
    } else if (isRB) {
        endpoint = "/api/RB_RF";
        params.append("Y.G.Rush", document.getElementById("Y.G.Rush").value);
        params.append("Y.G.Rec", document.getElementById("Y.G.Rec").value);
        params.append("Total.Yds", document.getElementById("Total.Yds").value);
        params.append("T.G", document.getElementById("T.G").value);
        params.append("Rec", document.getElementById("Rec").value);
        params.append("Age", document.getElementById("Age").value);
    } else if (isWR) {
        endpoint = "/api/WR_RF";
        params.append("R.G", document.getElementById("R.G").value);
        params.append("Y.G", document.getElementById("Y.G").value);
        params.append("TD", document.getElementById("TD").value);
    } else {
        alert("Please select a player type first.");
        return;
    }

    // Fetch prediction from API
    fetch(`${endpoint}?${params.toString()}`)
        .then(response => response.json())
        .then(data => {
            const prediction = Number(data.prediction);
            const formatted = prediction.toLocaleString(undefined, {
                style: "currency",
                currency: "USD",
                maximumFractionDigits: 0
            });
            document.getElementById("predictionResult").textContent = `Predicted Salary: ${formatted}`;
        })
        .catch(error => {
            console.error("Error fetching prediction:", error);
            document.getElementById("predictionResult").textContent = "Error fetching prediction.";
        });
  });

});
