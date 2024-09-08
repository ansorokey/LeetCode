Select s.machine_id, round(avg(e.timestamp - s.timestamp), 3) as processing_time
from (
    select machine_id, activity_type, timestamp
    FROM activity
    where activity_type = 'start'
) s
JOIN (
    select machine_id, activity_type, timestamp
    FROM activity
    where activity_type = 'end'
) e
ON s.machine_id = e.machine_id
group by s.machine_id;