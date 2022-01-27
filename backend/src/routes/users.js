const { Router } = require('express')
const fs = require('fs')
const bcrypt = require('bcrypt')
const { usersDataFilePath, createUsersDataFileIfNotExists } = require('../utils/users')

const usersRouter = Router()

usersRouter.get('/', (_, res) => {
  createUsersDataFileIfNotExists()
  const users = JSON.parse(fs.readFileSync(usersDataFilePath))
  return res.status(200).json(users)
})

usersRouter.get('/:cpf', (req, res) => {
  createUsersDataFileIfNotExists()

  const users = [...JSON.parse(fs.readFileSync(usersDataFilePath))]
  const { cpf } = req.params
  const user = users.find((user) => user.cpf === cpf)

  if (user) {
    return res.status(200).json(user)
  }

  return res.status(404).send('Usuário não encontrado')
})

usersRouter.post('/', async (req, res) => {
  createUsersDataFileIfNotExists()
  const users = [...JSON.parse(fs.readFileSync(usersDataFilePath))]

  if (users.some((user) => user.cpf === req.body.cpf)) {
    return res.status(400).send('CPF já cadastrado')
  }

  const hash = await bcrypt.hash(req.body.senha, 8)

  req.body.senha = hash
  const { confirmar_senha: _, ...user } = req.body
  users.push(user)

  fs.writeFileSync(usersDataFilePath, JSON.stringify(users))

  return res.status(201).send('Cadastro realizado com sucesso!')
})

module.exports = { usersRouter }
