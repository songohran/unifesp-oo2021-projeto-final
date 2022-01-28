(() => {
  const btnRecord = document.querySelector('#btn-create-record');
  const btnCancel = document.querySelector('#btn-cancel');

  btnRecord?.addEventListener('click', (e) => {
    fetch('/users').then((res) => res.json()).then(console.log);
  });
})();
