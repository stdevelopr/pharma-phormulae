import React, { useState } from "react";
import Index from "./Index.jsx";
import Handler from "./Handler.jsx";
import "./styles.css";
import formulas from "./formulas.json";

const App = () => {
  const [selectedItem, setSelectedItem] = useState("");
  return (
    <div>
      <div className="page-title">Pharma-Phormulae</div>
      <div className="container">
        <div className="index-position">
          <Index
            formulas={formulas}
            // referenceItemDict={formulas[selectedItem]}
            selectedItem={selectedItem}
            setSelectedItem={setSelectedItem}
          />
        </div>
        <div className="handler-position">
          <Handler referenceItemDict={formulas[selectedItem]} />
        </div>
      </div>
    </div>
  );
};

export default App;
