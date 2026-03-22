import { createCustomer } from './customers.js'

async function test() {
  const { data, error } = await createCustomer({
    name: 'Cliente via customers.js'
  })

  console.log('DATA:', data)
  console.log('ERROR:', error)
}

test()