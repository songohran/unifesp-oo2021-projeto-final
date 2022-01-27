const express = require('express')
const app = express()
const path = require('path')
const { usersRouter } = require('./routes/users')
const { authRouter } = require('./routes/auth')

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use('/frontend/public', express.static(path.resolve(__dirname, '..', '..', 'frontend', 'public')))

app.use('/users', usersRouter)
app.use('/auth', authRouter)

app.use('/', (_, res) => {
  res.redirect('/frontend/public')
})

module.exports = { app }
