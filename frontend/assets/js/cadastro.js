(() => {
  const btnRecord = document.querySelector("#btn-create-record");
  const btnCancel = document.querySelector("#btn-cancel");

  const form = document.querySelector("form");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
  });

  const getFormDataValues = () => {
    const formData = new FormData(form);
    const formValues = formData.values();

    const name = formValues.next().value;
    const email = formValues.next().value;
    const password = formValues.next().value;
    const passwordConfirm = formValues.next().value;
    const cpf = formValues.next().value;
    const cep = formValues.next().value;
    const street = formValues.next().value;
    const number = formValues.next().value;

    return { name, email, password, passwordConfirm, cpf, cep, street, number };
  };

  const validateFormData = () => {
    const data = getFormDataValues();
    const { name, email, password, passwordConfirm, cpf, cep, street, number } = data;

    if (!name) return alert("O campo nome não pode estar vazio!");

    if (!email) return alert("O campo email não pode estar vazio!");

    if (!password) return alert("O campo senha não pode estar vazio!");

    if (!passwordConfirm) return alert("O campo confirmar senha não pode estar vazio!");

    if (password !== passwordConfirm) return alert("As duas senhas tem que ser idênticas!");

    if (!cpf) return alert("O campo cpf senha não pode estar vazio!");

    if (!cep) return alert("O campo cep senha não pode estar vazio!");

    if (!street) return alert("O campo logradouro senha não pode estar vazio!");

    if (!number) return alert("O campo número senha não pode estar vazio!");

    return data;
  };

  btnRecord?.addEventListener("click", () => {
    const data = validateFormData();
    const { passwordConfirm: _, ...filteredData } = data;

    if (!data) return;

    fetch("http://localhost:3000/users", {
      headers: { "Content-Type": "application/json" },
      method: "POST",
      body: JSON.stringify(filteredData),
    })
      .then(async (res) => {
        if (res.status !== 201) throw new Error(await res.text());
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
