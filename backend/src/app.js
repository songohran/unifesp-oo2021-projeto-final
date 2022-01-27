const express = require('express')
const app = express()
const path = require('path')

app.use(express.json())
app.use(express.urlencoded({ extended: true }))

app.use('/frontend/public', express.static(path.resolve(__dirname, '..', '..', 'frontend', 'public')))

app.use('/', (_, res) => {
  res.redirect('/frontend/public')
})

module.exports = { app }
