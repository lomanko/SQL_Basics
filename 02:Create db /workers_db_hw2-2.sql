CREATE TABLE IF NOT EXISTS departments(
	id SERIAL PRIMARY KEY,
	department_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS workers(
	id SERIAL PRIMARY KEY,
	worker_name TEXT NOT NULL,
	department_id INTEGER NOT NULL REFERENCES departments(id)
);

CREATE TABLE IF NOT EXISTS workers_bosses(
	id SERIAL PRIMARY KEY,
	worker_id INTEGER NOT NULL REFERENCES workers(id),
	boss_id INTEGER NOT NULL REFERENCES workers(id)
);