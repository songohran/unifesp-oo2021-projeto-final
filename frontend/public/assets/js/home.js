(() => {
  const loadPublicResource = (publicUri) => () => {
    const uri = `/frontend/public/${String(publicUri)}`;
    window.location.pathname = uri;
  };

  const btnRecord = document.querySelector('#btn-create-record');
  const btnLogin = document.querySelector('#btn-login');

  btnRecord?.addEventListener('click', loadPublicResource('cadastro.html'));
  btnLogin?.addEventListener('click', loadPublicResource('login.html'));
})();
