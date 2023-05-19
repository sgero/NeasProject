// // Detecta si el usuario tiene el modo oscuro preferido en su sistema operativo
// const prefersDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
//
// // Obtiene el botón de alternar modo oscuro
// const darkModeToggle = document.getElementById('dark-mode-toggle');
//
// // Función para cambiar el modo oscuro
// function toggleDarkMode() {
//   // Obtiene el elemento <link> que carga el archivo CSS del modo oscuro
//   const darkModeCSS = document.getElementById('dark-mode-css');
//
//   // Alterna la existencia de la clase 'dark-mode' en el elemento <link>
//   darkModeCSS.href = darkModeCSS.href.includes('dark-mode') ? '{% static "basic-page.css" %}' : '{% static "dark-mode.css" %}';
// }
//
// // Asigna un evento de clic al botón de alternar modo oscuro
// darkModeToggle.addEventListener('click', toggleDarkMode);
//
// // Si el usuario prefiere el modo oscuro, cambia al modo oscuro de inmediato
// if (prefersDarkMode) {
//   toggleDarkMode();
// }

const body = document.querySelector('body');
      sidebar = body.querySelector('.sidebar');
      toggle = body.querySelector('.toggle');
      searchBtn = body.querySelector('.search-box .bx-search');
      modeSwitch = body.querySelector('.toggle-switch');
      modeText = body.querySelector('.mode-text');

      toggle.addEventListener('click', () => {
          body.classList.toggle('close');
      });

            modeSwitch.addEventListener('click', () => {
          body.classList.toggle('dark');

          if(body.classList.contains('dark')){
              modeText.innerText = 'Modo de día';
            }else{
              modeText.innerText = 'Modo Oscuro';
            }

      });


