import { createClient } from 'redis';

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

client.on('ready', () => {
  const channelName = 'holberton school channel';

  client.subscribe(channelName, (err, count) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    console.log(`Subscribed to channel: ${channelName} (Channels subscribed: ${count})`);
  });

  // Listen for messages on the subscribed channel
  client.on('message', (channel, message) => {
    console.log(`Received message: ${message}`);
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channelName, (err, count) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        console.log(`Unsubscribed from channel: ${channelName}`);
        client.quit();
      });
    }
  });
});

