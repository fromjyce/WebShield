import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NavbarComponent from "./components/NavbarComponent";
import BodyComponent from "./components/BodyComponent";
import PhishSearch from "./components/PhishSearch";

function App() {
  return (
    <Router>
      <NavbarComponent />
      <Routes>
        <Route path="/" element={<BodyComponent />} />
        <Route path="/phishsearch" element={<PhishSearch />} />
      </Routes>
    </Router>
  );
}

export default App;
