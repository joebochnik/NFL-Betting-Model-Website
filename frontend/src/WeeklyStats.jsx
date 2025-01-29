import React from 'react';

function WeeklyStats({ summary }) {
  const weeks = Object.keys(summary)
                      .filter(key => key.startsWith('week_'))
                      .map(week => ({
                          week: summary[week].week,
                          accuracy: summary[week].accuracy,
                          correct_picks: summary[week].correct_picks,
                          total_picks: summary[week].total_picks
                      }));

  return (
    <div>
      <h2>Weekly Stats</h2>
      <table className='table table-bordered table-striped'>
        <thead className='thead-dark'>
          <tr>
            <th>Week</th>
            <th>Total Picks</th>
            <th>Correct Picks</th>
            <th>Accuracy</th>
          </tr>
        </thead>
        <tbody>
          {weeks.map(week => (
            <tr key={week.week}>
              <td>Week {week.week}</td>
              <td>{week.total_picks}</td>
              <td>{week.correct_picks}</td>
              <td>{(week.accuracy * 100).toFixed(2)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default WeeklyStats;
