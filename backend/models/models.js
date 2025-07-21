import pkg from 'pg';
import dotenv from 'dotenv';
dotenv.config();

const { Pool } = pkg;

const pool = new Pool({
  user: process.env.PGUSER,
  host: process.env.PGHOST,
  database: process.env.PGDATABASE,
  password: process.env.PGPASSWORD,
  port: process.env.PGPORT,
});

export async function createUser({ name, email, phone, agency, cluster, password }) {
  const result = await pool.query(
    'INSERT INTO users (name, email, phone, agency, cluster, password) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *',
    [name, email, phone, agency, cluster, password]
  );
  return result.rows[0];
}

export async function getUserByEmail(email) {
  const result = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
  return result.rows[0];
}
