// Clarification - keep track of points and declare winning team

// Approach
/*
	let winningTeam = '';
	loop through the arrays
		check the results at the current index
		store resultNumber
		when gettin the nested array item, we want to index at where result is
		if teams object contains key 'teamName'
			'teamName' += 3
		else 'teamName' = 0
		
		for team in teams 
			loop through them
				find team with largest value
		if statements to add points to whatever team the results array corresponds to	
*/

// psuedoCode

/* 
	let tournamentWinner = '';
	points = 0;
	
	for(let i = 0; i < competitions.length; i++) {
		let outcome = results[i];
		let teams = competitions[i];
		let winningTeam = teams[outcome];
		if(teams[winningTeam]) {
			teams[winningTeam] += 3;
		} else {
			teams[winningTeam] = 0;
		}
	}
	
	for team in teams {
		if(team.value) >= points {
			tournamentWinner = team;
		}
	}
	
	return tournamentWinner;
*/

function tournamentWinner(competitions, results, teams = new Object()) {
   let tournamentWinner = '';
    points = 0;
 
    for(let i = 0; i < competitions.length; i++) {
       let match = competitions[i];
       let outcome = results[i];
       
       if(outcome === 0) {
          winningTeam = match[1]
       } else {
          winningTeam = match[0]
       }
       
       if(!(winningTeam in teams)) {
          teams[winningTeam] = 0;
       } else {
          teams[winningTeam] += 3;
       }
    }
    
    for (team in teams) {
       if(teams[team] >= points) {
          points = teams[team]
          tournamentWinner = team;
       }
    }
 
    return tournamentWinner;
 }
 
 // Do not edit the line below.
 exports.tournamentWinner = tournamentWinner;