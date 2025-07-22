import pool from '../db.js';
import bcrypt from 'bcrypt';

export const register = async (req, res) => {
  const { name, email, phone, agency, cluster, password } = req.body;

  try {
    const userExists = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (userExists.rows.length > 0) {
      return res.status(400).json({ error: 'Email already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await pool.query(
      'INSERT INTO users (name, email, phone, agency, cluster, password) VALUES ($1, $2, $3, $4, $5, $6) RETURNING *',
      [name, email, phone, agency, cluster, hashedPassword]
    );

    res.status(201).json({ message: 'User registered successfully', user: newUser.rows[0] });
  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Server error' });
  }
};
