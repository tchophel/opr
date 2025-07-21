import express from 'express';
import bcrypt from 'bcrypt';

const router = express.Router();

router.post('/register', async (req, res) => {
  const { name, email, phone, agency, cluster, password } = req.body;
  const pool = req.app.locals.pool;

  if (!name || !email || !phone || !agency || !cluster || !password) {
    return res.status(400).json({ error: "All fields are required." });
  }

  try {
    const existingUser = await pool.query('SELECT id FROM users WHERE email = $1', [email]);
    if (existingUser.rows.length > 0) {
      return res.status(400).json({ error: 'Email already registered' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const result = await pool.query(
      `INSERT INTO users (name, email, phone, agency, cluster, password)
       VALUES ($1, $2, $3, $4, $5, $6)
       RETURNING id`,
      [name, email, phone, agency, cluster, hashedPassword]
    );

    res.status(201).json({ message: 'User registered successfully', userId: result.rows[0].id });
  } catch (error) {
    console.error('Register error:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

export default router;
