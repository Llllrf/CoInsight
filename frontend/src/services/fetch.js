async function fetchPOST(url, payload, context) {
  const data = payload.data;
  const type = payload.type;

  try {
    context.commit("setLoading", true);
    let headers = {};
    if (type === "form") {
    } else if (type === "json") {
      headers["Content-Type"] = "application/json";
    }
    let response = await fetch(url, {
      method: "POST",
      headers: headers,
      body: data,
    });
    let responseData = await response.json();

    if (!response.ok) {
      throw new Error(
        responseData.message ? responseData.message : "RESPONSE ERROR"
      );
    }
    context.commit("setError", {
      state: false,
      message: "",
    });
    context.commit("setLoading", false);
    context.dispatch("handleData", responseData);
  } catch (error) {
    context.commit("setError", {
      state: true,
      message: error.message,
    });
    context.commit("setLoading", false);
    console.error("error:", error.message);
  }
}

async function fetchGET(url, payload, context) {
  // const data = payload.data;

  try {
    context.commit("setLoading", true);

    let response = await fetch(url, {
      method: "GET",
    });
    let responseData = await response.json();

    if (!response.ok) {
      throw new Error(
        responseData.message ? responseData.message : "RESPONSE ERROR"
      );
    }
    context.commit("setError", {
      state: false,
      message: "",
    });
    context.commit("setLoading", false);
    context.dispatch("handleData", responseData);
  } catch (error) {
    context.commit("setError", {
      state: true,
      message: error.message,
    });
    context.commit("setLoading", false);
    console.error("error:", error.message);
  }
}

export { fetchPOST, fetchGET };
