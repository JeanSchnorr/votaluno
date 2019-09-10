let aberto = false;
const sidebar = document.getElementById('sidebar');

let sidebarWidth = '275px'
const abrirmenu = () => {
    if (aberto){                
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
        
    } else {                
        sidebar.style.left = '0';
        aberto = true;
    }
}

const footer = document.getElementsByClassName('footer')[0]
function verificaSide() {
    if (window.innerWidth >= 720) {
        sidebar.style.left = '0';
        aberto = true;
    } else {
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
    }
}
