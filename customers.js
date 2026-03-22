import { supabase } from './supabaseClient.js'

export async function createCustomer(customer) {
  const { data, error } = await supabase
    .from('customers')
    .insert([customer])
    .select()

  return { data, error }
}