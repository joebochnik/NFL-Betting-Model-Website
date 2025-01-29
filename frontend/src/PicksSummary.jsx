import React, { useState, useEffect } from 'react';
import OverallStats from './OverallStats.jsx';
import WeeklyStats from './WeeklyStats.jsx';
function PicksSummary() {
    const [summary, setSummary] = useState(null);

    useEffect(() => {
        async function fetchData() {
            const response = await fetch('http://127.0.0.1:5000/get_picks');
            const data = await response.json();
            setSummary(data);
        }
        fetchData();
    }, []);

    if (!summary) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>Season {summary.season} Picks Summary</h1>
            <OverallStats summary={summary} />
            <WeeklyStats summary={summary} />
        </div>
    );
}
export default PicksSummary;
