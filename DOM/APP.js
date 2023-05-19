window.onload = function(){
    main();
};

function main(){
    const input = document.getElementById('input-name');
    const addBtn = document.getElementById('add-btn');
    const nameList = document.getElementById('name-list');

    addBtn.addEventListener('click', function (){
        if(input.value){
            const li = document.createElement('li');
            const tittleAttr = document.createAttribute('title');
            tittleAttr.value= 'List Tittle'
        li.innerText = input.value;
        nameList.appendChild(li);
        input.value = '';
        }

    })

}