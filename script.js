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
});