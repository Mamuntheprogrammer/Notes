const panels = document.querySelectorAll('.panel')

panels.forEach((panel)=>{
    panel.addEventListener('click',()=>{
        removeActiveClasees()
        panel.classList.add('active')

    })
})

function removeActiveClasees(){
    panels.forEach((panel)=>{
        panel.classList.remove('active')
    })
}