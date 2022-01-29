(() => {
  const btnLogin = document.querySelector("#btn-login");
  const btnCancel = document.querySelector("#btn-cancel");

  const form = document.querySelector("form");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
  });

  const getFormDataValues = () => {
    const formData = new FormData(form);
    const formValues = formData.values();

    const cpf = formValues.next().value;
    const password = formValues.next().value;

    return { cpf, password };
  };

  const validateFormData = () => {
    const data = getFormDataValues();
    const { cpf, password } = data;

    if (!password) return alert("O campo senha não pode estar vazio!");

    if (!cpf) return alert("O campo cpf senha não pode estar vazio!");

    return data;
  };

  btnLogin?.addEventListener("click", () => {
    const data = validateFormData();

    if (!data) return;

    fetch("http://localhost:3000/auth/login", {
      headers: { "Content-Type": "application/json" },
      method: "POST",
      body: JSON.stringify(data),
    })
      .then(async (res) => {
        if (res.status !== 200) throw new Error(await res.text());
        return res.text();
      })
      .then((res) => {
        alert(res);
        location.pathname = "/pages/index.html";
      })
      .catch((res) => {
        alert(res);
      });
  });

  btnCancel?.addEventListener("click", () => {
    location.pathname = "/pages/index.html";
  });
})();
