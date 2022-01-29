(() => {
  const btnRecord = document.querySelector('#btn-create-record');
  const btnLogin = document.querySelector('#btn-login');

  btnRecord?.addEventListener('click', () => {
    location.pathname = '/pages/cadastro.html';
  });

  btnLogin?.addEventListener('click', () => {
    location.pathname = '/pages/login.html';
  });
})();
