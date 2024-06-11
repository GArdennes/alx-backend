import { createClient, print } from 'redis';

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

function setHashValue(key, field, value) {
  client.hset(key, field, value, print);
}

function displayHashValue(key) {
  client.hgetall(key, (error, result) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(result);
  });
}

setHashValue('HolbertonSchools', 'Portland', 50);
setHashValue('HolbertonSchools', 'Seattle', 80);
setHashValue('HolbertonSchools', 'New York', 20);
setHashValue('HolbertonSchools', 'Bogota', 20);
setHashValue('HolbertonSchools', 'Cali', 40);
setHashValue('HolbertonSchools', 'Paris', 2);

displayHashValue('HolbertonSchools');

