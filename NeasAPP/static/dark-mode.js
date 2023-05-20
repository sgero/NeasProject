// const body = document.querySelector('body');
// const sidebar = body.querySelector('.sidebar');
// const toggle = body.querySelector('.toggle');
// const searchBtn = body.querySelector('.search-box .bx-search');
// const modeSwitch = body.querySelector('.toggle-switch');
// const modeText = body.querySelector('.mode-text');
//
//       toggle.addEventListener('click', () => {
//           sidebar.classList.toggle('close');
//       });
//
//       searchBtn.addEventListener('click', () => {
//           sidebar.classList.remove('close');
//       });
//
//
//
//       modeSwitch.addEventListener('click', () => {
//           body.classList.toggle('dark');
//
//           if(body.classList.contains('dark')){
//               modeText.innerText = 'Modo de día';
//             }else{
//               modeText.innerText = 'Modo Oscuro';
//             }
//
//       });





// const body = document.querySelector('body');
// const sidebar = body.querySelector('.sidebar');
// const toggle = body.querySelector('.toggle');
// const searchBtn = body.querySelector('.search-box .bx-search');
// const modeSwitch = body.querySelector('.toggle-switch');
// const modeText = body.querySelector('.mode-text');
//
// if (toggle && sidebar) {
//   toggle.addEventListener('click', () => {
//     sidebar.classList.toggle('close');
//   });
// }
//
// if (searchBtn && sidebar) {
//   searchBtn.addEventListener('click', () => {
//     sidebar.classList.remove('close');
//   });
// }
//
// if (modeSwitch && body && modeText) {
//   modeSwitch.addEventListener('click', () => {
//     body.classList.toggle('dark');
//
//     if (body.classList.contains('dark')) {
//       modeText.innerText = 'Modo de día';
//     } else {
//       modeText.innerText = 'Modo Oscuro';
//     }
//   });
// }
//




const body = document.querySelector('body');
const sidebar = body.querySelector('.sidebar');
const toggle = body.querySelector('.toggle');
const searchBtn = body.querySelector('.search-box .bx-search');
const modeSwitch = body.querySelector('.toggle-switch');
const modeText = body.querySelector('.mode-text');

// Función para guardar el estado del modo oscuro en el localStorage
const saveDarkModeState = (darkModeEnabled) => {
  localStorage.setItem('darkModeEnabled', darkModeEnabled);
};

// Función para cargar el estado del modo oscuro del localStorage
const loadDarkModeState = () => {
  const darkModeEnabled = localStorage.getItem('darkModeEnabled');
  if (darkModeEnabled === 'true') {
    body.classList.add('dark');
    modeText.innerText = 'Modo de día';
  } else {
    body.classList.remove('dark');
    modeText.innerText = 'Modo Oscuro';
  }
};

// Verificar si el modo oscuro está guardado en el localStorage y cargarlo al cargar la página
loadDarkModeState();

if (toggle && sidebar) {
  toggle.addEventListener('click', () => {
    sidebar.classList.toggle('close');
  });
}

if (searchBtn && sidebar) {
  searchBtn.addEventListener('click', () => {
    sidebar.classList.remove('close');
  });
}

if (modeSwitch && body && modeText) {
  modeSwitch.addEventListener('click', () => {
    body.classList.toggle('dark');

    if (body.classList.contains('dark')) {
      modeText.innerText = 'Modo de día';
      saveDarkModeState(true);
    } else {
      modeText.innerText = 'Modo Oscuro';
      saveDarkModeState(false);
    }
  });
}




//
// // SIDEBAR
//
// // ...
//
// // Función para guardar el estado del sidebar en el sessionStorage
// const saveSidebarState = (isOpen) => {
//   sessionStorage.setItem('sidebarOpen', isOpen);
// };
//
// // Función para cargar el estado del sidebar del sessionStorage
// const loadSidebarState = () => {
//   const sidebarOpen = sessionStorage.getItem('sidebarOpen');
//   if (sidebarOpen === 'true') {
//     sidebar.classList.remove('close');
//   } else {
//     sidebar.classList.add('close');
//   }
// };
//
// // Verificar si el estado del sidebar está guardado en el sessionStorage y cargarlo al cargar la página
// loadSidebarState();
//
// // ...
//
// if (toggle && sidebar) {
//   toggle.addEventListener('click', () => {
//     sidebar.classList.toggle('close');
//     saveSidebarState(!sidebar.classList.contains('close'));
//   });
// }
//
// // ...
