import React from 'react';

function OverallStats({ summary }) {
  return (
    <div>
      <h2>Overall Stats</h2>
      <p>Total Picks: {summary.total_picks}</p>
      <p>Correct Picks: {summary.correct_picks}</p>
      <p>Accuracy: {(summary.accuracy * 100).toFixed(2)}%</p>
    </div>
  );
}

export default OverallStats;