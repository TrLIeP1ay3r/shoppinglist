
const Add = document.querySelector('#addPlus');
const ctnt = document.querySelector('#add-item-plate');
var ausgeklappt = false;

function addPage(){
    if(ausgeklappt == false) {
        ctnt.classList.add('her');
        ausgeklappt = true;
    }else {
        ctnt.classList.remove('her');
        ausgeklappt = false;
    }
}