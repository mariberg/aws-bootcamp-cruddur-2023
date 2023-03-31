SELECT
    users.uuid,
    users.handle,
    users.diplay_name
FROM public.users
WHERE
    users.handle = %(handle)s