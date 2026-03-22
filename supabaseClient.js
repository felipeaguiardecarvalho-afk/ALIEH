
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = `https://egnhskijionwpbrszlzr.supabase.co`
const supabaseKey = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVnbmhza2lqaW9ud3BicnN6bHpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxNDcxMzgsImV4cCI6MjA4OTcyMzEzOH0.NnIR90S4mDFUVfM0N9Ph-fvOPSy9L6luTXaWjkZSPWQ`

export const supabase = createClient(supabaseUrl, supabaseKey)
