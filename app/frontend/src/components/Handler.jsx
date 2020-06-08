import React, { useState, useEffect } from "react";

const functions = {
  f1: ({ a, b }) => {
    return a + b;
  },
  f2: ({ a, b, c }) => {
    return a * b * c;
  }
};
const Handler = ({ referenceItemDict }) => {
  const [variables, setVariables] = useState({});
  const [result, setResult] = useState("");

  useEffect(() => {
    setVariables({});
  }, [referenceItemDict]);

  let dict = {};
  const updateVariables = e => {
    let varName = e.target.getAttribute("varName");
    let varValue = e.target.value;
    dict = { ...variables };
    dict[varName] = parseFloat(varValue);
    setVariables(dict);
  };

  const calculateResult = () => {
    // console.log(referenceItemDict["function_name"]);
    let f_name = referenceItemDict["function_name"];
    const result = functions[f_name](variables);
    setResult(result);
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
        referenceItemDict.variables.map(variable => (
          <div key={variable} className="input-item">
            <div>{variable}</div>
            <input
              varname={variable}
              value={variables[variable] ? variables[variable] : ""}
              onChange={updateVariables}
            />
          </div>
        ))}

      {referenceItemDict && (
        <button className="calculate-button" onClick={calculateResult}>
          Calculate
        </button>
      )}

      {referenceItemDict && (
        <div className="calculate-result">Result: {result}</div>
      )}
    </div>
  );
};
export default Handler;
