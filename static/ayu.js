function calculateDosha() {
    // Get all the quiz questions (h3 elements)
    const questions = document.querySelectorAll('h3');
    
    // Initialize counters for each dosha option for each question
    let doshaCounts = {
        'vatta': 0,
        'pitta': 0,
        'kapha': 0
    };
    
    // Loop through the questions to count the selected options
    questions.forEach((question, index) => {
        const selectedOption = document.querySelector(`input[name="q${index + 1}"]:checked`);
        if (selectedOption) {
            doshaCounts[selectedOption.value]++;
        }
    });

    // Determine which dosha has the maximum count
    let maxCount = Math.max(doshaCounts.vatta, doshaCounts.pitta, doshaCounts.kapha);
    let resultDosha = '';

    // Check for a tie between two doshas
    const doshasWithMaxCount = Object.keys(doshaCounts).filter(dosha => doshaCounts[dosha] === maxCount);
    if (doshasWithMaxCount.length === 2) {
        resultDosha = doshasWithMaxCount.join('_'); // Concatenate the two doshas with an underscore
    } else if (doshasWithMaxCount.length === 3) {
        // All three doshas have the same count
        resultDosha = 'balanced'; // You can change this to any other appropriate value or redirect to a separate page
    } else {
        resultDosha = doshasWithMaxCount[0]; // Only one dosha has the maximum count
    }

    // Redirect the user to the appropriate page based on the result
    if (resultDosha === 'balanced') {
        window.location.href = `result_${resultDosha}.html`; // You can change this to any other appropriate value or redirect to a separate page
    } else {
        window.location.href = `result_${resultDosha}.html`;
    }
}


















