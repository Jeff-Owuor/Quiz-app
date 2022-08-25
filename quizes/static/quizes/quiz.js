const url = window.location.href

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: (response)=>{console.log(response)},
    error: (error)=>{console.log(error)}
})