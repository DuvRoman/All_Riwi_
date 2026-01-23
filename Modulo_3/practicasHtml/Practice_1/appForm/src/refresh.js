// export async function setupCounter(element) {
//   let counter = 0
//   const setCounter = (count) => {
//     counter = count
//     element.innerHTML = `count is ${counter}`
//   }
//   element.addEventListener('click', () => setCounter(counter + 1))
//   setCounter(0)
// }

export async function refresh(namePage) {

  const url = namePage 
  try {
        const  response = await fetch(url) 
        const  data = await response.text()
        localStorage.setItem('contentPage', data)
        return data
    } catch (error) {
        console.error(error);
    }
}