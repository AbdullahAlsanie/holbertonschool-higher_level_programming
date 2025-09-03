--  lists all shows
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_shows_genres AS tg
on ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
