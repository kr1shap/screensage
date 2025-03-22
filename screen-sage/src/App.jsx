import Quiz from "./Quiz";
import {jsQuizz} from "./constants"

function App() {
  //const [count, setCount] = useState(0)

  return (
    <Quiz questions={jsQuizz.questions}/>
  )
}

export default App;
