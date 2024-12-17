const express = require('express');
const User = require('../models/MyUser');
const router = express.Router();
const passport = require("passport");
const auth = require("../middleware/auth");
const { check, validationResult } = require("express-validator");
const debug = require("debug")("app:users");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

// Получить всех пользователей
router.get('/', async (req, res) => {
    try {
        const users = await User.find();
        res.json(users);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Добавить нового пользователя
router.post('/', async (req, res) => {
    const { username, phone_number } = req.body;
    const newUser = new User({ username, phone_number });
    
    try {
        const savedUser = await newUser.save();
        res.status(201).json(savedUser);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Google 
router.get(
    "/google",
    passport.authenticate("google", { scope: ["profile", "email"] })
  );
  router.get(
    "/google/callback",
    passport.authenticate("google", { failureRedirect: "/login" }),
    (req, res) => {
        console.log(req.user.id);
      const token = jwt.sign(
        { user: { id: req.user.id } },
        'fdssdf',
        {
          expiresIn: 3600,
        }
      );
      res.redirect(`http://localhost:3000/?token=${token}`);
    }
  );

// Пользователь сейчас
router.get("/me", auth, async (req, res) => {
    try {
      const user = await User.findById(req.user.id).select("-password");
      res.json(user);
    } catch (err) {
      debug("Server error during fetching user: %O", err);
      res.status(500).json({ msg: "Server error" });
    }
  });

// Удалить пользователя
router.delete('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndDelete(req.params.id);
        if (!user) return res.status(404).json({ message: 'User not found' });
        res.json({ message: 'User deleted' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Логин
router.post(
    "/login",
    [
      check("username", "Username is required").not().isEmpty(),
      check("password", "Password is required").exists(),
    ],
    async (req, res) => {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }
  
      const { username, password } = req.body;
      try {
        const user = await User.findOne({username});
        if (!user) {
          debug("Invalid credentials: %s", username);
          return res.status(400).json({ msg: "Invalid credentials" });
        }
  
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
          debug("Invalid credentials: %s", username);
          return res.status(400).json({ msg: "Invalid credentials" });
        }
  
        const payload = { user: { id: user.id } };
        jwt.sign(
          payload,
          'fdssdf',
          { expiresIn: 3600 },
          (err, token) => {
            if (err) {
              debug("Error signing token: %O", err);
              throw err;
            }
            debug("User logged in successfully: %s", username);
            res.json({ token, user });
          }
        );
      } catch (err) {
        debug("Server error during login: %O", err);
        res.status(500).json({ msg: "Server error" });
      }
    }
  );

// Регистрация
router.post(
    "/register",
    [
      check("username", "Username is required").not().isEmpty(),
      check("password", "Password must be at least 6 characters").isLength({
        min: 6,
      }),
    ],
    async (req, res) => {
      const errors = validationResult(req);
      if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
      }
      const { username, password} = req.body;
      
      try {
        let user = await User.findOne({username});
        
        if (user) {
          debug("User already exists: %s", username);
          return res.status(400).json({ msg: "User already exists" });
        }
        user = new User({ username, password });
        const salt = await bcrypt.genSalt(10);
        user.password = await bcrypt.hash(password, salt); 
        await user.save();
        debug("User registered successfully: %s", username);
        res.status(201).json({ msg: "User registered" });
      } catch (err) {
        debug("Server error during registration: %O", err);
        res.status(500).json({ msg: "Server error" });
      }
    }
  );

module.exports = router;