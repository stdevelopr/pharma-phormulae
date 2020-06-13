import React, { useState, useEffect } from "react";
import axios from "axios";

// const functions = {
//   f1: ({ a, b }) => {
//     return a + b;
//   },
//   f2: ({ a, b, c }) => {
//     return a * b * c;
//   }
// };
const Handler = ({ referenceItemDict }) => {
  const [variables, setVariables] = useState({});
  const [result, setResult] = useState("");

  useEffect(() => {
    setVariables({});
    setResult("");
  }, [referenceItemDict]);

  let dict = {};
  const updateVariables = e => {
    // console.log(e.target.value);
    let varName = e.target.getAttribute("varName");
    // console.log(varName);
    let varValue = e.target.value;
    dict = { ...variables };
    dict[varName] = varValue;
    setVariables(dict);
  };

  const calculateResult = () => {
    axios
      .get(`/${referenceItemDict["function_name"]}`, {
        params: variables
      })
      .then(res => setResult(res.data));
    // let f_name = referenceItemDict["function_name"];
    // const result = functions[f_name](variables);
    // setResult(result);
  };

  return (
    <div className="handler-container">
      <div style={{ marginBottom: "30px" }}>
        {referenceItemDict ? referenceItemDict.name : "Formula"}
      </div>
      <div className="handler-description">
        Description: {referenceItemDict ? referenceItemDict.description : ""}
      </div>
      {referenceItemDict &&
        referenceItemDict.variables.map(variable => {
          let var_name = Object.keys(variable)[0];
          return (
            <div key={var_name} className="input-item">
              {/* <div>{var_name}</div> */}
              <div>{variable[var_name]["description"]}</div>
              <input
                type="number"
                // pattern="[0-9.]*"
                step="0.01"
                // placeholder="1.0"
                varname={var_name}
                min="0"
                value={variables[var_name] ? variables[var_name] : ""}
                onChange={updateVariables}
              />
            </div>
          );
        })}

      {referenceItemDict && (
        <button className="calculate-button" onClick={calculateResult}>
          Calculate
        </button>
      )}

      {referenceItemDict && <div className="calculate-result">{result}</div>}
    </div>
  );
};
export default Handler;
