const HDWalletProvider = require('truffle-hdwallet-provider');
const fs = require('fs');
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*"
    },
    greenticks2019: {
      network_id: "*",
      gas: 0,
      gasPrice: 0,
      provider: new HDWalletProvider(fs.readFileSync('/Users/aadilmehdi/Hackathons/2019/CodeFunDo/GreenTicks/dumbContracts/config.env', 'utf-8'), "https://greenticks.blockchain.azure.com:3200/zyI5vxdSZFpWyLmYATqjBqtD"),
      consortium_id: 1564681916105
    }
  },
  mocha: {},
  compilers: {
    solc: {
      version: "0.5.0"
    }
  }
};
