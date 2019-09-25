let aberto = false;
const sidebar = document.getElementById('sidebar');
const sidebar_helper = document.querySelector('.sidebar-helper');

let sidebarWidth = '275px'
const abrirmenu = () => {
    if (aberto){                
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
        sidebar_helper.style.opacity = 0;
    } else {                
        aberto = true;
        sidebar.style.left = '0';
        sidebar_helper.style.opacity = 1;
    }
}

const footer = document.getElementsByClassName('footer')[0]
function verificaSide() {
    if (window.innerWidth >= 720) {
        sidebar.style.left = '0';
        sidebar_helper.style.opacity = 0;        
        aberto = true;
    } else {
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
        sidebar_helper.style.opacity = 0;        
    }
}