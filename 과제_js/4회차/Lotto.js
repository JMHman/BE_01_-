let todayspen = document.querySelector("#today")
let numbersDiv = document.querySelector(".numbers")
let drawButton = document.querySelector("#draw")
let resetButton = document.querySelector("#reset")

let LottoNumbers = []

const today = new Date()
let year = today.getFullYear()
let month = today.getMonth() + 1 //0 부터 시작이기 떄문에 +1 잊지 않기
let date = today.getDate()
todayspen.textContent = `${year}년 ${month}월 ${date}일 `

function paintNumber(number){
    const eachNumDiv = document.createElement("div")
    eachNumDiv.classList.add("eachnum")
    eachNumDiv.textContent = number
    numbersDiv.append(eachNumDiv)
}

drawButton.addEventListener("click",function(){
  if((LottoNumbers.length < 6)){  
    while(LottoNumbers.length < 6){ 
        let rn = Math.floor(Math.random() * 45) + 1
        if(LottoNumbers.indexOf(rn)=== -1){
            LottoNumbers.push(rn)
            paintNumber(rn)
        }
        
    }
    console.log(LottoNumbers)
  } else {
    LottoNumbers.splice(0, 6)
    console.log(LottoNumbers)
    numbersDiv.innerHTML = ""
    
    while(LottoNumbers.length < 6){ 
        let rn = Math.floor(Math.random() * 45) + 1
        if(LottoNumbers.indexOf(rn)=== -1){
            LottoNumbers.push(rn)
            paintNumber(rn)
        }
        
    }  
    console.log(LottoNumbers)
    }       
})

resetButton.addEventListener("click",function(){
    LottoNumbers.splice(0, 6)
    console.log(LottoNumbers)
    numbersDiv.innerHTML = ""
})





