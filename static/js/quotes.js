const form = document.getElementById("quoteForm");
const API_URL = "/quotes";
const button = document.getElementById("btn");
const cardContainer = document.querySelector(".cardContainer");
if (form) {
  form.addEventListener("submit", (e) => {
    const { author, category, body } = form;
    button.classList.add("loading");
    addQuote({
      author: author.value,
      category: category.value,
      body: body.value,
    });
    e.preventDefault();
  });
}

async function addQuote(dataObj) {
  axios
    .post(API_URL, dataObj)
    .then((data) => {
      button.classList.remove("loading");
      ShowSuccess("Quote added Successfully");
    })

    .catch((er) => {
      button.classList.remove("loading");
      const { field, message } = er.response.data;
      const res = `${field} : ${message}`;
      ShowError(res);
    });
}

async function DeleteQuote(id) {
  axios
    .delete(`${API_URL}/${id}`)
    .then((res) => {
      ShowSuccess("Quote Deleted Successfully");
    })
    .catch((err) => {
      ShowError(err.response.data.message);
    });
}
function ShowError(message) {
  const out = document.getElementById("errorMessage");
  const errorContainer = document.querySelector(".errorContainer");
  out.textContent = message;
  errorContainer.style.display = "block";
  setTimeout(() => {
    errorContainer.style.display = "none";
  }, 1000);
}
function ShowSuccess(message) {
  const out = document.getElementById("successMessage");
  const successContainer = document.querySelector(".successContainer");
  out.textContent = message;
  successContainer.style.display = "block";
  setTimeout(() => {
    successContainer.style.display = "none";
    window.location.reload();
  }, 1000);
}
