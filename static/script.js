const toggleButton = document.querySelector('button');
toggleButton.addEventListener('click', async () => {
  const toggleRestAddress = '/toggle';
  await fetch(toggleRestAddress);
})