const url = window.location.href
const quizBox = document.getElementById('quiz-box')


$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: (response)=>{
        console.log(response)
        const data = response.data
        data.forEach(element => {
            for(const [question,answers] of Object.entries(element)){
                quizBox.innerHTML += `
                   <hr>
                   <div class='mb-2'>
                       <b>${question}</b>
                   </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                         <div> 
                             <input type='radio' class='ans'  id='${question}-${answer}' name='${question}' value='${answer}'>
                             <label for="${question}">${answer}</label>
                         </div>
                    `
                })
            }
        });
    },
    error: (error)=>{console.log(error)}
})