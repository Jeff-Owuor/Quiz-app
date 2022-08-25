const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.querySelector('#modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener("click", () =>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const NumberOfQuestions = modalBtn.getAttribute('data-questions')
    const testDuration = modalBtn.getAttribute('data-time')

    modalBody.innerHTML =`
        <div class='h5 mb-3'> Are you ready to begin the <b>${name}</b> test? </div>
        <div class='text-muted'>
             <ul> 
                 <li>Difficulty: <b>${difficulty}</b></li>
                 <li>Number of questions: <b>${NumberOfQuestions}</b></li>
                 <li>Score to pass: <b>${scoreToPass}%</b></li>
                 <li>Time: <b>${testDuration}min</b></li>
             </ul>
        </div>
    `
    startBtn.addEventListener("click", ()=>{
        window.location.href = url + pk
    })
}))