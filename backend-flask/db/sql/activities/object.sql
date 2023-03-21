SELECT 
    activities.uuid,
    users.diplay_name,
    users.handle,
    activities.message,
    activities.created_at,
    activities.expired_at
FROM public.activities
INNER JOIN public.users ON users.uuid = activities.user_uuid
WHERE
    activities.uuid = %(uuid)s