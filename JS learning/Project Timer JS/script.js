
let roundSeconds = parseInt(prompt('🔥 Burn time (seconds): '));
let restSeconds = parseInt(prompt('⚡️ Recharge (seconds): '));
let roundTimes = parseInt(prompt('🛎️ How many rounds: '));

// Calculate total time
let totalTimeSeconds = (roundSeconds + restSeconds) * roundTimes;
let totalTimeMinutes = totalTimeSeconds / 60;

// Display total workout time 
if (totalTimeSeconds >= 60) {
    let minutes = Math.floor(totalTimeSeconds / 60);
    let seconds = totalTimeSeconds % 60;
    console.log(`🔥 Start your ${minutes}m ${seconds}s workout 🔥`);
} else {
    console.log(`🔥 Start your ${totalTimeSeconds} second workout 🔥`);
    console.log(`\n🟠 Get ready for ROUND 1`);
    
    // Initial 
    let countdown = 5;
    let countdownTimer = setInterval(() => {
        console.log(`🟠 in ${countdown} seconds`);
        countdown -= 1;
        if (countdown < 0) {
            clearInterval(countdownTimer);
            startMainWorkout(); 
        }
    }, 1000);  
}

// Main workout function (Python: for loop → JavaScript: recursive function calls)
function startMainWorkout() {
    let currentRound = 1;
    
    function runRound() {
        if (currentRound <= roundTimes) {
            console.log(`\n🟢 ROUND ${currentRound}`);
            
            // Work timer (Python: while loop → JavaScript: setInterval)
            let workTimeLeft = roundSeconds;
            let workTimer = setInterval(() => {
                let minutes = Math.floor(workTimeLeft / 60);
                let seconds = workTimeLeft % 60;
                let secondsFormatted = seconds.toString().padStart(2, '0'); // Python: :02d → JavaScript: padStart()
                console.log(`🟢 ROUND: ${minutes}:${secondsFormatted}`);
                
                workTimeLeft -= 1;
                
                if (workTimeLeft < 0) {
                    clearInterval(workTimer);
                    
                    // Rest period (only if not the last round)
                    if (currentRound < roundTimes) {
                        console.log("\n🔵 REST TIME");
                        
                        let restTimeLeft = restSeconds;
                        let restTimer = setInterval(() => {
                            let minutes = Math.floor(restTimeLeft / 60);
                            let seconds = restTimeLeft % 60;
                            let secondsFormatted = seconds.toString().padStart(2, '0');
                            console.log(`🔵 REST: ${minutes}:${secondsFormatted}`);
                            
                            restTimeLeft -= 1;
                            
                            if (restTimeLeft < 0) {
                                clearInterval(restTimer);
                                currentRound += 1;
                                runRound(); // Start next round
                            }
                        }, 1000);
                    } else {
                        // Workout complete
                        console.log("\n🎉 WORKOUT COMPLETE! 🎉");
                        console.log("Great job! 💪");
                    }
                }
            }, 1000);
        }
    }
    
    runRound(); // Start the first round
}

// If total time is less than 60 seconds, the countdown and workout start automatically
// If total time is 60+ seconds, only the total time is displayed (you'll need to call startMainWorkout() manually)