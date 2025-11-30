function toggleDarkMode() {
  document.documentElement.classList.toggle("dark");
  localStorage.setItem("darkMode", document.documentElement.classList.contains("dark"));
}

// apply saved pref
if (localStorage.getItem("darkMode") === "true") {
  document.documentElement.classList.add("dark");
}
