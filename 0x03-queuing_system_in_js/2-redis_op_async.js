import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error);
});

client.connect().catch((error) => {
  console.error('Redis client not connected to the server:', error);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

main();

