-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Marika Bergman', 'marika.bergman+marika@gmail.com', 'Marik' ,'MOCK'),

   ('Marika', 'marika.bergman@gmail.com', 'Marika' ,'MOCK'),

  ('balboo', 'marika.bergman+balboo@gmail.com', 'balboo', 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'Marik' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  ),
  (
    (SELECT uuid from public.users WHERE users.handle = 'Marika' LIMIT 1),
    'I am the other!',
    current_timestamp + interval '10 day'
  )