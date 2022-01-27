const { Router } = require('express')
const bcrypt = require('bcrypt')
const fs = require('fs')
const { usersDataFilePath, createUsersDataFileIfNotExists } = require('../utils/users')

const authRouter = Router()

authRouter.post('/login', async (req, res) => {
  createUsersDataFileIfNotExists()
  const users = [...JSON.parse(fs.readFileSync(usersDataFilePath))]
  const user = users.find((user) => user.cpf === req.body.cpf)

  if (user) {
    const matchPassword = await bcrypt.compare(req.body.senha, user.senha)

    if (matchPassword) {
      return res.status(200).send('Usuário OK')
    }

    return res.status(401).send('Senha incorreta')
  }

  return res.status(404).send('Usuário não encontrado')
})

module.exports = { authRouter }
