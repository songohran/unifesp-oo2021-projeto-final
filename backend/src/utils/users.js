const fs = require('fs')
const path = require('path')

const usersDataFilePath = path.resolve(__dirname, '..', 'db', 'users.json')

const createUsersDataFileIfNotExists = () => {
  if (!fs.existsSync(usersDataFilePath)) {
    fs.writeFileSync(usersDataFilePath, '[]')
  }
}

module.exports = {
  usersDataFilePath,
  createUsersDataFileIfNotExists
}
