const toggleButton = document.querySelector('button');
toggleButton.addEventListener('click', async () => {
  const toggleRestAddress = 'http://192.168.43.253:80/toggle';
  const toggleRequest = await fetch(toggleRestAddress);
})